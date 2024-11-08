import streamlit as st
import pandas as pd
import os
import json
from app import *

index_area = "Återkoppling"
st.title(index_area)

options = [
    "Kommunicerat vad som förväntas",
    "Konstruktiv dialog",
    "Positiv feedback"
]

print_on_page(index_area, options)