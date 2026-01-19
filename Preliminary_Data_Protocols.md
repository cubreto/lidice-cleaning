# Preliminary Data Collection Protocols
## Fast-Track Experiments for SBIR Competitiveness

**Timeline**: 8-10 weeks to generate 3 compelling figures
**Budget Estimate**: $8,000-12,000 (reagents + analysis)

---

## EXPERIMENT 1: Orange EV Isolation and Characterization (Week 1-2)

### Objective
Demonstrate reproducible isolation of intact, bioactive PDEVs from sweet orange juice.

### Materials Needed
- Fresh sweet orange juice (organic, commercial or fresh-squeezed) - 2L
- Ultracentrifuge (or access to core facility)
- Size exclusion chromatography columns (qEV, Izon Science) - $500
- TEM grids and access to electron microscope
- Western blot supplies (antibodies: anti-CD63, anti-TSG101) - $300
- HPLC for flavonoid analysis (or LC-MS service)

### Protocol

#### Step 1: Juice Preparation (Day 1, ~2 hours)
```
1. Start with 2L fresh orange juice (room temp)
2. Centrifuge at 500×g for 10 min (remove pulp)
3. Transfer supernatant to new tubes
4. Centrifuge at 2,000×g for 20 min (remove cellular debris)
5. Transfer supernatant to new tubes
6. Centrifuge at 10,000×g for 30 min (remove large vesicles/apoptotic bodies)
7. Collect supernatant (~1.8L) → this contains EVs
```

#### Step 2: EV Isolation (Day 1-2, ~8 hours total)
**Method A: Ultracentrifugation** (gold standard, time-intensive)
```
1. Transfer supernatant to ultracentrifuge tubes
2. Ultracentrifuge at 100,000×g for 90 min at 4°C
3. Carefully discard supernatant
4. Resuspend pellet in 500 μL PBS (pipette gently, do not vortex)
5. Pool pellets from multiple tubes
6. Final wash: 100,000×g for 90 min at 4°C
7. Resuspend in 200-500 μL PBS
8. Store at 4°C (use within 48h) or -80°C with 10% DMSO
```

**Method B: Size Exclusion Chromatography** (faster, better integrity)
```
1. Concentrate 10,000×g supernatant using 100 kDa MWCO filter
   - Spin at 4,000×g until volume reduces to ~10 mL
2. Load onto qEV column (70 nm separation size)
3. Collect fractions 7-9 (EV peak, ~3 mL total)
4. Concentrate to 500 μL if needed
5. Store at 4°C or -80°C
```

**Recommendation**: Use Method B for preliminary data (faster, better quality)

#### Step 3: Characterization (Day 3-5)

**A. Protein Quantification**
- BCA assay: quantify total protein
- Expected: 50-200 μg protein/mL orange juice
- **Goal**: ≥5 mg total protein for experiments

**B. Particle Count and Size (NTA or DLS)**
- Dilute EVs 1:100 to 1:1000 in filtered PBS
- Run nanoparticle tracking analysis (NTA) or dynamic light scattering (DLS)
- **Target metrics**:
  - Concentration: 10^9 to 10^11 particles/mL
  - Size: Peak at 80-150 nm
  - PDI (polydispersity index): <0.3 (uniform population)

**C. Transmission Electron Microscopy**
```
1. Dilute EVs 1:10 in PBS
2. Load 5 μL onto formvar/carbon-coated TEM grid
3. Incubate 5 min, wick away liquid
4. Negative stain with 2% uranyl acetate (1 min)
5. Image at 80-120 kV
```
- **Look for**: Cup-shaped vesicles, 50-200 nm, intact membranes

**D. Western Blot (EV Markers)**
```
Samples:
- Lane 1: Orange EVs (10 μg protein)
- Lane 2: Orange juice (pre-isolation, 10 μg protein)
- Lane 3: Positive control (mammalian EVs if available)

Antibodies:
- Primary: anti-CD63 (1:1000), anti-TSG101 (1:500)
- Secondary: HRP-conjugated (1:5000)

Expected: Strong bands in EVs, weak/absent in crude juice
```

**E. Flavonoid Analysis (HPLC or LC-MS)**
```
1. Extract EVs: add 4 volumes methanol, vortex, centrifuge
2. Inject supernatant onto C18 column
3. Gradient: water/acetonitrile with 0.1% formic acid
4. Detect at 280 nm (hesperidin) and 360 nm (naringenin)

Quantify against standards:
- Hesperidin: expect 10-50 μg/mg EV protein
- Naringenin: expect 5-20 μg/mg EV protein
```

### Data Analysis and Figure Preparation

**Figure 1: Orange EV Characterization (4-panel)**

