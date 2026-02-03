import streamlit as st
import pandas as pd

st.set_page_config(page_title="Finanças", page_icon="🔥")

st.markdown("# Finanças")


file_upload = st.file_uploader("Carregar arquivo de transações financeiras", type=["csv"])


if file_upload:

    df = pd.read_csv(file_upload)


    columns_fmt = {"Valor": st.column_config.NumberColumn(format="R$ %.2f")}

    st.dataframe(df, hide_index=True, column_config=columns_fmt)


