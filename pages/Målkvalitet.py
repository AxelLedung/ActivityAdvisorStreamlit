import streamlit as st
import pandas as pd
import os
import json
from app import *

index_area = "Målkvalitet"
st.title(index_area)

options = [
    "Påverkningsbara",
    "Realistiska",
    "Tydliga",
    "Uppföljningsbara"
]

print_on_page(index_area, options)