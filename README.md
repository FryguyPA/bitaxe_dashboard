# BitAxe Dashboard

A single-file browser dashboard for monitoring one or more [BitAxe](https://github.com/skot/bitaxe) miners running AxeOS. No cloud, no account — everything runs locally and all configuration is stored in your browser's `localStorage`.

![Dashboard preview showing miner cards, fleet hashrate chart, and stats bar](https://img.shields.io/badge/status-active-brightgreen)

## Features

- **Multi-miner monitoring** — add as many miners as you like by IP address or hostname
- **Live stats per miner** — hashrate (current, 1m, 10m, 1h), temperature, power, efficiency (J/TH), fan RPM, shares, best difficulty, pool info, uptime, and firmware version
- **Fleet summary bar** — combined hashrate at 1m / 10m / 1h averages, total power, avg efficiency, avg temp
- **History charts** — data accumulates while the page is open and persists across refreshes:
  - Fleet hashrate area chart with 2-hour moving average
  - Best session difficulty (bar chart, log scale)
  - Per-miner: hashrate, temperature, power draw, efficiency, cumulative shares
- **Sparklines** — inline mini-chart per miner card showing recent 10m hashrate trend
- **Customizable layout** — drag cards to reorder, pick a custom color per miner, choose 1–4 columns or auto, switch between normal and compact card size
- **Persistent configuration** — miner list, order, colors, layout, and refresh interval all saved in `localStorage`
- **Auto-refresh** — configurable interval (15s, 30s, 1m, 2m, 5m, or manual)
- **CORS-safe proxy** — included `server.py` routes API calls server-side to avoid browser CORS restrictions

## Quick Start

### Option A — Open directly (may work if your AxeOS version sends permissive CORS headers)

```
open dashboard.html
```

If you see a yellow CORS warning, use Option B instead.

### Option B — Serve via the included proxy server (recommended)

Requires Python 3 — no extra packages needed.

```bash
python3 server.py
```

Then open **http://localhost:8080/dashboard.html** in your browser.

To use a different port:

```bash
python3 server.py 9000
```

## Adding Miners

1. Enter an IP address (e.g. `192.168.1.50`) or hostname (e.g. `bitaxe.local`) in the **Add Miner** field
2. Press **Enter** or click **Add**
3. The miner is polled immediately and saved for future visits

## Customization

Click **Customize** in the top-right to enter customize mode:

| Control | What it does |
|---|---|
| Drag card header | Reorder miners — new order is saved automatically |
| Color swatch (card header) | Open a color picker to repaint that miner's accent across the card, sparkline, and charts |
| Columns | Set 1, 2, 3, 4, or Auto columns in the card grid |
| Card size | Normal (full detail) or Compact (denser layout) |
| Reset Colors | Revert all miners to the default color palette |

## Files

| File | Purpose |
|---|---|
| `dashboard.html` | The entire dashboard — HTML, CSS, and JavaScript in one file |
| `server.py` | Lightweight Python proxy server; also serves `dashboard.html` as a static file |

## Data & Privacy

All data stays on your machine. Miner IP addresses, history, and preferences are stored in your browser's `localStorage` and never transmitted anywhere other than directly to your miners.

History accumulates up to 500 data points per miner. When localStorage approaches its limit the oldest half of history is automatically trimmed.

## API

The dashboard uses the AxeOS REST API at `/api/system/info` on each miner. Full API documentation is available at [osmu.wiki/bitaxe/api](https://osmu.wiki/bitaxe/api/).

## Requirements

- A BitAxe miner running AxeOS (any recent version)
- A modern browser (Chrome, Firefox, Safari, Edge)
- Python 3 (standard library only) if using `server.py`

## License

See [LICENSE](LICENSE).