```
Panel A: TEM images (scale bar 100 nm)
         - Show 3-5 representative EVs with intact cup-shaped morphology

Panel B: Size distribution (NTA or DLS histogram)
         - X-axis: Diameter (nm), Y-axis: Particle count
         - Add mean ± SD annotation (e.g., "Mean: 120 ± 35 nm")

Panel C: Western blot for EV markers
         - Show CD63 and TSG101 enrichment in EV fraction vs crude juice
         - Include densitometry quantification bar graph

Panel D: HPLC flavonoid profile
         - Chromatogram showing hesperidin and naringenin peaks
         - Bar graph: flavonoid concentration (μg/mg protein)
```

**Statistical Target**: Run 3 independent EV isolations, report mean ± SD for all metrics

**Expected Result**: "Orange EVs isolated by SEC exhibit typical exosome-like morphology (cup-shaped, 120±35 nm), express canonical markers (CD63, TSG101), and retain endogenous flavonoids (hesperidin: 28±6 μg/mg protein)."

---

## EXPERIMENT 2: CsA Loading Optimization (Week 3-4)

### Objective
Develop "Gentle Fusion" protocol achieving ≥60% encapsulation efficiency with preserved EV integrity.

### Materials Needed
- Cyclosporine A (Sigma C3662) - 25 mg (~$200)
- Ethanol, DMSO (analytical grade)
- Size exclusion chromatography columns (qEV) - $500
- LC-MS/MS service for CsA quantification (or HPLC-UV) - $500/sample
- Water bath or heat block (37°C capability)

### Protocol: "Gentle Fusion" Loading

#### Step 1: CsA Stock Preparation
```
1. Dissolve 10 mg CsA in 1 mL ethanol (10 mg/mL stock)
2. Store at -20°C, warm to RT before use
3. Vortex well before each use (CsA can precipitate)
```

#### Step 2: Pre-activation of EVs
```
1. Take freshly isolated orange EVs (~1 mg protein)
2. Dilute to 1 mg/mL protein in PBS (pH 7.4)
3. Incubate at 37°C for 15 min in heat block
   - This increases membrane fluidity
```

#### Step 3: CsA Loading
```
1. Calculate volumes for different CsA:EV ratios:
   - Low: 1:10 (w/w) → 100 μg CsA per 1 mg EV protein
   - Medium: 1:5 → 200 μg CsA per 1 mg EV protein
   - High: 1:2.5 → 400 μg CsA per 1 mg EV protein

2. Add CsA dropwise from ethanolic stock:
   - Add slowly over 1 min with gentle swirling
   - Final ethanol concentration: 2-5% (v/v)
   - Keep at 37°C

3. Incubate 30 min at 37°C with gentle rotation
   - Use rotator at ~10 rpm (avoid vigorous mixing)

4. Rapid cooling:
   - Transfer tube to ice bath for 5 min
   - This "locks" CsA into membrane

5. Optional sonication pulse:
   - 30 sec at 10% amplitude (probe sonicator)
   - OR 2 min in bath sonicator
```

#### Step 4: Removal of Free CsA
```
Method 1: Size Exclusion Chromatography (preferred)
1. Load CsA-EV mixture onto qEV column
2. Collect fractions 7-9 (contains EVs, excludes free CsA)
3. Concentrate using 100 kDa MWCO filter if needed

Method 2: Ultracentrifugation
1. Dilute to 10 mL in PBS
2. Ultracentrifuge 100,000×g for 90 min at 4°C
3. Wash pellet once more (repeat spin)
4. Resuspend in PBS
```

#### Step 5: Quantification

**Total CsA (Input)**
- Measure CsA added initially (known from stock)

**Encapsulated CsA (Output)**
```
1. Lyse EVs: add 0.1% Triton X-100, vortex
2. Extract: add 4 volumes methanol, vortex, spin 10,000×g
3. Analyze supernatant by LC-MS/MS or HPLC-UV
   - HPLC: C18 column, 210 nm detection
   - Retention time ~8-10 min (acetonitrile/water gradient)
```

**Encapsulation Efficiency Calculation**
```
EE% = (CsA in purified EVs / CsA added initially) × 100

Loading Capacity = (mass CsA in EVs / mass EV protein)
```

**Target**: EE% ≥60%, Loading capacity ≥50 μg CsA/mg protein

#### Step 6: Comparison to Standard Method

**Control: Sonication Method**
```
1. Mix EVs + CsA (same ratios as above)
2. Sonicate 5 min at 20% amplitude
3. Purify by SEC
4. Quantify as above
```

**Hypothesis**: Gentle Fusion yields higher EE% with better EV integrity

### Characterization of CsA-Loaded EVs

**A. Size and Morphology**
- NTA/DLS: expect slight size increase (~10-20 nm)
- TEM: check for aggregation or membrane rupture

