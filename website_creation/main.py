import streamlit as st
from st_pages import Page, show_pages, add_page_title
import pandas as pd
import numpy as np

#add_page_title()

show_pages(
    [
        Page("./main.py", "Home", "🏠"),
        Page("./pages/01_Player_Profiles.py", "Dancer Profiles", ":trophy:"),
        Page("./pages/02_Judge_Profiles.py", "Judge Profiles", ":male-judge:"),
        Page("./pages/03_Our_Data.py", "Our Data", ":male-technologist:"),
    ]
)
#st.set_page_config(page_title='Competitive Breaking', layout='wide',
                #    initial_sidebar_state=st.session_state.get('sidebar_state', 'collapsed'),
#)

st.markdown('Who Are We?')
st.sidebar.markdown("Who Are We?")

st.title('Welcome to Settle it in the Cypher!')
st.subheader('Competitive Breaking Data')
st.text('Open Breaking is a project to collect competitive breaking data and produce findings through analysis that can be incorporated into the further development of competitive breaking.')

#st.image("./logo.png", width = 500)
st.sidebar.image("./logo.png", use_column_width=True)

