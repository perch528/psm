@echo off

:: 要移动的文件名（如果和脚本不在同一目录，请写完整路径）
set "FILE_TO_MOVE_EXE=minion.exe"
set "FILE_TO_MOVE_TXT=group_config.txt"

:: 当前用户的Windows启动目录
set "STARTUP_DIR=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup"

:: 执行移动命令
copy "%FILE_TO_MOVE_EXE%" "%STARTUP_DIR%"
copy "%FILE_TO_MOVE_TXT%" "%STARTUP_DIR%"

:: 提示结果并退出
if %errorlevel% equ 0 (
    echo 文件 "%FILE_TO_MOVE%" 已成功移动到启动目录。
    explorer.exe %STARTUP_DIR%
) else (
    echo 移动失败！请检查文件是否存在，或者是否有权限。
)

pause