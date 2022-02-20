import socket
from cea256 import *

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
        self.expectedCEAShim = "AtlasProviderAPI-CEA-SHIM - 1.0.0"

    def ProviderVersion(self):
        return f"0.3.1 - vNext"

    def connect(self):
        # Check if correct CEAShim is installed, will also validated by the server in vNext.
        if CEAMisc.GetShimVersion() != self.expectedCEAShim:
            raise CustomError(
                f"Invalid CEA SHIM version! Expected version: {self.expectedCEAShim}")
        socket = self.socket
        try:
            socket.connect((self.host, self.port))
            if self._send(socket, f"OpCode=0;Caller={self.app_id};").split(";")[0].split("=")[1] == "8":
                self.isConnected = True
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

    def disconnect(self):
        try:
            if self.isConnected:
                self.socket.close()
                self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except Exception as e:
            raise CustomError("{}".format(e))

    def Identify(self, userHandle: str):
        socket = self.socket
        try:
            payload_id = CEADecrypt(self.app_token).CEA256(
                self._send(socket, CEAEncrypt(self.app_token).CEA256(f"OpCode=10;UserHandle={userHandle};")))
            response_code = payload_id.split(";")[0].split("=")[1]
            response_result = payload_id.split(";")[1].split("=")[1]
            if response_code == "8" and response_result == "Identified!":
                return True
            elif response_code == "2":
                raise CustomError("Username not found!")
        except Exception as e:
            self.disconnect()
            raise CustomError(e)

    def Login(self, username: str, password: str):
        socket = self.socket
        try:
            AuthReponse = CEADecrypt(self.app_token).CEA256(self._send(socket, CEAEncrypt(self.app_token).CEA256(
                f"OpCode=4;AuthOpCode=1;UserHandle={username};UserPass={password};")))
            AuthCode = AuthReponse.split(";")[0].split("=")[1]
            AuthMessage = AuthReponse.split(";")[1].split("=")[1]
            if AuthCode == "8":
                match AuthMessage:
                    case "AuthenticationSuccessful":
                        return True
                    case "AuthenticationDisabled":
                        raise CustomError(
                            "Account has been disabled, contact support")
                    case "AuthenticationFailed":
                        raise CustomError("Username/Password is invalid")
            else:
                raise CustomError(
                    "An unknown issue occured while attempting to authenticate")
        except Exception as e:
            self.disconnect()
            raise CustomError("{}".format(e))

    def Register(self, username: str, password: str):
        socket = self.socket
        try:
            RegisterPayload = CEADecrypt(self.app_token).CEA256(self._send(socket, CEAEncrypt(self.app_token).CEA256(
                f"OpCode=4;AuthOpCode=2;UserFullname={username};UserHandle={username};UserPass={password};UserEmail={username}@nomail.com;")))
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
                raise CustomError(
                    "An unknown issue occured while registering the specified user")
        except Exception as e:
            self.disconnect()
            raise CustomError("{}".format(e))

    def InitAppUser(self, hwid: str):  # Must be authenticated (See docs)
        socket = self.socket
        try:
            RegisterPayload = CEADecrypt(self.app_token).CEA256(
                self._send(socket, CEAEncrypt(self.app_token).CEA256(f"OpCode=5;AppOpCode=1;HWID={hwid};")))
            responseCode = RegisterPayload.split(";")[0].split("=")[1]
            responseResult = RegisterPayload.split(";")[1].split("=")[1]
            if responseCode == "8":
                match responseResult:
                    case "AppUserRegistrationSuccessful":
                        return True
                    case "AppUserRegistrationFailed":
                        raise CustomError(
                            "Unable to register as application user")
                    case "AppUserHWIDRegistrationFailed":
                        raise CustomError(
                            "Unable to register as application user HWID not accepted by server")
            else:
                raise CustomError(
                    "An unknown issue occured while enrolling application user")
        except Exception as e:
            self.disconnect()
            raise CustomError("{}".format(e))

    def DropAppUser(self):  # Must be authenticated (See docs)
        socket = self.socket
        try:
            RegisterPayload = CEADecrypt(self.app_token).CEA256(
                self._send(socket, CEAEncrypt(self.app_token).CEA256(f"OpCode=5;AppOpCode=2;")))
            responseCode = RegisterPayload.split(";")[0].split("=")[1]
            responseResult = RegisterPayload.split(";")[1].split("=")[1]
            if responseCode == "8":
                match responseResult:
                    case "AppUserDeRegistrationSuccessful":
                        return True
                    case "AppUserDeRegistrationFailed":
                        raise CustomError(
                            "Unable to deallocate the specified application user")
            else:
                raise CustomError(
                    "An unknown issue occured while removing the application user")
        except Exception as e:
            self.disconnect()
            raise CustomError("{}".format(e))

    # Must be authenticated (See docs)
    def RedeemEntitlement(self, LicenseKey: str, applicationSKU: str):
        socket = self.socket
        try:
            RegisterPayload = CEADecrypt(self.app_token).CEA256(self._send(socket, CEAEncrypt(self.app_token).CEA256(
                f"OpCode=5;AppOpCode=3;SLK={LicenseKey};SKU={applicationSKU};")))
            responseCode = RegisterPayload.split(";")[0].split("=")[1]
            responseResult = RegisterPayload.split(";")[1].split("=")[1]
            if responseCode == "8":
                match responseResult:
                    case "SLActivated":
                        return True
                    case "SLActivationFailed":
                        raise CustomError(
                            "An issue occured while activating the specified license key")
            else:
                raise CustomError(
                    "An unknown issue occured while redeeming the specified entitlement")
        except Exception as e:
            self.disconnect()
            raise CustomError("{}".format(e))

    # Must be authenticated (See docs)
    def ValidateEntitlement(self, applicationSKU: str):
        socket = self.socket
        try:
            RegisterPayload = CEADecrypt(self.app_token).CEA256(
                self._send(socket, CEAEncrypt(self.app_token).CEA256(f"OpCode=5;AppOpCode=4;SKU={applicationSKU};")))
            responseCode = RegisterPayload.split(";")[0].split("=")[1]
            responseResult = RegisterPayload.split(";")[1].split("=")[1]
            if responseCode == "8":
                match responseResult:
                    case "UserEntitlementValid":
                        return True
                    case "SKUValidationFailed":  # SKU should be embedded as constant, has tampering/use of incorrect version been detected?
                        raise CustomError(
                            "An issue occured while validating the specified application")
                    case "SKUInvalid":
                        raise CustomError(
                            "The specified user is not licensed to use the specified application")
                    case "UserEntitlementInvalid":
                        raise CustomError(
                            "The specified user is not licensed to use the specified application")
            else:
                raise CustomError(
                    "An unknown issue occured while validating the application")
        except Exception as e:
            self.disconnect()
            raise CustomError("{}".format(e))

    def SetUserHWID(self, hwid: str):  # Must be authenticated (See docs)
        socket = self.socket
        try:
            RegisterPayload = CEADecrypt(self.app_token).CEA256(
                self._send(socket, CEAEncrypt(self.app_token).CEA256(f"OpCode=5;AppOpCode=5;HWID={hwid};")))
            responseCode = RegisterPayload.split(";")[0].split("=")[1]
            responseResult = RegisterPayload.split(";")[1].split("=")[1]
            if responseCode == "8":
                match responseResult:
                    case "HWIDUpdated":
                        return True
                    case "HWIDUpdateFailed":
                        raise CustomError(
                            "An issue occured while attempting to update the specified user's HWID")
            else:
                raise CustomError(
                    "An unknown issue occured while attempting to update the specified user's HWID")
        except Exception as e:
            self.disconnect()
            raise CustomError("{}".format(e))

    def ValidateUserHWID(self, hwid: str):  # Must be authenticated (See docs)
        socket = self.socket
        try:
            RegisterPayload = CEADecrypt(self.app_token).CEA256(
                self._send(socket, CEAEncrypt(self.app_token).CEA256(f"OpCode=5;AppOpCode=6;HWID={hwid};")))
            responseCode = RegisterPayload.split(";")[0].split("=")[1]
            responseResult = RegisterPayload.split(";")[1].split("=")[1]
            if responseCode == "8":
                match responseResult:
                    case "HardwareIDValid":
                        return True
                    case "HardwareIDInvalid":
                        raise CustomError(
                            "The submitted hardware ID is invalid")
                    case "HardwareIDNotSet":
                        raise CustomError(
                            "No hardware ID has been set for the specified user")
            else:
                raise CustomError(
                    "An unknown issue occured while attempting to validate the specified user's HWID")
        except Exception as e:
            self.disconnect()
            raise CustomError("{}".format(e))

    def GetAppUserRole(self):  # Must be authenticated (See docs)
        socket = self.socket
        try:
            RegisterPayload = CEADecrypt(self.app_token).CEA256(
                self._send(socket, CEAEncrypt(self.app_token).CEA256(f"OpCode=5;AppOpCode=7;")))
            responseCode = RegisterPayload.split(";")[0].split("=")[1]
            responseResult = RegisterPayload.split(";")[1].split("=")[1]
            if responseCode == "8":
                return responseResult
            else:
                raise CustomError(
                    "An unknown issue occured while attempting to obtain the specified user's AppUserRole")
        except Exception as e:
            self.disconnect()
            raise CustomError("{}".format(e))

    # Must be authenticated (See docs)
    def CheckLicenseKeyValidity(self, LicenseKey: str):
        socket = self.socket
        try:
            RegisterPayload = CEADecrypt(self.app_token).CEA256(
                self._send(socket, CEAEncrypt(self.app_token).CEA256(f"OpCode=5;AppOpCode=8;SLK={LicenseKey};")))
            responseCode = RegisterPayload.split(";")[0].split("=")[1]
            responseResult = RegisterPayload.split(";")[1].split("=")[1]
            if responseCode == "8":
                match responseResult:
                    case "SLKValid":
                        return True
                    case "SLKInvalid":
                        raise CustomError(
                            "The specified license key is invalid")
                    case "SLKValidationFailed":
                        raise CustomError(
                            "An issue occured while attempting to validate the specified license key")
            else:
                raise CustomError(
                    "An unknown issue occured while attempting to validate the specified user's HWID")
        except Exception as e:
            self.disconnect()
            raise CustomError("{}".format(e))


auth_luna = Atlas("auth.project-atlas.xyz", 6969,  "02621487807712432558", "Pde67VDTmJXGCpKZLPHijiPFhZUTHcMF")

class Auth:
    