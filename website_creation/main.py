import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title='Competitive Breaking', layout='wide',
                #    initial_sidebar_state=st.session_state.get('sidebar_state', 'collapsed'),
)

st.markdown('Who Are We?')
st.sidebar.markdown("Who Are We?")

st.title('Welcome to Settle it in the Cypher!')
st.subheader('Competitive Breaking Data')
st.text('Open Breaking is a project to collect competitive breaking data and produce findings through analysis that can be incorporated into the further development of competitive breaking.')

#st.image("./logo.png", width = 500)
st.sidebar.image("./logo.png", use_column_width=True)

