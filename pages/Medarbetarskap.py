import streamlit as st
import pandas as pd
import os
import json
from app import *

index_area = "Medarbetarskap"
st.title(index_area)

options = [
    "Ansvar för kompetens",
    "Ansvar informerad",
    "Initiativ till förändring",
    "Öppen för förändring"
]

print_on_page(index_area, options)