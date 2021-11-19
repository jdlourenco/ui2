import streamlit as st

import numpy as np
import pandas as pd

st.markdown("""# This is a header
## This is a sub header
This is text

Another line

whatever""")

st.write('hello 👋')

st.sidebar.markdown(f"""
    # Header resizer
    """)

st.sidebar.text("olha")

with st.echo():
    st.write('hello 👋')


df = pd.DataFrame({
          'first column': list(range(1, 11)),
          'second column': np.arange(10, 101, 10)
        })

# this slider allows the user to select a number of lines
# to display in the dataframe
# the selected value is returned by st.slider
line_count = st.slider('Select a line count', 1, 10, 3)

line_count

# # and used in order to select the displayed lines
head_df = df.head(line_count)

head_df

@st.cache
def get_line_chart_data():

    return pd.DataFrame(
            np.random.randn(20, 3),
            columns=['a', 'b', 'c']
        )

df = get_line_chart_data()

st.line_chart(df)