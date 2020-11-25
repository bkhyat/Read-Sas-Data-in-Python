import glob
import datetime
import pyreadstat
import pandas as pd
from sas7bdat import SAS7BDAT

files = glob.glob("*.sas7bdat")
"""print("filenames")
for file in files:
    print(file)"""

temp = [] # List to store the List of times for each epoch
for i in range(100):
    start = datetime.datetime.now()
    for file in files:
        df = pd.read_sas(file)
    pandas_time = (datetime.datetime.now()-start).microseconds/1000

    start = datetime.datetime.now()
    for file in files:
        reader = SAS7BDAT(file)
        df = reader.to_data_frame()
    sas7bdat_time = (datetime.datetime.now()-start).microseconds/1000

    start = datetime.datetime.now()
    for file in files:
        df, _ = pyreadstat.read_sas7bdat(file)
    pyreadstat_time = (datetime.datetime.now()-start).microseconds/1000

    temp.append([pandas_time, sas7bdat_time, pyreadstat_time])

cols = ['pandas (milisecond)', 'sas7bdat (milisecond)', 'pyreadstat (milisecond)']
result = pd.DataFrame(data=temp, columns=cols)
result.to_csv('benchmark_result.csv', index_label='Epoch')
