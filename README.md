# Deforestation-free Soy Dashboard

## Overview

This Streamlit application provides an interactive dashboard for visualizing and analyzing deforestation-free soy data. Users can explore the distribution of soy production across Brazilian states, analyze deforestation metrics, and view summary statistics. The application uses Folium for interactive mapping and Streamlit for the user interface.

## Features

- Interactive choropleth map displaying soy production data for Brazilian states.
- Filtering options for selecting specific years and states for analysis.
- Summary statistics sidebar displaying total soy production, carbon on soil, legal reserve surplus, and active CARs (Cadastro Ambiental Rural).

## Requirements

- Python 3.x
- Streamlit
- Pandas
- Folium
- Streamlit-Folium

## Installation

1. Clone the repository to your local machine:
git clone https://github.com/sacramento-unb/dash_soja_brasil.git

2. Install the required dependencies:
pip install -r requirements.txt

3. Run the Streamlit application using the following command:
streamlit run app.py

## Configuration

- Adjust file paths in Home.py if necessary (DATA_FILE_PATH, GEO_DATA, IMAGE_DATA).
- Customize the application title and subtitle in app.py by modifying APP_TITLE and APP_SUB_TITLE.
- Contributing
- Contributions are welcome! If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request.

## License
- This project is licensed under the MIT License - see the LICENSE file for details.
