import os
import json
import tqdm
import pickle
import shutil
import datetime
import tempfile

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import streamlit as st
import plotly.graph_objs as go
from pyproj import Transformer
from PIL import Image


def display():
	st.header('SLAM Demo')
	st.image('data/demo_img.jpg')


if __name__ == "__main__":
	display()

