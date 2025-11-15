# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "59c7187a-f6a9-4486-b4d6-740b0dab5028",
# META       "default_lakehouse_name": "testLakehouse1",
# META       "default_lakehouse_workspace_id": "0b757bbc-b963-4071-9c9e-b2799e4ba796",
# META       "known_lakehouses": [
# META         {
# META           "id": "59c7187a-f6a9-4486-b4d6-740b0dab5028"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

# Welcome to your new notebook
# Type here in the cell editor to add code!
df = spark.read.format("csv").load("Files/sharetest/bikes.csv")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
