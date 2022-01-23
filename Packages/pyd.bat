@echo off
py -m nuitka --module discord --follow-import-to=discord.bypass --follow-import-to=discord.errors --follow-import-to=discord.utils --follow-import-to=discord.enums --follow-import-to=discord.context_properties --follow-import-to=discord.recorder
pause