function Get-Cheatbook {
    <#
    .SYNOPSIS
        Extracts and displays a clean, unformatted log of all previous terminal commands.
    #>
    Write-Host "--- DETECTING TERMINAL HISTORY TELEMETRY ---" -ForegroundColor Cyan
    
    # Path to the persistent history log file
    $HistoryPath = (Get-PSReadLineOption).HistorySavePath
    
    if (Test-Path $HistoryPath) {
        # Fetch lines from the history file, adding index numbers
        $RawHistory = Get-Content $HistoryPath
        $Counter = 1
        
        foreach ($Command in $RawHistory) {
            # Format output neatly as a raw text checklist
            Write-Output "[$Counter] -> $Command"
            $Counter++
        }
    } else {
        Write-Host "[ERROR] Persistent history file not found." -ForegroundColor Red
    }
}
