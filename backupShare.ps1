$ErrorActionPreference = "Stop"

#$theFolder = "C:\Users\aleks\ERMACK"
#Copy-Item : Слишком длинный путь или имя файла. Полное имя файла должно содержать меньше 260 знаков, а имя каталога - меньше 248 знаков.

[Console]::OutputEncoding = [System.Text.Encoding]::GetEncoding("utf-8")
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

$dirs = ls $theFolder
$exclusionDirs = @("backup")

ForEach($dir in $dirs){ #xcopy $theFolder\ $staging /s /e
    if($dir -in $exclusionDirs) {
        continue
    }

    #Write-Host ("Directory: " + $dir.PSIsContainer + " " + $dir.FullName)
    if($dir.PSIsContainer){ #this directory
        #Write-Host $dir.FullName $dirStaging
        xcopy ($dir.FullName + "\*") ($staging + "\" + $dir + "\") /s /e 
    }
    else{
        #Write-Host $dir.FullName ($dirStaging + $dir) #тута ошибка, файл помечает как директория. НО С xcopy всё работает, просто раскоменти
        xcopy $dir.FullName $staging /s /e
    }


}
$backupZipFile = $staging + "\" + (Get-Date -Format "dd-MM-yyyy").ToString() + ".zip"
$backupZipFile


& "C:\Program Files\7-Zip\7z.exe" a -tzip -ssw -mx1 -pPassword -r0 $backupZipFile $staging
Write-Host "!!!!!! Done create zip archive"


Copy-Item $backupZipFile ($theFolder+"\backup") #try xcopy /s /e
Write-Host "!!!!!! Done copy zip archive to \\172.17.250.10"

Copy-Item $backupZipFile $local_backup #try xcopy /s /e
Write-Host "!!!!!! Done copy zip archive to local"


Remove-Item $staging\* -Recurse -Force
Remove-Item $staging
Write-Host "!!!!!! Done delete files from staging"
