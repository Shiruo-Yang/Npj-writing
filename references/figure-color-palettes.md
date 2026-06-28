# Figure color palettes

Use this reference when a user asks for manuscript figures, graphical abstracts, schematic panels, workflow diagrams, palettes, color matching, or plot styling.

Machine-readable source:

`assets/color-palettes/npj_figure_palettes.json`

The palettes were read from the user-provided figure-style images on 2026-06-28. Hex values follow the printed color labels where available. For images that only showed RGB labels, RGB values were converted to hex.

## Selection rule

- Use `r2omics_ggstyle` palettes for statistical plots: scatter, violin, stacked bars, cluster annotations and candidate-family plots.
- Use `applied_energy_schematic` palettes for dense workflow diagrams, engineering schematics, optimization pipelines and method overview figures.
- Use `origin_framework_templates` palettes for soft framework diagrams, graphical abstracts and low-saturation conceptual panels.
- For final NPJ figures, check contrast, colorblind accessibility and grayscale legibility before submission.
- Do not use red-green opposition as the only semantic distinction.
- If a palette has more colors than needed, take colors in listed order unless the first color is white or a very pale background.

## Palette classes

### R2Omics ggstyle categorical palettes

Use these for data-heavy plots where each color maps to a group.

| ID | Chinese name | Colors | Suggested use |
|---|---:|---:|---|
| `r2omics_blue_sky_green_land` | 蓝天绿地 | 8 | balanced blue-red-neutral categorical plots |
| `r2omics_aqua_flower_shadow` | 水色花影 | 8 | teal/purple cluster figures |
| `r2omics_summer_beach` | 夏日海滩 | 8 | warm-to-cool candidate-family panels |
| `r2omics_fresh_holiday` | 清新假日 | 8 | light mixed-category figures |
| `r2omics_pastel_girl` | 粉彩少女 | 8 | soft supplemental panels |
| `r2omics_ocean_breeze` | 海洋清风 | 8 | warm-cool workflow plots |
| `r2omics_soft_green_forest` | 柔绿森林 | 8 | nature/green mechanism-family maps |

### Applied Energy schematic palettes

Use these for flowcharts and process diagrams. They are stronger and more technical than the pastel palettes.

| ID | Colors | Suggested use |
|---|---:|---|
| `applied_energy_hydrogen_pipeline` | 8 | two-lane orange/blue engineering workflows |
| `applied_energy_energy_system` | 6 | optimization and system-configuration panels |
| `applied_energy_virtual_power_plant` | 12 | dense network and market-flow diagrams |
| `applied_energy_low_carbon_technology` | 10 | scenario and policy model schematics |
| `applied_energy_wind_forecasting` | 12 | ML training/validation/testing pipelines |
| `applied_energy_physical_optimization` | 6 | optimization/Pareto/TOPSIS workflows |
| `applied_energy_market_rl` | 8 | reinforcement-learning and market mechanisms |
| `applied_energy_solar_route_main` | 12 | GIS and factor-screening frameworks |
| `applied_energy_solar_route_font` | 5 | emphasis text colors |
| `applied_energy_solar_route_arrow` | 4 | arrows and flow connectors |

### Origin framework template palettes

Use these for manuscript-friendly low-saturation figure backgrounds and boxed graphical abstracts.

| ID | Source | Colors | Suggested use |
|---|---|---:|---|
| `origin_sustainable_cities_pastel` | Sustainable Cities and Society | 7 | soft framework layouts |
| `origin_arxiv_agentswift_pastel` | arXiv preprint-style framework | 7 | AI/agent method schematics |
| `origin_ecological_informatics_pastel` | Ecological Informatics | 7 | materials-screening workflow panels |
| `origin_applied_energy_hvac_pastel` | Applied Energy HVAC | 7 | control-system and energy workflow panels |

## Python usage

```python
import json
from pathlib import Path

palette_file = Path(r"C:/Users/HP/.codex/skills/npj-writing/assets/color-palettes/npj_figure_palettes.json")
data = json.loads(palette_file.read_text(encoding="utf-8"))
palettes = {p["id"]: p["hex"] for p in data["palettes"]}

colors = palettes["r2omics_blue_sky_green_land"]
```

For Matplotlib:

```python
import matplotlib.pyplot as plt

plt.rcParams["axes.prop_cycle"] = plt.cycler(color=colors)
```

For Seaborn:

```python
import seaborn as sns

sns.set_palette(colors)
```

## R usage

```r
library(jsonlite)

palette_file <- "C:/Users/HP/.codex/skills/npj-writing/assets/color-palettes/npj_figure_palettes.json"
data <- fromJSON(palette_file)
palettes <- setNames(data$palettes$hex, data$palettes$id)
colors <- palettes[["r2omics_blue_sky_green_land"]][[1]]
```

For ggplot2:

```r
scale_color_manual(values = colors)
scale_fill_manual(values = colors)
```

## LaTeX usage

Use the hex values with `xcolor`:

```tex
\usepackage{xcolor}
\definecolor{npjBlueSky1}{HTML}{377EB8}
\definecolor{npjBlueSky2}{HTML}{B23648}
```

## Project preference

For the current 2PI manuscript:

- Use `r2omics_blue_sky_green_land`, `r2omics_fresh_holiday`, or `r2omics_ocean_breeze` for quantitative result figures.
- Use `origin_ecological_informatics_pastel` for graphical abstract or workflow panels.
- Use `applied_energy_wind_forecasting` or `applied_energy_solar_route_main` if the figure is a dense multi-step computational workflow.
- Use black/gray text with pale fill colors for Methods schematics.
- Keep highly saturated reds/oranges for warnings, exclusions, failed AD/OOD cases, or high-risk candidates.
