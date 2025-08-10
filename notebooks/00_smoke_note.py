# Databricks notebook source
# MAGIC %md
# MAGIC # Smoke Notebook
# MAGIC Este notebook es solo para validar que la importación al Workspace funciona.

# COMMAND ----------
print("Hola desde Databricks ✅")

# COMMAND ----------
from pyspark.sql import Row
df = spark.createDataFrame([Row(x=1), Row(x=2), Row(x=3)])
display(df)

# COMMAND ----------
# Listar catálogos (Unity Catalog)
spark.sql("SHOW CATALOGS").show()
