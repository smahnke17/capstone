import streamlit as st
import pandas as pd
import numpy as np

#df = st.file_uploader("./data.csv", type={"csv"})

show_df = pd.read_csv("./data.csv",)
st.dataframe(show_df,
             column_config={
        "Video Link": st.column_config.LinkColumn("App URL"),
    },
    hide_index=True,)
