import streamlit as st
import pandas as pd
import os
import json
from app import *

index_area = "Ledarskap"
st.title(index_area)

options = [
    "Förklara hur vi ska nå målen",
    "Konsekvent agerande",
    "Tydlig kommunikation"
]

print_on_page(index_area, options)