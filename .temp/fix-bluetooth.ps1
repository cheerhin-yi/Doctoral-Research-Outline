# 1. 禁用正常的蓝牙适配器
Write-Output '=== 禁用蓝牙适配器 ==='
Disable-PnpDevice -InstanceId 'USB\VID_0A12&PID_0001\6&14A59FFF&0&1' -Confirm:$false -ErrorAction SilentlyContinue
Start-Sleep 3

# 2. 清除异常适配器实例（ghost 设备）
Write-Output '=== 清除异常实例 ==='
$ghosts = @('USB\VID_0A12&PID_0001\6&1CE2DEFA&0&7','USB\VID_0A12&PID_0001\6&1CE2DEFA&0&12')
foreach ($g in $ghosts) {
    Write-Output "Removing: $g"
    & pnputil /remove-device $g 2>&1 | Select-Object -First 5
}

# 3. 重新启用蓝牙适配器
Write-Output '=== 重新启用蓝牙适配器 ==='
Start-Sleep 2
Enable-PnpDevice -InstanceId 'USB\VID_0A12&PID_0001\6&14A59FFF&0&1' -Confirm:$false -ErrorAction SilentlyContinue
Start-Sleep 5

# 4. 检查结果
Write-Output '=== 蓝牙适配器状态 ==='
Get-PnpDevice -Class Bluetooth 2>$null | Where-Object { $_.FriendlyName -match 'Radio' } | Select-Object Status,FriendlyName,InstanceId | Format-Table -AutoSize -Wrap

Write-Output '=== 蓝牙音频端点状态 ==='
Get-PnpDevice -Class AudioEndpoint 2>$null | Where-Object { $_.FriendlyName -match 'vivo|ROSE' } | Select-Object Status,FriendlyName | Format-Table -AutoSize

Write-Output '=== DONE ==='
