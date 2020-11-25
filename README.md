# Read-Sas-Data-in-Python
<p> This repo contains different methods to read sas7dbat binary data files properly in Python. I have basically used 3 libraries namely pandas, sas7dbat, and pyreadstat to read the sas7dbat data files as pandas dataframe.
Furthermore, it's more like a benchmarking test to read sas7dbat files in Python using different libraries and compare their time efficiency.
It has used US disease datasets for the comparison, the detail about the data files and the link to the datafiles are available in the notebook.
All the files have been read 100 times using each libraries, and time taken to load the dataframe has been captured and finally the csv file is output which contains time taken by each of the libraries to read those files on each iteration.
Finally brief result statistics have been presented.
Based on those results, I have come to conclusion that pyreadstat is relatively faster than other two, the min time and standard deviations are lowest for pyreadstat.
  </p>
  
