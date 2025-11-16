# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "805ae812-074e-4090-bbba-d25165fa8964",
# META       "default_lakehouse_name": "testLakehouse2",
# META       "default_lakehouse_workspace_id": "0b757bbc-b963-4071-9c9e-b2799e4ba796",
# META       "known_lakehouses": [
# META         {
# META           "id": "805ae812-074e-4090-bbba-d25165fa8964"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

# Welcome to your new notebook
# Type here in the cell editor to add code!
df = spark.read.table("bikesFromDataflowLH2")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

from pyspark.sql.functions import col, expr

df = df.withColumn("fullDateInt", (col("year")*10000 + col("mnth")*100 + col("day")))

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df.write.format("delta").mode("append").saveAsTable("bikesFromNotebook")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
