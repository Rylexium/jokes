#$ErrorActionPreference = "Stop"
$timeExecutionBackupScript = [Diagnostics.Stopwatch]::StartNew()

chcp 65001 #Enable russian symbols, sometime work.

#Remove restrict max 260 character in filename.
reg delete "HKLM\SYSTEM\CurrentControlSet\Control\FileSystem" /v LongPathsEnabled /f
reg add "HKLM\SYSTEM\CurrentControlSet\Control\FileSystem" /v LongPathsEnabled /t REG_DWORD /d 1

#Get password from backup_srv and connect to share server with creds.
$pass=python -c "import keyring; print(keyring.get_password('172.17.250.10', 'backup_srv'))"
net use \\172.17.250.10 /user:backup_srv $pass

$theFolder = "\\172.17.250.10\soc-files" #path to dir what need backup
$staging = "C:\soc-files" #Tmp directory, here downloading all files from share server
$localBackup = "C:\backup(172.17.250.10)" #Here save .zip file with all files from share server.

$exclusionDirs = @("backup") #name of directory exclusion
$nameOfSmbPolicy="SMBRestrictFileCopySpeed" #name of policy, what restrict smb(traffic) speed


function createDir($path) {
    if(-not(Test-Path $path)) {
        mkdir $path
    }
}

function removeFilesDir($path){
    if(-not(Test-Path $path)){
        Remove-Item $path\* -Recurse -Force
        Write-Host "!!!!!! Done delete files from $path"
    }
}

createDir($localBackup)
createDir($staging)
#removeFilesDir($staging)



if($nameOfSmbPolicy -in [array](Get-NetQosPolicy | select -Property Name)){ #check policy, if exists delete
    Write-Host "Delete Policy: $nameOfSmbPolicy"
    Remove-NetQosPolicy -Name $nameOfSmbPolicy -Confirm:$false
}


if($nameOfSmbPolicy -in [array](Get-NetQosPolicy | select -Property Name)){ #create policy restrict smb speed
    Write-Host "Add Policy: $nameOfSmbPolicy"
    New-NetQosPolicy -Name "$nameOfSmbPolicy" -SMB -ThrottleRateActionBitsPerSecond 1600MB #limit for uploading (in mbit) 800Mbit = 100mbait
}


ForEach($dir in (ls $theFolder)){ #download all dir and files from share server to stage
    if($dir -in $exclusionDirs) { #if name dir in exclusion -> continue
        continue
    }

    #Write-Host ("Directory: " + $dir.PSIsContainer + " " + $dir.FullName)
    if($dir.PSIsContainer){ #this directory, we process it different #p.s add to path "\*"
        #xcopy ($dir.FullName + "\*") ($staging + "\" + $dir + "\") /s /e 
    }
    else{ #just copy this file
        #xcopy $dir.FullName $staging /s /e
    }
}

$backupZipFile = $localBackup + "\" + (Get-Date -Format "dd-MM-yyyy").ToString() + ".7z" #example path: C:\stage\25-09-2023.zip
$backupZipFile
if(Test-Path $backupZipFile) { #remove file with same name
    Remove-Item $backupZipFile -Force
}

if(-not (Test-Path $staging)){ #staging not exists throw exception
    throw [Exception] "Not found $staging"
}


if(Test-Path $backupZipFile){
    Remote-Item $backupZipFile -Force
}

# -bb3 - full log, -stm16 - 16 threats, -y - access all dialogs, -mx5 - step of compress, -tzip - type (zip) of archive, -ssw - analogue "force", -r0 - recursive all directories
try{ #mx2 40gb -> 30gb, mx5 40gb -> ?gb, mx9 40gb ->?gb
    & 'C:\Program Files\7-Zip\7z.exe' a -bb2 -stm32 -y -mx9 -t7z -ssw -r0 $backupZipFile $staging # create archive and move to local storage
}catch {
    Write-Host "Error when archiving data..."
}

Write-Host "!!!!!! Done create zip archive"
Write-Host "!!!!!! Done copy zip archive to local"

Copy-Item $backupZipFile ($theFolder+"\backup") #send archive to share server
Write-Host "!!!!!! Done copy zip archive to \\172.17.250.10"

#removeFilesDir($staging)
#Remove-Item $staging
Write-Host "!!!!!! Done delete files and directory from $staging"

Remove-NetQosPolicy -Name $nameOfSmbPolicy -Confirm:$false
$timeExecutionBackupScript.Stop()
$timeExecutionBackupScript.Elapsed
Write-Host "========================================================"
