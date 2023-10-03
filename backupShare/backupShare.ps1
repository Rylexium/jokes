#$ErrorActionPreference = "Stop"

$timeExecutionBackupScript = [Diagnostics.Stopwatch]::StartNew()
$nowDate = get-date -format "dd-MM-yyyy HH_MM_s"
$pathToScriptLog = "C:\Distr\script_backup\log\backupScript_$nowDate.log"

Start-Transcript -Path $pathToScriptLog

chcp 65001 #Enable russian symbols, sometime work.

#Remove restrict max 260 character in filename.
reg delete "HKLM\SYSTEM\CurrentControlSet\Control\FileSystem" /v LongPathsEnabled /f
reg add "HKLM\SYSTEM\CurrentControlSet\Control\FileSystem" /v LongPathsEnabled /t REG_DWORD /d 1

#Get password from backup_srv and connect to share server with creds.
$pass=python -c "import keyring; print(keyring.get_password('172.17.250.10', 'backup_srv'))"
net use \\172.17.250.10 /user:backup_srv $pass

$rev=[array](Get-NetIPAddress | Select -Property IPAddress).IPAddress
$ipHost = $rev[$rev.Length - 2]

$theFolder = "\\172.17.250.10\soc-files" #path to dir what need backup
$staging = "\\$ipHost\C$\soc-files" #Tmp directory, here downloading all files from share server
$localBackup = "\\$ipHost\C$\backup(172.17.250.10)" #Here save .zip file with all files from share server.

$exclusionDirs = @("backup") #name of directory exclusion
$nameOfSmbPolicy = "SMBRestrictFileCopySpeed" #name of policy, what restrict smb(traffic) speed
$speedSMBUploadingBitsPerSecond = 1600MB

$isPreviousStepError = $false


function createDir($path) {
    if(-not(Test-Path $path)) {
        mkdir $path
    }
}

function removeDir($path){
    if(-not(Test-Path $path)){
        Remove-Item $path -Force -Recurse
        Write-Host "!!!!!! Done delete files from $path"
    }
}

function removeRestrictTrafficSMBPolicy($policy){
    if($policy -in [array](Get-NetQosPolicy | select -Property Name).Name){ #check policy, if exists delete
        Write-Host "Delete Policy: $policy"
        Remove-NetQosPolicy -Name $policy -Confirm:$false
    }
}

function sendNotificationToTelegram($msg) {
    getElapsedSeconds
    $hostname = hostname
    python C:\Distr\script_backup\main.py --msg $msg --log $pathToScriptLog --source "$hostname($ipHost)" --folder $theFolder --localbackup $localBackup --remotebackup $theFolder"\backup"
}

function getElapsedTime {
    Write-Host $timeExecutionBackupScript.Elapsed
}

createDir($localBackup) #create dir if not exists
createDir($staging)
removeDir($staging) #remove all files, if exists staging


removeRestrictTrafficSMBPolicy($nameOfSmbPolicy) #delete previous policy restrict speed smb



if($nameOfSmbPolicy -in [array](Get-NetQosPolicy | select -Property Name)){ #create policy restrict smb speed
    Write-Host "Add Policy: $nameOfSmbPolicy"
    New-NetQosPolicy -Name "$nameOfSmbPolicy" -SMB -ThrottleRateActionBitsPerSecond $speedSMBUploadingBitsPerSecond  #limit for uploading (in mbit) 800Mbit = 100mbait
}

#/b /e /xa:s /xjd /sl /a-:hs /mt /v /fp /eta
#/MIR /E /XO /xx /tee /eta /R:3 /W:1 /SEC /b /256 /mt /z
robocopy $theFolder $staging /b /e /xa:s /xjd /sl /a-:hs /R:1000 /W:2 /mt /v /fp /eta /XD \\172.17.250.10\soc-files\backup # her command not copy projects(encrypted file) and others files, because i select xcopy
#ForEach($dir in (ls $theFolder)){ #download all dir and files from share server to stage
#    if($dir -in $exclusionDirs) { #if name dir in exclusion -> continue
#        continue
#    }
#
#
#    if($dir.PSIsContainer){ #this directory, we process it different #p.s add to path "\*"
#        xcopy ($dir.FullName + "\*") ($staging + "\" + $dir + "\") /s /e
#    }
#    else{ #just copy this file
#        xcopy $dir.FullName $staging /s /e
#    }
#}

$backupZipFile = $localBackup + "\" + (Get-Date -Format "dd-MM-yyyy").ToString() + ".7z" #example path: C:\stage\25-09-2023.7z
$backupZipFile
if(Test-Path $backupZipFile) { #remove file with same name
    Remove-Item $backupZipFile -Force
}

if(-not (Test-Path $staging)){ #staging not exists throw exception
    throw [Exception] "Not found $staging"
}


if(Test-Path $backupZipFile){ #delete previous archive if exists, this script create new archive
    Remote-Item $backupZipFile -Force
}

# -bb3 - full log, -stm16 - 16 threats, -y - access all dialogs, -mx5 - step of compress, -tzip - type (zip) of archive, -ssw - analogue "force", -r0 - recursive all directories
try { #experemt with mx9, mb use mx2 or mx5. 7z(mx9): 40gb -> 29gb, zip(mx9): 40gb -> 31.8gb 
    & 'C:\Program Files\7-Zip\7z.exe' a -bb2 -stm32 -y -mx9 -t7z -ssw -r0 $backupZipFile $staging # create archive and move to local storage
    Write-Host "!!!!!! Done create zip archive"
    Write-Host "!!!!!! Done copy zip archive to local"
} catch {
    Write-Host "Error when archiving data..."
    $isPreviousStepError=$true
    sendNotificationToTelegram("архивации данных")
}

if(-not $isPreviousStepError){
    try {
        Copy-Item $backupZipFile ($theFolder+"\backup") #send archive to share server
        Write-Host "!!!!!! Done copy zip archive to \\172.17.250.10"

        removeDir($staging)
        Write-Host "!!!!!! Done delete files and directory from $staging"
    } catch {
        Write-Host "Error when send archive to share server..."
        $isPreviousStepError=$true
        sendNotificationToTelegram("отправки архива на файловый сервер")
    }
}

removeRestrictTrafficSMBPolicy($nameOfSmbPolicy)
$timeExecutionBackupScript.Stop()
getElapsedSeconds
Write-Host "========================================================"
Stop-Transcript
