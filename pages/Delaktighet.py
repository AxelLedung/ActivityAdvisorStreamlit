import streamlit as st
import pandas as pd
import os
import json
from app import *

index_area = "Delaktighet"
st.title(index_area)

options = [
    "Arbetssituation",
    "Kommentera på information",
    "Påverka beslut",
    "Påverka hur",
    "Påverka vad",
    "Tillräckligt med befogenheter"
]

print_on_page(index_area, options)