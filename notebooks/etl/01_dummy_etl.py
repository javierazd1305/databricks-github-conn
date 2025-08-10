# Databricks notebook source
# MAGIC %md
# MAGIC # Dummy ETL
# MAGIC Crea un DataFrame de ejemplo y calcula una columna derivada.

# COMMAND ----------
from pyspark.sql import functions as F

data = [(1, "A", 10.5),
        (2, "B", 20.0),
        (3, "C", 7.25)]
df = spark.createDataFrame(data, ["id", "category", "value"])

df = df.withColumn("value_x2", F.col("value") * 2)

display(df)

# COMMAND ----------
print("ETL dummy finalizado.")
