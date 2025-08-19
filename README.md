<div align="center">
  <img src="https://img.shields.io/badge/Python-3.6%2B-blue?logo=python" alt="Python Version" />
  <img src="https://img.shields.io/badge/Folium-Map-green?logo=leaflet" alt="Folium" />
  <img src="https://img.shields.io/badge/Pandas-Data-yellow?logo=pandas" alt="Pandas" />
</div>

# 🌋 Interactive Volcano Map

**Visualize volcano locations and world population interactively using Python, Folium, and Pandas.**

---

## 🚀 Features

✅ Volcanoes plotted from CSV, color-coded by elevation<br>
✅ World population overlay from GeoJSON, colored by population<br>
✅ Interactive map with layer controls and popups<br>

---

## 🛠️ Requirements

- Python 3.6+
- pandas
- folium

---

## ⚡ Quick Start

```bash
# 1. Clone the repository (if not already)
git clone https://github.com/MNATorres/interactive-volcano-map.git
cd interactive-volcano-map

# 2. Install dependencies
pip install pandas folium

# 3. Add data files
#   - Place Volcanoes.txt (CSV: LAT, LON, ELEV) in the folder
#   - Place world.json (GeoJSON with population data) in the folder

# 4. Run the script
python index.py

# 5. Open Map1.html in your browser
```

---

## 📁 File Overview

| File           | Description                                      |
|----------------|--------------------------------------------------|
| `index.py`     | Main script to generate the map                  |
| `Volcanoes.txt`| CSV file with volcano data (not included)        |
| `world.json`   | GeoJSON file with world population (not included)|
| `Map1.html`    | Output HTML file with the interactive map        |

---

## 💡 Notes

- You need an internet connection to load map tiles.
- To change the map style, modify the `tiles` parameter in `folium.Map`.
- You can customize marker colors, popups, and overlays as you wish.

---

<div align="center">
  <b>Feel free to modify or extend the code for your own data visualizations!</b>
</div>
