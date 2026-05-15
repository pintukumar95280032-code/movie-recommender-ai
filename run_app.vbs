Set WshShell = CreateObject("WScript.Shell")
' Yeh line aapki .bat file ko bina black screen dikhaye chalayegi
WshShell.Run chr(34) & "MovieApp.bat" & Chr(34), 0
Set WshShell = Nothing