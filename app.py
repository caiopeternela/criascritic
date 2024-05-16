import pandas as pd
import streamlit as st

data_df = pd.read_csv("criascritic.csv", usecols=list(range(8)))

grouped_data_df = data_df.groupby("Nome do Jogo").mean().reset_index()

grouped_data_df["Reviews"] = data_df.groupby("Nome do Jogo").size().values

grouped_data_df = grouped_data_df.sort_values("Reviews", ascending=False)

st.set_page_config(page_title="Criascritic", page_icon="🍷", layout="wide")

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
        # "Zerado": st.column_config.CheckboxColumn(
        #     help="Se o cria zerou o jogo",
        # ),
        # "Platinado": st.column_config.CheckboxColumn(
        #     help="Se o cria platinou o jogo",
        # ),
        # "Dropado": st.column_config.CheckboxColumn(
        #     help="Se o cria dropou o jogo",
        # ),
        # "Genêros": st.column_config.ListColumn(
        #     label="Gêneros",
        #     help="Gêneros do jogo",
        # ),
        # "Plataforma": st.column_config.TextColumn(
        #     help="Plataforma em que o cria jogou",
        # ),
        "Reviews": st.column_config.TextColumn(
            label="Reviews",
            help="Quantidade de reviews do jogo",
        ),
        # "Criado em": st.column_config.DatetimeColumn(
        #     help="Data e hora de criação da avaliação",
        #     format="D/MM/YYYY, HH:mm"
        # ),
    },
    height=700,
    hide_index=True,
)
