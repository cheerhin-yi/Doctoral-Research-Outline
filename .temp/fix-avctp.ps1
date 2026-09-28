Write-Output '=== 强制重启 AVCTP 服务 ==='
# 先尝试正常停止
Stop-Service -Name BthAvctpSvc -Force -ErrorAction SilentlyContinue
Start-Sleep 2

# 如果还卡着，杀进程
$svc = Get-CimInstance Win32_Service -Filter "Name='BthAvctpSvc'" -ErrorAction SilentlyContinue
if ($svc -and $svc.ProcessId -gt 0) {
    Write-Output "Killing PID: $($svc.ProcessId)"
    Stop-Process -Id $svc.ProcessId -Force -ErrorAction SilentlyContinue
    Start-Sleep 2
}

# 重新启动
Start-Service -Name BthAvctpSvc -ErrorAction SilentlyContinue
Start-Sleep 2

# 同时重启 AudioEndpointBuilder
Restart-Service -Name AudioEndpointBuilder -Force -ErrorAction SilentlyContinue
Start-Sleep 2
Restart-Service -Name Audiosrv -Force -ErrorAction SilentlyContinue
Start-Sleep 3

Write-Output '=== 服务最终状态 ==='
Get-Service -Name BthAvctpSvc,AudioEndpointBuilder,Audiosrv | Select-Object Name,Status | Format-Table -AutoSize

Write-Output '=== 蓝牙音频端点 ==='
Get-PnpDevice -Class AudioEndpoint 2>$null | Where-Object { $_.FriendlyName -match 'vivo|ROSE' } | Select-Object Status,FriendlyName | Format-Table -AutoSize

Write-Output '=== DONE ==='
