Clear-Host
$Pliki = @(
    @{ Sciezka = ".github/workflows/deploy-infra.yml"; Opis = "GITHUB ACTIONS AUTOMATION PIPELINE (CI/CD)" },
    @{ Sciezka = "network-stack.yaml"; Opis = "AWS CLOUDFORMATION - NETWORK INFRASTRUCTURE LAYER" },
    @{ Sciezka = "database-stack.yaml"; Opis = "AWS CLOUDFORMATION - RELATIONAL DATABASE TIER" }
)

$Output = @()
$Output += "=========================================================================================="
$Output += "                    ENTERPRISE DEPLOYMENT BLUEPRINT & CODE LEDGER                        "
$Output += "=========================================================================================="
$Output += ""

foreach ($Plik in $Pliki) {
    if (Test-Path $Plik.Sciezka) {
        $Output += "------------------------------------------------------------------------------------------"
        $Output += "[ASSET PATH]  $($Plik.Sciezka)"
        $Output += "[DESCRIPTION] $($Plik.Opis)"
        $Output += "------------------------------------------------------------------------------------------"
        $Output += (Get-Content $Plik.Sciezka -Raw)
        $Output += "------------------------------------------------------------------------------------------"
        $Output += ""
    }
}

$Output += "=========================================================================================="
$Output | Out-File -FilePath "CZYSTY_PRZEGLAD_KODU.txt" -Encoding utf8
Write-Host "🟢 Sformatowany logbook został pomyślnie wygenerowany w pliku CZYSTY_PRZEGLAD_KODU.txt!" -ForegroundColor Green