**B. Zeta Potential**
- Empty EVs: typically -10 to -30 mV
- CsA-EVs: expect slight change (±5 mV)

**C. EV Marker Retention (Western Blot)**
- Compare CD63 levels in empty vs CsA-loaded EVs
- **Goal**: ≥80% marker retention (indicates preserved integrity)

**D. Flavonoid Retention (HPLC)**
- Measure hesperidin in CsA-loaded EVs
- **Goal**: ≥40% retention vs empty EVs

### Stability Testing (Run in parallel, Weeks 4-8)

**Protocol**:
```
1. Prepare 3 batches of PDEV-CsA (optimal ratio from above)
2. Aliquot into multiple tubes
3. Storage conditions:
   - 4°C (refrigerator)
   - -20°C (freezer)
   - -80°C (ultracold)

4. Test timepoints: Day 0, 7, 14, 28
5. At each timepoint:
   - Measure CsA content (LC-MS)
   - Check particle size (NTA/DLS)
   - Visual inspection (precipitation?)
```

**Acceptance criteria**: ≥90% CsA retained at 4°C for 28 days

### Data Analysis and Figure Preparation

**Figure 2: CsA Loading and Optimization (5-panel)**

```
Panel A: Schematic of Gentle Fusion protocol
         - Cartoon showing: pre-activation → CsA addition → cooling → purification

Panel B: Optimization of CsA:EV ratio
         - Bar graph: EE% at different ratios (1:10, 1:5, 1:2.5)
         - Show mean ± SD from 3 batches

Panel C: Comparison to sonication method
         - Side-by-side bars: EE%, Loading capacity, CD63 retention
         - Show Gentle Fusion superiority

Panel D: TEM comparison
         - Empty EVs vs CsA-loaded EVs (Gentle Fusion) vs Sonication
         - Annotate: intact morphology for Gentle Fusion

Panel E: Stability curve
         - Line graph: % CsA remaining over 28 days at 4°C, -20°C, -80°C
         - Error bars (SD), n=3 batches
```

**Expected Result**: "Gentle Fusion loading achieves 68±5% encapsulation efficiency at 1:5 CsA:EV ratio, outperforming sonication (42±8%, p<0.01) while preserving EV markers (92% CD63 retention) and flavonoids (51% hesperidin retention). CsA-loaded EVs retain 93±4% drug content at 4°C for 28 days."

---

## EXPERIMENT 3: In Vitro T-Cell Suppression (Week 5-8) [OPTIONAL BUT IMPACTFUL]

### Objective
Demonstrate that PDEV-CsA retains (or enhances) immunosuppressive activity vs. free CsA.

### Materials Needed
- Human peripheral blood (60 mL from healthy donor) or commercial PBMCs - $300
- Ficoll-Paque for PBMC isolation - $50
- T cell activation reagents: anti-CD3/CD28 beads (Dynabeads) - $400
- IL-2 ELISA kit (R&D Systems or eBioscience) - $350
- Cell culture supplies (RPMI, FBS, etc.) - $200

### Protocol

#### Step 1: PBMC Isolation (Day 1)
```
1. Dilute whole blood 1:1 with PBS
2. Layer over Ficoll-Paque (2:1 volume ratio)
3. Centrifuge 400×g for 30 min (no brake)
4. Collect buffy coat (PBMC layer)
5. Wash 2× with PBS
6. Count cells, adjust to 2×10^6 cells/mL in RPMI + 10% FBS
```

#### Step 2: T Cell Activation + Treatment (Day 1)
```
Plate setup (96-well, U-bottom):
- 200 μL per well (4×10^5 PBMCs)

Groups (n=6 wells each):
1. Unstimulated (negative control)
2. Stimulated (anti-CD3/CD28 beads, 1:1 bead:cell ratio)
3. Stimulated + Free CsA (50 ng/mL)
4. Stimulated + Free CsA (100 ng/mL)
5. Stimulated + PDEV-CsA (50 ng/mL CsA-equivalent)
6. Stimulated + PDEV-CsA (100 ng/mL CsA-equivalent)
7. Stimulated + Empty PDEVs (same protein dose as #5)

Add treatments simultaneously with activation
Incubate 48h at 37°C, 5% CO2
```

#### Step 3: Supernatant Collection (Day 3)
```
1. Centrifuge plate 400×g for 5 min
2. Collect 100 μL supernatant per well
3. Store at -80°C until ELISA
```

#### Step 4: IL-2 ELISA (Day 4-5)
```
Follow kit instructions
Measure in duplicate for each well
Calculate mean IL-2 concentration (pg/mL)
```

### Data Analysis

