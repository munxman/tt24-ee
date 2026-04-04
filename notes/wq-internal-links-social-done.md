# WQ Task: Internal Cross-Links for Sotsiaalhoolekanne — DONE

**Completed:** 2026-04-05  
**Commits:** 6978c69 (parallel agent) + a0151ce (this agent)

## Files Modified

### 1. `sektorid/tervishoid.html`
- Added `<a href="sotsiaalhoolekanne.html" class="seotud-link">Sotsiaalhoolekanne</a>` to the "Seotud teemad" section (after haridus.html)
- Committed by parallel agent in 6978c69

### 2. `index.html`
- Sotsiaalhoolekanne was already added to the homepage sector grid by parallel agent (commit 6978c69) as the 3rd card
- No additional changes needed for index.html

### 3. `enesekontroll.html`
- Added `<a href="sektorid/sotsiaalhoolekanne.html">` card to the "Kasulikud artiklid" section after the existing 4 article links
- Card text: "Sotsiaalhoolekande nõuded — Bioloogilised riskid, psühhosotsiaalne koormus ja hooldustöö ergonoomika"
- Committed in a0151ce

### 4. `sektorid/sotsiaalhoolekanne.html` (outbound links already present)
- Already has `<a href="tervishoid.html">` and `<a href="haridus.html">` in the "Seotud teemad" section — no changes needed

## Links Added Summary

| From | To | Location |
|---|---|---|
| tervishoid.html | sotsiaalhoolekanne.html | "Seotud teemad" section |
| index.html | sotsiaalhoolekanne.html | Sector grid (done by parallel agent) |
| enesekontroll.html | sotsiaalhoolekanne.html | "Kasulikud artiklid" section |
| sotsiaalhoolekanne.html | tervishoid.html | Already existed |
| sotsiaalhoolekanne.html | haridus.html | Already existed |

## Issues / Notes

- A parallel agent (wq-homepage-sector-link) had already handled index.html + tervishoid.html before this agent ran — no conflicts, just avoided duplicate work
- sotsiaalhoolekanne.html already had outbound links to tervishoid.html and haridus.html — task pre-satisfied
- All changes committed and pushed to origin/main successfully
