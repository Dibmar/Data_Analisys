import pandas as pd
import numpy as np

def import_csv (path):
    df = pd.read_csv(path)
    return df