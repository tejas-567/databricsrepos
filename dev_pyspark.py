# Databricks notebook source
data = "dbfs:/FileStore/donations.csv"
df = spark.read.format("csv").option("header","true").option("sep",",").option("inferSchema","true").load(data)
df.show(5)
