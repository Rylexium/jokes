$tasks = (Get-ScheduledTask).Actions
$res = [System.Collections.Arraylist]::New()
$trigger_in_cmdline = "lsass" #на что триггеримся в командной строке
foreach($task in $tasks) {
    if (($task | select Execute) -match $trigger_in_cmdline){
        $res.Add($task)
    }
}

$path = "\\172.17.123.4\files\res_scan\" + $(hostname)+".txt" #укажите файловую шару с сетевым доступом для вывода результата, либо локальный путь, если шара не доступна
if ($res.Count -ne 0) {
    echo "===================================">>$path
    echo $("username : " + $(whoami))>>$path

    $hostIps = Get-NetIPAddress | Select IPAddress
    foreach($hostIp in $hostIps){
        echo ($hostIp)>>$path
    }

    echo $("Tasks :")>>$path
    foreach($task in $res) {
        echo ($task)>>$path
    }
}
