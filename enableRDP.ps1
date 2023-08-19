$rdpPort = 3389

#set RDP port
Set-ItemProperty -Path "HKLM:\System\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp\" -Name PortNumber -Value $rdpPort

# Turn on RDP
Set-ItemProperty -Path 'HKLM:\System\CurrentControlSet\Control\Terminal Server' -name "fDenyTSConnections" -Value 0
Set-ItemProperty -Path 'HKLM:\System\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp' -name UserAuthentication -Value 0

Set-ItemProperty -Path 'HKLM:\SOFTWARE\Policies\Microsoft\Windows NT\Terminal Services' -name 'fSingleSessionPerUser' -Value 0
Set-ItemProperty -Path 'HKLM:\SOFTWARE\Policies\Microsoft\Windows NT\Terminal Services' -name 'MaxInstanceCount' -Value 4

#add to firewall
netsh advfirewall firewall add rule name="allow RemoteDesktop" dir=in protocol=TCP localport=$rdpPort action=allow
netsh advfirewall firewall add rule name="allow RemoteDesktop" dir=in protocol=UDP localport=$rdpPort action=allow

#create RDP user
$username='rylexium'
$params = @{
    Name        = $username
    Password    = [securestring]::new("123456")
    FullName    = 'RDP User'
    Description = 'Description of this account.'
}
New-LocalUser @params
Add-LocalGroupMember -Group "Remote Desktop Users" -Member $username
Add-LocalGroupMember -Group "Пользователи удаленного рабочего стола" -Member $username
net localgroup "Remote Desktop Users" /add $username
net localgroup "Пользователи удаленного рабочего стола" /add $username

#restart services and set many sessions on host
Stop-Service UmRdpService -Force
Stop-Service TermService -Force
$termsrv_dll_acl = Get-Acl c:\windows\system32\termsrv.dll
Copy-Item c:\windows\system32\termsrv.dll c:\windows\system32\termsrv.dll.copy
takeown /f c:\windows\system32\termsrv.dll
$new_termsrv_dll_owner = (Get-Acl c:\windows\system32\termsrv.dll).owner
cmd /c "icacls c:\windows\system32\termsrv.dll /Grant $($new_termsrv_dll_owner):F /C"
# search for a pattern in termsrv.dll file 
$dll_as_bytes = Get-Content c:\windows\system32\termsrv.dll -Raw -Encoding byte
$dll_as_text = $dll_as_bytes.forEach('ToString', 'X2') -join ' '
$patternregex = ([regex]'39 81 3C 06 00 00(\s\S\S){6}')
$patch = 'B8 00 01 00 00 89 81 38 06 00 00 90'
$checkPattern=Select-String -Pattern $patternregex -InputObject $dll_as_text
If ($checkPattern -ne $null) {
    $dll_as_text_replaced = $dll_as_text -replace $patternregex, $patch
}
Elseif (Select-String -Pattern $patch -InputObject $dll_as_text) {
    Write-Output 'The termsrv.dll file is already patched, exiting'
    Exit
}
else { 
    Write-Output "Pattern not found "
}
# patching termsrv.dll
[byte[]] $dll_as_bytes_replaced = -split $dll_as_text_replaced -replace '^', '0x'
Set-Content c:\windows\system32\termsrv.dll.patched -Encoding Byte -Value $dll_as_bytes_replaced
# comparing two files 
fc.exe /b c:\windows\system32\termsrv.dll.patched c:\windows\system32\termsrv.dll
# replacing the original termsrv.dll file 
Copy-Item c:\windows\system32\termsrv.dll.patched c:\windows\system32\termsrv.dll -Force
Set-Acl c:\windows\system32\termsrv.dll $termsrv_dll_acl
Start-Service UmRdpService
Start-Service TermService


#add this script to scheduler task (on future)