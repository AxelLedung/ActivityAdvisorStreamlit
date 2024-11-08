import streamlit as st
import pandas as pd
import os
import json
from app import *

index_area = "Medarbetarkraft"
st.title(index_area)

options = [
    "Irritation",
    "Koncentrationsvårigheter",
    "Oro",
    "Rastlöshet",
    "Uppgivenhet"
]

print_on_page(index_area, options)