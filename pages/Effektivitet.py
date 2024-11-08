import streamlit as st
import pandas as pd
import os
import json
from app import *

index_area = "Effektivitet"
st.title(index_area)

options = [
    "Använder resurser på bästa sätt",
    "Beslutsprocessen",
    "Gemensamt mål",
    "Planerar vårt arbete"
]

print_on_page(index_area, options)