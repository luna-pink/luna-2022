from encryption import *
import socket
import subprocess

# ------------------------------------------------------------------------------

class CustomError(Exception):
     pass

class Atlas:
    def __init__(self, host: str, port: int, app_id: str, app_token: str):
        self.app_id = app_id
        self.app_token = app_token
        self.host = host
        self.port = port
        self.buffer = 4096
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.isConnected = False

    def Version(self):
        return "0.3.0 - vNext"

    def _connect(self):
        try:
            socket = self.socket
            socket.connect((self.host, self.port))
            self.isConnected = True
            if self._send(socket, f"OpCode=0;Caller={self.app_id};").split(";")[0].split("=")[1] == "8":
                self._send(socket, f"OpCode=9;CipherSpec=2;")
                return True
            else:
                pass
        except Exception as e:
            raise CustomError(e)
            
    def _send(self, socket, payload: str):
        try:
            socket.send(payload.encode("utf-8"))
            return socket.recv(self.buffer).decode("utf-8")
        except Exception as e:
            raise CustomError(e)

    def _disconnect(self): # nothing wrong with this, weird, ik
        try:
            
            if self.isConnected:
                #payloadID = Decryption_Changed(self.app_token).CEA256_Changed(self._send(socket, Encryption_Changed(self.app_token).CEA256_Changed(f"OpCode=6;")))
                self.socket.close()
                self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except Exception as e:
            raise CustomError(f"Error: ".format(e))


    def Login(self, username: str, password: str):
        socket = self.socket
        try:
            payloadID = Decryption_Changed(self.app_token).CEA256_Changed(self._send(socket, Encryption_Changed(self.app_token).CEA256_Changed(f"OpCode=10;UserHandle={username};"))) # What the fuck is this? -Nshout
            responseCode = payloadID.split(";")[0].split("=")[1]
            responseResult = payloadID.split(";")[1].split("=")[1]
            if responseCode == "8" and responseResult == "Identified!":
                AuthReponse = Decryption_Changed(self.app_token).CEA256_Changed(self._send(socket, Encryption_Changed(self.app_token).CEA256_Changed(f"OpCode=4;AuthOpCode=1;UserHandle={username};UserPass={password};")))
                AuthCode = AuthReponse.split(";")[0].split("=")[1]
                AuthMessage = AuthReponse.split(";")[1].split("=")[1]
                if AuthCode == "8":
                    match AuthMessage:
                        case "AuthenticationSuccessful":
                            return True
                        case "AuthenticationDisabled":
                            raise CustomError("Account has been disabled, contact support")
                        case "AuthenticationFailed":
                            raise CustomError("Username/Password is invalid")
                         
            elif responseCode == "2":
                raise CustomError("Username not found!")
            else:
                raise CustomError("An unknown issue occured while attempting to authenticate")
        except Exception as e:
            self._disconnect()
            raise CustomError("{}".format(e))

    def Register(self, username: str, password: str):
        socket = self.socket
        try:
            RegisterPayload = Decryption_Changed(self.app_token).CEA256_Changed(self._send(socket, Encryption_Changed(self.app_token).CEA256_Changed(f"OpCode=4;AuthOpCode=2;UserFullname={username};UserHandle={username};UserPass={password};UserEmail={username}@nomail.com;")))
            responseCode = RegisterPayload.split(";")[0].split("=")[1]
            responseResult = RegisterPayload.split(";")[1].split("=")[1]
            if responseCode == "8":
                match responseResult:
                    case "Success":
                        return True
                    case "UserAlreadyExists":
                        raise CustomError("User already exists")
                    case "AccountRegistrationFailed":
                        raise CustomError("Registration failed")
            else:
                raise CustomError("An unknown issue occured while registering the specified user")
        except Exception as e:
            self._disconnect()
            raise CustomError("{}".format(e))


    def InitAppUser(self, hwid: str): # Must be authenticated (See docs)
        socket = self.socket
        try:
            RegisterPayload = Decryption_Changed(self.app_token).CEA256_Changed(self._send(socket, Encryption_Changed(self.app_token).CEA256_Changed(f"OpCode=5;AppOpCode=1;HWID={hwid};")))
            responseCode = RegisterPayload.split(";")[0].split("=")[1]
            responseResult = RegisterPayload.split(";")[1].split("=")[1]
            if responseCode == "8":
                match responseResult:
                    case "AppUserRegistrationSuccessful":
                        return True
                    case "AppUserRegistrationFailed":
                        raise CustomError("Unable to register as application user")
                    case "AppUserHWIDRegistrationFailed":
                        raise CustomError("Unable to register as application user HWID not accepted by server")
            else:
                raise CustomError("An unknown issue occured while enrolling application user")
        except Exception as e:
            self._disconnect()
            raise CustomError("{}".format(e))

    
    def DropAppUser(self): # Must be authenticated (See docs)
        socket = self.socket
        try:
            RegisterPayload = Decryption_Changed(self.app_token).CEA256_Changed(self._send(socket, Encryption_Changed(self.app_token).CEA256_Changed(f"OpCode=5;AppOpCode=2;")))
            responseCode = RegisterPayload.split(";")[0].split("=")[1]
            responseResult = RegisterPayload.split(";")[1].split("=")[1]
            if responseCode == "8":
                match responseResult:
                    case "AppUserDeRegistrationSuccessful":
                        return True
                    case "AppUserDeRegistrationFailed":
                        raise CustomError("Unable to deallocate the specified application user")
            else:
                raise CustomError("An unknown issue occured while removing the application user")
        except Exception as e:
            self._disconnect()
            raise CustomError("{}".format(e))

    def RedeemEntitlement(self, LicenseKey: str, applicationSKU: str): # Must be authenticated (See docs)
        socket = self.socket
        try:
            RegisterPayload = Decryption_Changed(self.app_token).CEA256_Changed(self._send(socket, Encryption_Changed(self.app_token).CEA256_Changed(f"OpCode=5;AppOpCode=3;SLK={LicenseKey};SKU={applicationSKU};")))
            responseCode = RegisterPayload.split(";")[0].split("=")[1]
            responseResult = RegisterPayload.split(";")[1].split("=")[1]
            if responseCode == "8":
                match responseResult:
                    case "SLActivated": # the functions that are being called are missing (self) i think
                        return True
                    case "SLActivationFailed":
                        raise CustomError("An issue occured while activating the specified license key")
            else:
                raise CustomError("An unknown issue occured while redeeming the specified entitlement")
        except Exception as e:
            self._disconnect()
            raise CustomError("{}".format(e))

    def ValidateEntitlement(self, applicationSKU: str): # Must be authenticated (See docs)
        socket = self.socket
        try:
            RegisterPayload = Decryption_Changed(self.app_token).CEA256_Changed(self._send(socket, Encryption_Changed(self.app_token).CEA256_Changed(f"OpCode=5;AppOpCode=4;SKU={applicationSKU};")))
            responseCode = RegisterPayload.split(";")[0].split("=")[1]
            responseResult = RegisterPayload.split(";")[1].split("=")[1]
            if responseCode == "8":
                match responseResult:
                    case "UserEntitlementValid":
                        return True
                    case "SKUValidationFailed": # SKU should be embedded as constant, has tampering/use of incorrect version been detected?
                        raise CustomError("An issue occured while validating the specified application") 
                    case "SKUInvalid":
                        raise CustomError("The specified user is not licensed to use the specified application")
                    case "UserEntitlementInvalid":
                        raise CustomError("The specified user is not licensed to use the specified application")
            else:
                raise CustomError("An unknown issue occured while validating the application")
        except Exception as e:
            self._disconnect()
            raise CustomError("{}".format(e))

    def SetUserHWID(self, hwid: str): # Must be authenticated (See docs)
        socket = self.socket
        try:
            RegisterPayload = Decryption_Changed(self.app_token).CEA256_Changed(self._send(socket, Encryption_Changed(self.app_token).CEA256_Changed(f"OpCode=5;AppOpCode=5;HWID={hwid};")))
            responseCode = RegisterPayload.split(";")[0].split("=")[1]
            responseResult = RegisterPayload.split(";")[1].split("=")[1]
            if responseCode == "8":
                match responseResult:
                    case "HWIDUpdated":
                        return True
                    case "HWIDUpdateFailed":
                        raise CustomError("An issue occured while attempting to update the specified user's HWID") 
            else:
                raise CustomError("An unknown issue occured while attempting to update the specified user's HWID")
        except Exception as e:
            self._disconnect()
            raise CustomError("{}".format(e))
    
    def ValidateUserHWID(self, hwid: str): # Must be authenticated (See docs)
        socket = self.socket
        try:
            RegisterPayload = Decryption_Changed(self.app_token).CEA256_Changed(self._send(socket, Encryption_Changed(self.app_token).CEA256_Changed(f"OpCode=5;AppOpCode=6;HWID={hwid};")))
            responseCode = RegisterPayload.split(";")[0].split("=")[1]
            responseResult = RegisterPayload.split(";")[1].split("=")[1]
            if responseCode == "8":
                match responseResult:
                    case "HardwareIDValid":
                        return True
                    case "HardwareIDInvalid":
                        raise CustomError("The submitted hardware ID is invalid")
                    case "HardwareIDNotSet":
                        raise CustomError("No hardware ID has been set for the specified user")
            else:
                raise CustomError("An unknown issue occured while attempting to validate the specified user's HWID")
        except Exception as e:
            self._disconnect()
            raise CustomError("{}".format(e))

    def GetAppUserRole(self): # Must be authenticated (See docs)
        socket = self.socket
        try:
            RegisterPayload = Decryption_Changed(self.app_token).CEA256_Changed(self._send(socket, Encryption_Changed(self.app_token).CEA256_Changed(f"OpCode=5;AppOpCode=7;")))
            responseCode = RegisterPayload.split(";")[0].split("=")[1]
            responseResult = RegisterPayload.split(";")[1].split("=")[1]
            if responseCode == "8":
                return responseResult
            else:
                raise CustomError("An unknown issue occured while attempting to obtain the specified user's AppUserRole")
        except Exception as e:
            self._disconnect()
            raise CustomError("{}".format(e))


