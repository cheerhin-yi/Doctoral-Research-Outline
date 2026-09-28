Write-Output '=== 第1步: 扫描 Windows Update 可选驱动 ==='
$UpdateSession = New-Object -ComObject Microsoft.Update.Session
$Searcher = $UpdateSession.CreateUpdateSearcher()
$Searcher.ServiceID = '7971f918-a847-4430-9279-4a52d1efe18d'  # Microsoft Update
$Searcher.SearchScope = 1  # Current user
$Searcher.ServerSelection = 3  # Third party
$Result = $Searcher.Search("IsInstalled=0 and Type='Driver'")
if ($Result.Updates.Count -gt 0) {
    Write-Output "找到 $($Result.Updates.Count) 个可选驱动更新:"
    foreach ($Update in $Result.Updates) {
        Write-Output "  - $($Update.Title)"
    }
} else {
    Write-Output "没有找到可选驱动更新"
}

Write-Output ''
Write-Output '=== 第2步: 卸载当前蓝牙驱动(保留设备) ==='
# 获取当前驱动 INF
$inf = 'bth.inf'
Write-Output "当前驱动 INF: $inf"

# 删除设备并重新扫描（强制重新安装驱动）
$adapterId = 'USB\VID_0A12&PID_0001\6&14A59FFF&0&1'
Write-Output "移除设备: $adapterId"
& pnputil /remove-device "$adapterId" 2>&1 | Out-Null
Start-Sleep 3

Write-Output '=== 第3步: 扫描硬件变更(重新安装驱动) ==='
& pnputil /scan-devices 2>&1
Start-Sleep 8

Write-Output '=== 第4步: 检查结果 ==='
Write-Output '--- 蓝牙适配器状态 ---'
Get-PnpDevice -Class Bluetooth 2>$null | Where-Object { $_.FriendlyName -match 'Radio' } | Select-Object Status,FriendlyName | Format-Table -AutoSize

Write-Output '--- 驱动版本 ---'
Get-PnpDevice -Class Bluetooth 2>$null | Where-Object { $_.FriendlyName -match 'Radio' } | Get-PnpDeviceProperty -KeyName DEVPKEY_Device_DriverVersion,DEVPKEY_Device_DriverProvider 2>$null | Select-Object KeyName,Data | Format-Table -AutoSize -Wrap

Write-Output '--- 蓝牙服务 ---'
Get-Service -Name bthserv,BthAvctpSvc,BluetoothUserService_694dc 2>$null | Select-Object Name,Status | Format-Table -AutoSize

Write-Output '=== DONE ==='
