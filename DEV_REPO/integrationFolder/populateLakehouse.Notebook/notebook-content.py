# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "0deae9ed-d481-46ac-bc87-2e0ec43d37f2",
# META       "default_lakehouse_name": "testLakehouse3",
# META       "default_lakehouse_workspace_id": "0b757bbc-b963-4071-9c9e-b2799e4ba796",
# META       "known_lakehouses": [
# META         {
# META           "id": "0deae9ed-d481-46ac-bc87-2e0ec43d37f2"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

!git clone https://github.com/MicrosoftLearning/dp-data.git

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

import pandas as pd

salesdf = pd.read_csv('dp-data/sales.csv')
salesdf.to_csv("/lakehouse/default/Files/sales.csv")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
