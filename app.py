import notion_df
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Criascritic", page_icon="🍷", layout="wide")


@st.cache_data(ttl=3600)
def load_dataframe_from_notion_database():
    notion_df.pandas()
    df = notion_df.download(
        st.secrets["NOTION_DATABASE_URL"],
        api_key=st.secrets["NOTION_INTEGRATION_TOKEN"],
    )
    data_df = df.filter(
        items=[
            "Nome do Jogo",
            "Nota Pessoal",
            "Nota Técnica",
            "História",
            "Gameplay",
            "Direção de Arte",
            "Técnico",
        ]
    )
    grouped_data_df = data_df.groupby("Nome do Jogo").mean().reset_index()
    grouped_data_df["Reviews"] = data_df.groupby("Nome do Jogo").size().values
    grouped_data_df = grouped_data_df.sort_values("Reviews", ascending=False)

    return grouped_data_df


grouped_data_df = load_dataframe_from_notion_database()

st.title("Criascritic 🍷")

st.dataframe(
    grouped_data_df,
    column_config={
        "Nome do Jogo": st.column_config.TextColumn(
            help="Nota do Jogo", width="medium"
        ),
        "Nota Pessoal": st.column_config.ProgressColumn(
            help="Nota pessoal do jogo",
            format="%d",
            min_value=0,
            max_value=100,
        ),
        "Nota Técnica": st.column_config.ProgressColumn(
            help="Nota técnica do jogo",
            format="%d",
            min_value=0,
            max_value=100,
        ),
        "História": st.column_config.ProgressColumn(
            help="Nota da história do jogo",
            format="%d",
            min_value=0,
            max_value=100,
        ),
        "Gameplay": st.column_config.ProgressColumn(
            help="Nota da gameplay do jogo",
            format="%d",
            min_value=0,
            max_value=100,
        ),
        "Direção de Arte": st.column_config.ProgressColumn(
            help="Nota da direção de arte do jogo",
            format="%d",
            min_value=0,
            max_value=100,
        ),
        "Técnico": st.column_config.ProgressColumn(
            help="Nota do técnico do jogo",
            format="%d",
            min_value=0,
            max_value=100,
        ),
        "Tempo de Jogo (hora)": st.column_config.NumberColumn(
            label="Horas",
            help="Quantas horas possui no jogo",
            format="%d",
        ),
        "Reviews": st.column_config.TextColumn(
            label="Reviews",
            help="Quantidade de reviews do jogo",
        ),
    },
    height=700,
    hide_index=True,
)
