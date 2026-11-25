import pandas as pd
import streamlit as st

DATA_PATH = "data/nba.csv"

st.set_page_config(page_title="NBA Dashboard", layout="wide")


@st.cache_data
def load_data(path=DATA_PATH):
    """Load the NBA game data, one row per team per completed game."""
    df = pd.read_csv(path)
    df["DATE"] = pd.to_datetime(df["DATE"], format="%m/%d/%Y")
    return df


df = load_data()

st.title("NBA Dashboard")
st.caption(
    f"{len(df):,} team-game rows "
    f"({df['DATE'].min():%b %d, %Y} to {df['DATE'].max():%b %d, %Y})"
)

tab_explore, tab_logistic, tab_cluster = st.tabs(
    ["Explore Data", "Logistic Regression", "Clustering"]
)

with tab_explore:
    st.header("Explore Data")
    st.write("Placeholder: data exploration goes here.")

with tab_logistic:
    st.header("Logistic Regression")
    st.write("Placeholder: logistic regression model goes here.")

with tab_cluster:
    st.header("Clustering")
    st.write("Placeholder: clustering analysis goes here.")
