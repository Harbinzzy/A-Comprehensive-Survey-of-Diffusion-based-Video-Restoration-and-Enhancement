$ErrorActionPreference = 'Stop'
$taskRoot = Split-Path -Parent $PSScriptRoot
Push-Location $taskRoot
try {
    latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build paper.tex
    if ($LASTEXITCODE -ne 0) { throw 'LaTeX build failed.' }
    Copy-Item -LiteralPath 'build/paper.pdf' -Destination 'paper.pdf' -Force
    Write-Host 'Built paper.pdf'
} finally { Pop-Location }
