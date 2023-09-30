#$ErrorActionPreference = "Stop"

chcp 65001

reg delete "HKLM\SYSTEM\CurrentControlSet\Control\FileSystem" /v LongPathsEnabled /f
reg add "HKLM\SYSTEM\CurrentControlSet\Control\FileSystem" /v LongPathsEnabled /t REG_DWORD /d 1

$pass=python -c "import keyring; print(keyring.get_password('172.17.250.10', 'backup_srv'))"
net use \\172.17.250.10 /user:backup_srv $pass

$theFolder = "\\172.17.250.10\soc-files"
$staging = "C:\soc-files"
$local_backup = "C:\backup(172.17.250.10)"


function createDir($path) {
    if(-not(Test-Path $path)) {
        mkdir $path
    }
}

createDir($local_backup)
createDir($staging)

Remove-Item $staging\* -Recurse -Force
Remove-Item $staging
Write-Host "!!!!!! Done delete files from staging"

$dirs = ls $theFolder
$exclusionDirs = @("backup")
$nameOfSmbPolicy="SMBRestrictFileCopySpeed"

if($nameOfSmbPolicy -in [array](Get-NetQosPolicy | select -Property Name)){
    Write-Host "Delete Policy: $nameOfSmbPolicy"
    Remove-NetQosPolicy -Name $nameOfSmbPolicy -Confirm:$false
}


if($nameOfSmbPolicy -in [array](Get-NetQosPolicy | select -Property Name)){
    Write-Host "Add Policy: $nameOfSmbPolicy"
    New-NetQosPolicy -Name "$nameOfSmbPolicy" -SMB -ThrottleRateActionBitsPerSecond 1600MB #limit for uploading (in mbit) 800Mbit = 100mbait
}


ForEach($dir in $dirs){ #xcopy $theFolder\ $staging /s /e
    if($dir -in $exclusionDirs) {
        continue
    }

    #Write-Host ("Directory: " + $dir.PSIsContainer + " " + $dir.FullName)
    if($dir.PSIsContainer){ #this directory
        xcopy ($dir.FullName + "\*") ($staging + "\" + $dir + "\") /s /e 
    }
    else{
        xcopy $dir.FullName $staging /s /e
    }
    

}
$backupZipFile = $local_backup + "\" + (Get-Date -Format "dd-MM-yyyy").ToString() + ".zip"
$backupZipFile
if(Test-Path $backupZipFile) {
    Remove-Item $backupZipFile -Force
}

if((Test-Path $staging)){
    & 'C:\Program Files\7-Zip\7z.exe' a -bb3 -stm16 -y -mx5 -tzip -ssw -r0 $backupZipFile $staging\* # create archive and move to local storage
    Write-Host "!!!!!! Done create zip archive"
    Write-Host "!!!!!! Done copy zip archive to local"

    Copy-Item $backupZipFile ($theFolder+"\backup") #send archive to share server
    Write-Host "!!!!!! Done copy zip archive to \\172.17.250.10"

    Remove-Item $staging\* -Recurse -Force
    Remove-Item $staging
    Write-Host "!!!!!! Done delete files from staging"
    Remove-NetQosPolicy -Name $nameOfSmbPolicy -Confirm:$false
    Write-Host "========================================================"
}
else{
    Write-Host "!!!!!! Directory $staging is not exists."
}
