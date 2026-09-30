# TDOP documentation consistency validator (repository-relative).
# Runs inside the TDOP-docs clone (locally or in CI). Exit code 1 on any FAIL.
$ErrorActionPreference = "Stop"
$root = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)  # repo root (scripts/..)
$pmRaw = Get-Content "$root\PROJECT_MANAGEMENT.md" -Raw -Encoding UTF8
$tbRaw = Get-Content "$root\TASK_BREAKDOWN.md" -Raw -Encoding UTF8

$names = @(
"Project Initiation","Requirements Engineering","System Analysis","System Architecture",
"Database Design","API & Contract Design","Development Environment","Backend Foundation",
"Frontend Foundation","Authentication & Authorization","User & Profile Module",
"Organization Module","Opportunity Core","Trust & Verification","Discovery & Search",
"Application Engine","Notification System","Deadline & Freshness",
"Personalization & Matching","Administration & Governance","Analytics & Outcomes",
"Advanced Data Quality & Source Management","External Opportunity Ingestion",
"Advanced Intelligence / AI","Communication Expansion","Subscription / Business Model",
"Complete Security Hardening","Complete Testing","Performance & Reliability",
"Deployment & CI/CD","Beta Release","Production Launch","Continuous Improvement")

$ok = $true
function Check($label, $cond, $detail = "") {
  $script:ok = $script:ok -and $cond
  "{0} [{1}] {2}" -f $(if ($cond) { "PASS" } else { "FAIL" }), $label, $detail
}

$governance = "CHANGELOG.md","CODE_OF_CONDUCT.md","DEVELOPMENT_GUIDE.md","LICENSE","SECURITY.md","SECURITY_STANDARDS.md","CONTRIBUTING.md","PROJECT_MANAGEMENT.md","CODING_STANDARDS.md","MAINTAINERS.md"
Check "governance files exist" (($governance | Where-Object { -not (Test-Path "$root\$_") }).Count -eq 0)
Check "TASK_BREAKDOWN.md exists" (Test-Path "$root\TASK_BREAKDOWN.md")
Check "EXISTING_IMPLEMENTATION_AUDIT.md exists" (Test-Path "$root\EXISTING_IMPLEMENTATION_AUDIT.md")
Check "Specs/SRS.md exists" (Test-Path "$root\Specs\SRS.md")
Check "Specs/ roadmap + deployment exist" ((Test-Path "$root\Specs\IMPLEMENTATION & FUTURE ROADMAP.md") -and (Test-Path "$root\Specs\DEPLOYMENT_CHECKLIST.md"))
Check "LICENSE is MIT" ((Get-Content "$root\LICENSE" -Raw -Encoding UTF8) -match "MIT License")
Check "completion roadmap section present" ($pmRaw -match "33-phase" -and (Get-Content "$root\Specs\IMPLEMENTATION & FUTURE ROADMAP.md" -Raw -Encoding UTF8) -match "COMPLETION ROADMAP")

$idx = 0; $orderOk = $true
for ($i = 1; $i -le 33; $i++) {
  $decl = ("PHASE {0:d2} " -f $i) + [char]0x2014 + " " + $names[$i - 1]
  $p = $pmRaw.IndexOf($decl, $idx)
  if ($p -lt 0) { $orderOk = $false; break }
  $idx = $p + 1
}
Check "33 phase declarations in order" $orderOk

Check "66 phase/board headings in TASK_BREAKDOWN" (([regex]::Matches($tbRaw, "### PHASE \d\d " + [char]0x2014)).Count -eq 66)
$states6 = @("BACKLOG", "TO DO", "IN PROGRESS", "CODE REVIEW", "TESTING", "DONE")
$badBoards = @()
foreach ($s in $states6) {
  $c = ([regex]::Matches($tbRaw, "(?m)^#### $([regex]::Escape($s))\s*$")).Count
  if ($c -ne 33) { $badBoards += "$s=$c" }
}
Check "every phase board has 6 state tables" ($badBoards.Count -eq 0) ($badBoards -join ", ")
Check "33 phase tracker rows" (([regex]::Matches($pmRaw, "(?m)^\| \d\d \| [^\r\n]+ \| (Planned|In progress|Completed) \|")).Count -eq 33)
Check "177 master rows" (([regex]::Matches($tbRaw, "(?m)^\| P\d\d-T\d\d \| \d\d \|")).Count -eq 177)
$ids = [regex]::Matches($tbRaw, "(?m)^\| (P\d\d-T\d\d) \| \d\d \|") | ForEach-Object { $_.Groups[1].Value }
Check "task IDs unique" (($ids | Select-Object -Unique).Count -eq 177)
Check "15 DONE tasks (Phase 01 completed)" (([regex]::Matches($tbRaw, "(?m)^\| P\d\d-T\d\d \| \d\d \|[^\r\n]+\| DONE \|")).Count -eq 15)
Check "162 BACKLOG tasks" (([regex]::Matches($tbRaw, "(?m)^\| P\d\d-T\d\d \| \d\d \|[^\r\n]+\| BACKLOG \|")).Count -eq 162)
Check "0 TO DO tasks" (([regex]::Matches($tbRaw, "(?m)^\| P\d\d-T\d\d \| \d\d \|[^\r\n]+\| TO DO \|")).Count -eq 0)
Check "0 IN PROGRESS tasks" (([regex]::Matches($tbRaw, "(?m)^\| P\d\d-T\d\d \| \d\d \|[^\r\n]+\| IN PROGRESS \|")).Count -eq 0)

