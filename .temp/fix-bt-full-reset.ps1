Write-Output '=== 第1步: 移除两只耳机配对 ==='
$devices = Get-PnpDevice -Class Bluetooth 2>$null | Where-Object { $_.FriendlyName -match 'vivo TWS Air3|ROSE CAMBRIAN' }
foreach ($d in $devices) {
    Write-Output "Removing: $($d.FriendlyName)"
    & pnputil /remove-device "$($d.InstanceId)" 2>&1 | Out-Null
}
Start-Sleep 2

Write-Output '=== 第2步: 停止 AudioEndpointBuilder（解锁设备）==='
Stop-Service -Name AudioEndpointBuilder -Force -ErrorAction SilentlyContinue
Start-Sleep 2

Write-Output '=== 第3步: 停止 Windows Audio ==='
Stop-Service -Name Audiosrv -Force -ErrorAction SilentlyContinue
Start-Sleep 1

Write-Output '=== 第4步: 禁用蓝牙适配器 ==='
Disable-PnpDevice -InstanceId 'USB\VID_0A12&PID_0001\6&14A59FFF&0&1' -Confirm:$false -ErrorAction SilentlyContinue
Start-Sleep 5

Write-Output '=== 第5步: 重新启用蓝牙适配器 ==='
Enable-PnpDevice -InstanceId 'USB\VID_0A12&PID_0001\6&14A59FFF&0&1' -Confirm:$false -ErrorAction SilentlyContinue
Start-Sleep 5

Write-Output '=== 第6步: 启动 Windows Audio ==='
Start-Service -Name Audiosrv -ErrorAction SilentlyContinue
Start-Sleep 2

Write-Output '=== 第7步: 启动 AudioEndpointBuilder ==='
Start-Service -Name AudioEndpointBuilder -ErrorAction SilentlyContinue
Start-Sleep 3

Write-Output '=== 最终状态 ==='
Write-Output '--- 服务 ---'
Get-Service -Name Audiosrv,AudioEndpointBuilder,BthAvctpSvc,bthserv | Select-Object Name,Status | Format-Table -AutoSize
Write-Output '--- 蓝牙适配器 ---'
Get-PnpDevice -Class Bluetooth 2>$null | Where-Object { $_.FriendlyName -match 'Radio' } | Select-Object Status,FriendlyName | Format-Table -AutoSize
Write-Output '--- 蓝牙耳机(应为空) ---'
Get-PnpDevice -Class Bluetooth 2>$null | Where-Object { $_.FriendlyName -match 'vivo|ROSE' } | Select-Object Status,FriendlyName | Format-Table -AutoSize
Write-Output '--- 音频端点 ---'
Get-PnpDevice -Class AudioEndpoint -Status OK 2>$null | Select-Object FriendlyName | Format-Table -AutoSize

Write-Output '=== DONE ==='
