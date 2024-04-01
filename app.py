import altair as alt
import pandas as pd
import seaborn as sns
import streamlit as st
import time 

st.title("Palmer's Penguins")
st.markdown("Use this Streamlit app to make your own scatterplot about penguins!")
selected_x_var = st.selectbox(
"What do you want the x variable to be?",["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"],)
selected_y_var = st.selectbox(
"What about the y?", ["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"],)
penguin_file = st.file_uploader('Select Your Local Penguins CSV')

@st.cache_data()
def load_file(penguin_file):
    time.sleep(5)
    if penguin_file is not None:
        penguins_df = pd.read_csv(penguin_file)
    else:
        penguins_df = pd.read_csv('penguins.csv')
    return(penguins_df)

penguins_df = load_file(penguin_file)

sns.set_style('darkgrid')
markers = {"Adelie": "X", "Gentoo": "s", "Chinstrap":'o'}
alt_chart = (
    alt.Chart(penguins_df, title="Scatterplot of Palmer's Penguins")
    .mark_circle()
    .encode(
        x=selected_x_var,
        y=selected_y_var,
        color="species",
        #color is given for the column we want to color code on graph from the dataset we are upoading
    )
    .interactive()
)
st.altair_chart(alt_chart, use_container_width=True)


