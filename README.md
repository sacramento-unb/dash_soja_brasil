# Deforestation-free soy dashboard

## Overview

This Streamlit application visualizes bundled soy and environmental indicators by
Brazilian state. Users can filter years and states, inspect a Folium choropleth
and view summary statistics.

## Features

- Interactive choropleth map displaying soy production data for Brazilian states.
- Filtering options for selecting specific years and states for analysis.
- Summary statistics sidebar displaying total soy production, carbon on soil, legal reserve surplus, and active CARs (Cadastro Ambiental Rural).

## Current status and limits

This is a legacy study dashboard, not a validated production indicator. The
repository includes multiple CSV/XLSX datasets and a 32 MB workbook, but does
not document their source, update date, personal-data review or redistribution
terms. Do not add it to a public portfolio or redistribute the data until those
rights are confirmed.

The code expects `data/relatorio_soja_2024-02-27.csv` and
`data/BR_UF_2022.geojson`. The old README referenced `app.py`; the actual entry
point is `Home.py`. No automated tests are included and the application was not
run during this documentation audit.

## Requirements

- Python 3.x
- Streamlit
- Pandas
- Folium
- Streamlit-Folium

## Installation

1. Install the required dependencies:
pip install -r requirements.txt

2. Run the Streamlit application using:
streamlit run Home.py

## Configuration

- Adjust file paths in `Home.py` if necessary (`DATA_FILE_PATH`, `GEO_DATA`,
  `IMAGE_DATA`).
- Customize `APP_TITLE` and `APP_SUB_TITLE` in `Home.py`.
- Contributing
- Contributions are welcome! If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request.

## License

No repository-level license file was present in the audited tree. The data
license and the code's intended terms therefore require an explicit owner
decision before redistribution.
