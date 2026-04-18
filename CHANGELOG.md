# Changelog

All notable changes to BitAxe Dashboard are documented here.

## [Unreleased]

### Added
- Drag-and-drop card reordering via SortableJS
- Per-miner custom color picker (color swatch in card header)
- Column layout selector (1 / 2 / 3 / 4 / Auto) in customize toolbar
- Compact card size mode (denser stats grid, no sparkline row)
- "Customize" mode toggle — reveals drag handles and color controls
- "Reset Colors" button to revert all miners to the default palette
- Layout, card size, and miner colors persist across page refreshes via `localStorage`
- Fleet hashrate area chart with 2-hour moving average (teal fill + green MA line)
- Best session difficulty bar chart on a logarithmic scale
- Per-miner history charts: hashrate (10m avg), temperature, power draw, efficiency (J/TH), cumulative shares accepted
- Inline sparkline per miner card showing recent 10m hashrate trend (min/max annotated)
- Fleet summary bar showing 1m, 10m, and 1h combined hashrate averages
- History persists across page refreshes (up to 500 points per miner); auto-trims when localStorage quota is approached
- `server.py` — zero-dependency Python proxy server that routes `/proxy/<ip>/api/...` requests server-side to bypass browser CORS restrictions; also serves `dashboard.html` as a static file
- CORS warning banner with fix instructions when browser blocks direct miner requests
- Difficulty string parser supporting K / M / G / T / P suffixes for chart rendering

### Changed
- Summary bar expanded from 5 items to 7 (added 1m and 1h hashrate fleet totals)
- Per-miner colors now derived from the miner object's `color` field if set, falling back to the default PALETTE

## [0.1.0] — 2026-04-18

### Added
- Initial single-file dashboard (`dashboard.html`)
- Add and remove miners by IP address or hostname
- Miner list persists across refreshes via `localStorage`
- Auto-refresh with configurable interval (15s, 30s, 1m, 2m, 5m, manual)
- Countdown timer in the header
- Per-miner card displaying:
  - Live hashrate + 1m / 10m / 1h averages
  - Temperature with color coding (cool / warm / hot thresholds)
  - Power draw and efficiency (J/TH)
  - Fan RPM / speed (auto or manual)
  - ASIC model, frequency, and core voltage
  - Best difficulty (all-time and session)
  - Shares accepted / rejected with rejection rate
  - Pool URL, port, and username; fallback stratum indicator
  - Uptime, WiFi RSSI, firmware version
  - Block found indicator
- Fleet summary bar: miners online, total 10m hashrate, total power, avg efficiency, avg temperature
- Status indicators: online (green), loading (pulsing yellow), offline (red)
- Stale data display when a miner goes offline (last known values shown with stale badge)
- "Open AxeOS" button per card to launch the miner's web UI
- "Remove" button per card
- CORS-aware fetch: automatically routes through `/proxy/` when served from localhost