**Primary Endpoint**: % IL-2 suppression
```
Suppression % = [1 - (IL-2 treatment / IL-2 stimulated)] × 100
```

**Expected Results**:
- Free CsA (50 ng/mL): ~50% suppression
- PDEV-CsA (50 ng/mL): ≥50% suppression (ideally 60-70% if enhanced delivery)
- Empty PDEVs: <10% suppression (control for EV effects)

**Statistical Analysis**:
- One-way ANOVA followed by Tukey post-hoc
- Compare PDEV-CsA vs Free CsA at each dose

### Figure Preparation

**Figure 3: In Vitro Immunosuppressive Activity (2-panel)**

```
Panel A: IL-2 secretion (bar graph)
         - X-axis: Treatment groups
         - Y-axis: IL-2 concentration (pg/mL)
         - Show individual data points + mean ± SEM
         - Statistical annotations (*, p<0.05; **, p<0.01)

Panel B: Dose-response curves
         - X-axis: CsA concentration (log scale)
         - Y-axis: % IL-2 suppression
         - Two curves: Free CsA vs PDEV-CsA
         - Calculate IC50 for each (expect PDEV-CsA IC50 ≤ Free CsA)
```

**Expected Result**: "PDEV-CsA suppressed IL-2 secretion by 64±8% at 50 ng/mL, significantly greater than free CsA (48±6%, p=0.03). IC50 for PDEV-CsA was 38 ng/mL vs 62 ng/mL for free CsA, indicating enhanced potency. Empty PDEVs showed no suppression (6±4%), confirming drug-specific activity."

---

## Timeline and Resource Summary

### Gantt Chart

| Week | Experiment | Key Deliverable |
|------|-----------|----------------|
| 1-2  | EV isolation & characterization | Figure 1 (panels A-D) |
| 3-4  | CsA loading optimization | Figure 2 (panels A-D) |
| 4-8  | Stability testing (parallel) | Figure 2 (panel E) |
| 5-8  | T-cell assay (optional) | Figure 3 (panels A-B) |
| 9-10 | Data analysis, statistics | Complete figure set |

### Budget Breakdown

| Item | Cost |
|------|------|
| Orange juice + isolation reagents | $500 |
| qEV columns (×5) | $2,500 |
| Cyclosporine A | $200 |
| TEM imaging (core facility) | $500 |
| Western blot antibodies | $300 |
| HPLC/LC-MS service | $2,000 |
| T-cell assay reagents | $1,300 |
| Cell culture supplies | $500 |
| Miscellaneous (buffers, plasticware) | $500 |
| **TOTAL** | **$8,300** |

### Personnel Time

- **Week 1-4** (intensive): ~30 hours/week lab work
- **Week 5-8** (maintenance): ~15 hours/week
- **Week 9-10** (analysis): ~20 hours/week

---

## Tips for Success

### Critical Success Factors

1. **EV Quality**: Fresh juice yields better EVs. If using commercial juice, test multiple brands.

2. **CsA Handling**: Extremely hydrophobic—always dissolve in ethanol/DMSO first, never add directly to aqueous buffer.

3. **Reproducibility**: Run each experiment in triplicate (3 independent EV preps, not just technical replicates).

4. **Controls**: Always include empty PDEVs to control for EV effects independent of CsA.

5. **Documentation**: Take photos of everything (TEM grids, pellets, gels) for supplementary figures.

### Common Pitfalls to Avoid

❌ **Low EV yield**: Use fresh juice, optimize centrifugation times, consider using SEC instead of UC.

❌ **CsA precipitation**: Keep ethanol concentration ≥2% during loading; work quickly; maintain 37°C.

❌ **Variable T-cell responses**: Use same donor for all replicates; activate immediately after isolation; check bead:cell ratio.

❌ **Poor stability**: Add trehalose (5%) before storage; avoid freeze-thaw cycles; aliquot immediately.

### Quick Troubleshooting Guide

| Problem | Solution |
|---------|----------|
| EVs aggregate after CsA loading | Reduce CsA:EV ratio; add brief sonication pulse |
| Low encapsulation efficiency | Increase incubation time to 45 min; try 42°C instead of 37°C |
| Flavonoids lost | Reduce ethanol %; skip sonication step; use lower temp |
| High variability in T-cell assay | Pool PBMCs from 2-3 donors; pre-rest cells 4h before activation |

---

## Next Steps After Data Collection

Once you have these 3 figures:

✅ **Write** preliminary data section (2-3 pages)
✅ **File** provisional patent with data as supporting evidence
✅ **Submit** SBIR application (data makes you highly competitive)
✅ **Present** at conferences to build collaborations
✅ **Publish** as brief communication or letters journal (establish priority)

**You will be ready to compete for $500K Phase I funding with this dataset.**
