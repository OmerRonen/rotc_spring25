import pandas as pd

from .utils import TBI_CODES

# read the data "data/physionet.org/files/mimiciv/3.1/hosp/labevents.csv.gz" file
data = pd.read_csv("data/physionet.org/files/mimiciv/3.1/hosp/d_labitems.csv.gz")

unique_categories = data['category'].unique()

print(unique_categories)

# # filter the data to only include the TBI codes
# data = data[data['category'].isin(TBI_CODES)]
