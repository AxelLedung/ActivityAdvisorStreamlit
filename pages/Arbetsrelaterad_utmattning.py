import streamlit as st
import pandas as pd
import os
import json
from app import *

index_area = "Arbetsrelaterad Utmattning"
st.title(index_area)

options = [
    "Känslomässigt tömd",
    "Trött",
    "Utsliten"
]

print_on_page(index_area, options)