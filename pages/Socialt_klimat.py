import streamlit as st
import pandas as pd
import os
import json
from app import *

index_area = "Socialt klimat"
st.title(index_area)

options = [
    "God sammanhållning",
    "Kollegor ställer upp",
    "Positiv stämning"
]

print_on_page(index_area, options)