import streamlit as st
import pandas as pd
import os
import json
from app import *

index_area = "Lärande i arbetet"
st.title(index_area)

options = [
    "Arbete utveklande",
    "Kompetenser tas tillvara",
    "Utvecklas yrkesmässigt"
]

print_on_page(index_area, options)