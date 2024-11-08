import streamlit as st
import pandas as pd
import os
import json
from app import *

index_area = "Arbetstakt"
st.title(index_area)

options = [
    "Fundera",
    "Genomföra",
    "Planera",
    "Reflektera"
]

print_on_page(index_area, options)