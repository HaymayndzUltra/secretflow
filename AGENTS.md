# AGENTS Quick Guide: Mabilisang Pag-intindi sa System via README.md

## Objective
Makuha ang high-level na larawan ng buong system sa loob ng ilang minuto sa pamamagitan ng pag-scan ng lahat ng `README.md` at mga pangunahing protocol.

## TL;DR Flow (5–15 minutes)
1) Basahin muna ang root `README.md` upang makuha ang core concept at architecture ng framework.
2) Basahin ang `.cursor/dev-workflow/README.md` para sa 5-protocol lifecycle at unified review.
3) Basahin ang `workflow1/README.md` para sa phase capsules (2–6), evidence flow, at scripts.
4) I-skim ang bawat phase README/protocol sa `workflow1/codex-phase*/` at ang `review-protocols/` kung kailangan ng quality deep-dive.
5) Optional: Sulyapan ang automation scripts sa bawat phase (`scripts/`) para makita ang tunay na outputs/evidence.

## One-Click Listing (All README.md)
Gamitin ito para makita lahat ng READMEs at mabilis na mag-navigate:
```bash
find . -type f -iname "README.md" | sort
```

Pro tip: Para makita rin ang mga pangunahing protocol files:
```bash
printf "\n# Protocols in .cursor/dev-workflow\n" && ls -1 ./.cursor/dev-workflow/*.md 2>/dev/null
printf "\n# Phase protocols in workflow1\n" && find ./workflow1 -maxdepth 2 -type f -name "protocol.md" | sort
```

## Recommended Reading Order (and What to Look For)
- `README.md` (root): Why the framework exists, 2 core components, high-level workflow.
- `.cursor/dev-workflow/README.md`: 5-protocol lifecycle, session strategy, unified quality audit entrypoint.
- `.cursor/dev-workflow/0-5*.md`: Roles per step, exact prompts/commands, outputs per protocol.
- `workflow1/README.md`: Phase capsules (2–6), evidence manifests/logs, script usage.
- `workflow1/codex-phase3-quality-rails/protocol.md`: Quality rails objectives, gates, required artefacts, automation.
- Other `workflow1/codex-phase*/protocol.md`: Inputs → Procedure → Exit Criteria → Evidence logging.

## Rapid Comprehension Checklist
- Governance vs. Operator split malinaw (`/rules` vs. `/dev-workflow`).
- Lifecycle: 0 Bootstrap → 1 PRD → 2 Plan → 3 Implement → 4 Audit → 5 Retro → 6 Ops.
- Evidence trail: `evidence/phaseX/manifest.json`, `run.log`, `validation.md` updates.
- Quality gates: security, performance, a11y, analytics, tests, code review.
- Session hygiene: one parent task per session; audit + retro in the same session.

## Verify with Commands (Spot-Check)
```bash
# 1) Core docs
sed -n '1,140p' README.md | sed -n '1,60p'
sed -n '1,140p' ./.cursor/dev-workflow/README.md | sed -n '1,140p'
sed -n '1,120p' ./workflow1/README.md | sed -n '1,120p'

# 2) Quality rails protocol (key requirements)
sed -n '1,120p' ./workflow1/codex-phase3-quality-rails/protocol.md

# 3) Evidence skeletons exist
find ./workflow1/evidence -maxdepth 2 -type f -name "manifest.json" -o -name "validation.md" | sort
```

## When Deeper Context Is Needed
- Buksan ang anumang `protocol.md` ng phase na relevant at sundan ang "Inputs → Procedure → Exit Criteria → Evidence" pattern.
- Tingnan ang `scripts/` sa loob ng phase para sa actual file outputs at manifest updates.
- Para sa reviews, gamitin ang `.cursor/dev-workflow/4-quality-audit.md` bilang central orchestrator.

## Outputs na Dapat Naiintindihan Mo Pagkatapos
- Paano umiikot ang buong lifecycle at saan nagaganap ang approvals/gates.
- Saan sinusulat ang ebidensiya (manifests, logs, validations) at paano ito nava-validate.
- Paano tumatakbo ang quality rails at ano ang minimum na artefacts.
- Paano pinapamahalaan ang sessions para sa predictable na progress.

—
Tip: Kung nag-o-onboard ng bagong contributor, ipabasa ang sections na ito sa pagkakasunod-sunod, tapos ipagawa ang spot-check commands para ma-validate ang understanding agad.