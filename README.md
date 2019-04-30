# csc665-assignment-final
```
.
├── code
│   │
│   ├── correlation.py
│   ├── data.py
│   ├── dataSplit.py
│   ├── energy_hist.py
│   ├── heatmap.py
│   ├── learning.py
│   ├── models.py
│   ├── modiData.py
│   └── residual_plot.py
│
├── csc665_finalReport.pdf
│
├── images
│   │
│   ├── correlation_A.png
│   ├── correlation_B.png
│   ├── correlation_C.png
│   ├── correlation_D.png
│   ├── energy_freq_mean.png
│   ├── energy_freq.png
│   ├── energy_series_total.png
│   ├── gbr_residuals.png
│   ├── heatmap.png
│   ├── knn_residuals.png
│   ├── mlp_residuals.png
│   ├── mlr_residuals.png
│   ├── rfr_residuals.png
│   └── svm_residuals.png
├── README.md
│
└── source
    │
    ├── active.csv
    ├── energydata_complete.csv
    ├── nonactive.csv
    └── output.csv

```

## csc665_finalReport.pdf
The report of my final project

## ./code/
Contains the python code for Machine Learning, Data Virtualization, and other helper codes.<br/>
ML code:<br/>
learning.py -- do the traning, validation, and testing with "tuning"<br/>
model.py -- do the traning, validation, and testing without "tuning"  Usage: python model.py <dataFile><br/>
Virtualization:<br/>
correlation.py -- draw covariance images<br/>
energy_hist.py -- draw energy usage (frequency) statistics images<br/>
heatmap.py -- draw energy usage vs time images<br/>
residual_plot.py -- draw difference of prediction vs actural value<br/>
## ./source/
Conatins<br/>
energydata_complete.csv -- source data<br/>
output.csv -- modify the data, numeralize<br/>
active.csv, nonactive.csv -- split output.csv into 2 parts by human active periods, and human non-active periods