$allowedStates = @("BACKLOG", "TO DO", "IN PROGRESS", "CODE REVIEW", "TESTING", "DONE")
$statuses = [regex]::Matches($tbRaw, "(?m)^\| P\d\d-T\d\d \| \d\d \|[^|]+\|[^|]+\|[^|]+\|[^|]+\| ([A-Z ]+) \|") | ForEach-Object { $_.Groups[1].Value.Trim() } | Select-Object -Unique
Check "master statuses within six official states" (($statuses | Where-Object { $allowedStates -notcontains $_ }).Count -eq 0) ($statuses -join ", ")
Check "six official states referenced" (($states6 | Where-Object { $pmRaw -notmatch [regex]::Escape($_) }).Count -eq 0)

$phaseStatuses = [regex]::Matches($tbRaw, "(?m)^\*\*Status:\*\* (Planned|In progress|Completed) ") | ForEach-Object { $_.Groups[1].Value } | Select-Object -Unique
Check "TB phase records use lifecycle vocabulary" (([regex]::Matches($tbRaw, "(?m)^\*\*Status:\*\* (Planned|In progress|Completed) ")).Count -eq 33 -and ($phaseStatuses | Where-Object { @("Planned", "In progress", "Completed") -notcontains $_ }).Count -eq 0) ($phaseStatuses -join ", ")
Check "TB phase 01 marked Completed" ($tbRaw -match [regex]::Escape("**Status:** Completed · **Current progress:** 100%"))
Check "PM phase tracker uses lifecycle vocabulary" (([regex]::Matches($pmRaw, "(?m)^\| \d\d \| [^\r\n]+ \| (Planned|In progress|Completed) \|")).Count -eq 33)

$refs = @("DEVELOPMENT_GUIDE.md", "CONTRIBUTING.md", "SECURITY.md", "SECURITY_STANDARDS.md", "CHANGELOG.md", "CODE_OF_CONDUCT.md", "PROJECT_MANAGEMENT.md", "LICENSE", "CODING_STANDARDS.md")
Check "PM references governance files" (($refs | Where-Object { $pmRaw -notmatch [regex]::Escape($_) }).Count -eq 0)

$sec = Get-Content "$root\SECURITY.md" -Raw -Encoding UTF8
Check "SECURITY -> SECURITY_STANDARDS" ($sec -match "SECURITY_STANDARDS.md")
Check "disclosure warning present" ($sec -match "DO NOT publicly disclose an unpatched vulnerability")
$con = Get-Content "$root\CONTRIBUTING.md" -Raw -Encoding UTF8
Check "CONTRIBUTING -> DEVELOPMENT_GUIDE" ($con -match "DEVELOPMENT_GUIDE.md")
Check "CONTRIBUTING six-state flow" ($con -match "BACKLOG" -and $con -match "CODE REVIEW" -and $con -match "TESTING")
Check "CHANGELOG phase status section" ((Get-Content "$root\CHANGELOG.md" -Raw -Encoding UTF8) -match "Phase completion status")
Check "CHANGELOG phase 01 completed" ((Get-Content "$root\CHANGELOG.md" -Raw -Encoding UTF8) -match "\| 01 \| Project Initiation \| Completed \|")

$secOk = $true
for ($i = 1; $i -le 18; $i++) { if ($pmRaw -notmatch "(?m)^## $i\. ") { $secOk = $false } }
Check "PM sections 1..18 present" $secOk
Check "session history append-only rule" ($pmRaw -match "Never delete or overwrite a past session")
Check "latest session recorded" ($pmRaw -match "### Session 04")

""
if ($ok) { "OVERALL: PASS"; exit 0 } else { "OVERALL: FAIL"; exit 1 }
