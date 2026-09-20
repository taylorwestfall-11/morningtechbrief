# Morning Tech Brief Runner
# Runs daily via Windows Task Scheduler at 6:33am

$workDir  = "D:\Claude Projects\Morning Brief"
$claude   = "C:\Users\taylo\AppData\Local\Packages\Claude_pzs8sxrjxfjjc\LocalCache\Roaming\Claude\claude-code\2.1.119\claude.exe"
$prompt   = Get-Content "$workDir\brief_prompt.txt" -Raw
$logFile  = "$workDir\brief_log.txt"
$outFile  = "$workDir\brief_last_run.txt"
$logEntry = "$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"

Add-Content $logFile "$logEntry  Starting morning brief..."

try {
    & $claude -p $prompt --dangerously-skip-permissions *>&1 | Tee-Object -FilePath $outFile | Out-Null
    $exit = $LASTEXITCODE
    if ($exit -eq 0) {
        Add-Content $logFile "$logEntry  Brief complete (exit 0). Output captured to brief_last_run.txt."
    } else {
        Add-Content $logFile "$logEntry  ERROR: claude exited with code $exit. See brief_last_run.txt for details."
    }
} catch {
    Add-Content $logFile "$logEntry  ERROR: $_"
}
