# 关闭蓝牙 A2DP 绝对音量
# 让 Windows 回退到软件音量控制（PCM 衰减），系统滑块直接生效

Write-Output '=== 关闭 A2DP 绝对音量 ==='

# 注册表路径
$paths = @(
    'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Bluetooth\Audio\A2DP',
    'HKLM:\SYSTEM\CurrentControlSet\Control\Bluetooth\Audio\A2DP'
)

foreach ($p in $paths) {
    # 确保路径存在
    if (-not (Test-Path $p)) {
        New-Item -Path $p -Force | Out-Null
        Write-Output "创建路径: $p"
    }
    # 设置 AbsoluteVolumeEnabled = 0
    Set-ItemProperty -Path $p -Name 'AbsoluteVolumeEnabled' -Value 0 -Type DWord -ErrorAction SilentlyContinue
    Write-Output "设置: $p -> AbsoluteVolumeEnabled = 0"
}

# 同时禁用 AVRCP 绝对音量（备用键）
$avrcpPath = 'HKLM:\SYSTEM\CurrentControlSet\Services\BthAvctpSvc\Parameters'
if (Test-Path $avrcpPath) {
    Set-ItemProperty -Path $avrcpPath -Name 'AbsoluteVolume' -Value 0 -Type DWord -ErrorAction SilentlyContinue
    Write-Output "设置: $avrcpPath -> AbsoluteVolume = 0"
}

Write-Output ''
Write-Output '=== 重启音频服务使设置生效 ==='
Restart-Service -Name AudioEndpointBuilder -Force -ErrorAction SilentlyContinue
Start-Sleep 2
Restart-Service -Name Audiosrv -Force -ErrorAction SilentlyContinue
Start-Sleep 3

Write-Output '=== 服务状态 ==='
Get-Service -Name Audiosrv,AudioEndpointBuilder | Select-Object Name,Status | Format-Table -AutoSize

Write-Output '=== 验证注册表 ==='
foreach ($p in $paths) {
    $val = (Get-ItemProperty -Path $p -Name 'AbsoluteVolumeEnabled' -ErrorAction SilentlyContinue).AbsoluteVolumeEnabled
    Write-Output "$p -> AbsoluteVolumeEnabled = $val"
}

Write-Output '=== DONE ==='
