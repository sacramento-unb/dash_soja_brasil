import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium


APP_TITLE = 'Deforestation-free Soy'
APP_SUB_TITLE = 'Report from 2020-2022 * Only soy properties considered'
DATA_FILE_PATH = '\data\relatorio_soja_2020_2024-02-09.csv'
GEO_DATA = '\data\BR_UF_2022.geojson'
IMAGE_DATA = '\dash_soja_brasil\data\color_ramp.jpg'

def load_data(file_path):
    try:
        df = pd.read_csv(file_path, sep=',', encoding='utf-8')
        df[["soja_area_nao_desmat"]] = df[["soja_area_nao_desmat"]].apply(pd.to_numeric)
        return df
    except FileNotFoundError:
        st.error(f"File not found at: {file_path}")
        return None
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None
    

@st.cache_resource(experimental_allow_widgets=True)
def display_map(mdf, estado, year):
    map = folium.Map(location=[-15,-54], zoom_start=4, tiles='CartoDB positron')


    choropleth = folium.Choropleth(
        geo_data=GEO_DATA,
        data=mdf,
        columns=('sigla_uf','soja_area_nao_desmat'),
        key_on='feature.properties.sigla_uf',
        highlight=True,
        prefer_canvas=True
    )

    choropleth.geojson.add_to(map)


    for feature in choropleth.geojson.data['features']:
        state = feature['properties']['sigla_uf']

        formatted_number = '{:,.2f}'.format(mdf.loc[state][1] if state in mdf.index else 0)
        formatted_number = formatted_number.replace('.', '|').replace(',', '.').replace('|', ',')
        feature['properties']['soja_area_nao_desmat'] = 'Soy: ' + formatted_number + ' (ha)'

        formatted_carbon = '{:,.2f}'.format(round(mdf.loc[state][2]) if state in mdf.index else 0)
        formatted_carbon = formatted_carbon.replace('.', '|').replace(',', '.').replace('|', ',')
        feature['properties']['tco2eq'] = 'Carbon on soil: ' + formatted_carbon + ' (ton)'

        formatted_lr = '{:,.2f}'.format(round(mdf.loc[state][3]) if state in mdf.index else 0)
        formatted_lr = formatted_lr.replace('.', '|').replace(',', '.').replace('|', ',')
        feature['properties']['lr_surplus'] = 'Legal reserve surplus: ' + formatted_lr + ' (ha)'

        formatted_CARs = '{:,.0f}'.format(round(mdf.loc[state][4]) if state in mdf.index else 0)
        formatted_CARs = formatted_CARs.replace('.', '|').replace(',', '.').replace('|', ',')
        feature['properties']['qtd_cars'] = 'Active CARs: ' + formatted_CARs

    choropleth.geojson.add_child(
        folium.features.GeoJsonTooltip(['sigla_uf','soja_area_nao_desmat','tco2eq','lr_surplus','qtd_cars'], labels=False)
    )
    
    st_folium(map, width=950, height=500)

def main():
    st.set_page_config(page_title=APP_TITLE, layout='wide')
    st.title(APP_TITLE) 
    st.subheader(APP_SUB_TITLE)

    # Load data
    df = load_data(DATA_FILE_PATH)
    if df is None:
        return
    
    # FILTERS
    year_list = [''] + sorted(df['year'].unique())  # Add a blank option for year
    years_selected = st.sidebar.multiselect('Year', year_list)  # Use multiselect for year selection
    
    estado_list = [''] + sorted(df['sigla_uf'].unique())  # Add a blank option for state
    estados_selected = st.sidebar.multiselect('State', estado_list)  # Use multiselect for state selection
    
    # Filter data based on selected filters
    df_filtered = df
    if years_selected:
        df_filtered = df_filtered[df_filtered['year'].isin(years_selected)]
    if estados_selected:
        df_filtered = df_filtered[df_filtered['sigla_uf'].isin(estados_selected)]
    
    # Display the map with filtered data
    display_map(df_filtered, estados_selected, years_selected)
    st.image(IMAGE_DATA,use_column_width=True,output_format='JPEG')
    st.write(df_filtered)

    # Calculate and display metrics
    if not df_filtered.empty:
        
        total_soy = df_filtered['soja_area_nao_desmat'].sum()
        total_carbon = df_filtered['tco2eq'].sum()
        total_lr_surplus = df_filtered['lr_surplus'].sum()
        total_cars = df_filtered['qtd_cars'].sum()
        st.sidebar.write("## Summary statistics")

        st.sidebar.write("Soy", f"{total_soy:,.2f}{' (ha)'}".replace(',', '|').replace('.', ',').replace('|', '.'))
        st.sidebar.write("Carbon", f"{total_carbon:,.2f}{' ton'}".replace(',', '|').replace('.', ',').replace('|', '.'))
        st.sidebar.write("Legal reserve Surplus", f"{total_lr_surplus:,.2f}{' (ha)'}".replace(',', '|').replace('.', ',').replace('|', '.'))
        st.sidebar.write("Active CAR's", f"{total_cars:,.0f}".replace(',', '|').replace('.', ',').replace('|', '.'))

if __name__ == "__main__":
    main()