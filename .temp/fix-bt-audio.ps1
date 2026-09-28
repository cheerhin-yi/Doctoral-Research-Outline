Write-Output '=== 重启蓝牙音频服务 ==='
# 重启蓝牙用户服务
Restart-Service -Name BluetoothUserService_694dc -Force -ErrorAction SilentlyContinue
Start-Sleep 1
# 重启 AVCTP 服务
Restart-Service -Name BthAvctpSvc -Force -ErrorAction SilentlyContinue
Start-Sleep 1
# 重启蓝牙支持服务
Restart-Service -Name bthserv -Force -ErrorAction SilentlyContinue
Start-Sleep 3

Write-Output '=== 服务状态 ==='
Get-Service -Name BluetoothUserService_694dc,BthAvctpSvc,bthserv 2>$null | Select-Object Name,Status | Format-Table -AutoSize

# 禁用再启用蓝牙适配器（强制重新枚举音频端点）
Write-Output '=== 重新枚举蓝牙适配器 ==='
Disable-PnpDevice -InstanceId 'USB\VID_0A12&PID_0001\6&14A59FFF&0&1' -Confirm:$false -ErrorAction SilentlyContinue
Start-Sleep 3
Enable-PnpDevice -InstanceId 'USB\VID_0A12&PID_0001\6&14A59FFF&0&1' -Confirm:$false -ErrorAction SilentlyContinue
Start-Sleep 8

Write-Output '=== 蓝牙音频端点状态 ==='
Get-PnpDevice -Class AudioEndpoint 2>$null | Where-Object { $_.FriendlyName -match 'vivo|ROSE' } | Select-Object Status,FriendlyName | Format-Table -AutoSize

Write-Output '=== DONE ==='
