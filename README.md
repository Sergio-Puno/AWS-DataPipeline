AWS Pipeline Project - Repository for project description and documentaiton along with Python scripts, Spark scripts, and SQL queries used during the creation of the pipeline and post pipeline analytics.

**Contents**

- [Introduction and Goals](#introduction-and-goals)
- [Dataset Overview](#dataset-overview)
- [Tools and Services](#tools-and-services)
  - [Connect](#connect)
  - [Buffer](#buffer)
  - [Processing](#processing)
  - [Storage](#storage)
  - [Visualization](#visualization)
- [Pipeline Breakdown](#pipeline-breakdown)
  - [Stream Processing](#stream-processing)
  - [Batch Processing](#batch-processing)
- [PowerBI Visualization](#powerbi-visualization)
- [Conclusion](#conclusion)

---

# Introduction and Goals
The purpose of this personal project is to establish a data pipeline for e-commerce data to be transported to a PowerBI dashboard for business analysts. There are many issues to be considered and many individual components that influence your ability to consolidate data within a company. A few of the initial considerations when beginning this project:

- Data Sources: Internal operational database for transactions, CRM platforms, CSV or other file datasets.
- Data Quality: The quality of the data being processesed directly impacts the services and tooling required to properly store and use the data for analytical purposes.
- Internal Customers: All data pipelines have the potential to services multiple end clients inside the company rather than just a single group. There may be sales teams, executive level individuals, supply chain teams, machine maintenance teams and many more who require the pipeline to provide value for them.
- Documentation: For each of the outputs that your pipeline connects to (dashboards, warehouses, data lakes, etc) all have an end use and a process that involves many source streams and transformations. All this required proper documentations and testing to ensure that the tema knows how each piece works and can quickly respond to issues that arise.


# Dataset Overview
The dataset used for this pipeline project came from a Kaggle project located [here](https://www.kaggle.com/datasets/carrie1/ecommerce-data). This information comes from a UK based retailer and represents a subset of actual transaction data from 2010 to 2011.

As this dataset is a record of transactions, it is in a "long" format meaning invoice numbers will repeat for each unique item that was on the invoice. The column headers and the datatype I will use within AWS are:

- InvoiceNo (text)
- StockCode (text)
- Description (text)
- Quantity (integer)
- InvoiceDate (text)
- UnitPrice (float)
- CustomerID (integer)
- Country (text)

Many of the fields will end up becoming text fields, including the invoice number which has instances of a "C" prefix so we cannot store this column as an integer.

Looking ahead to how an analyst might be viewing this information, it is important to consider the exisitng fields as well as potential calculated fields that would be important to have. In this case having a total calculated cost for each line would be useful for invoice value aggreagations as well as determining highest revenue products.

# Tools and Services
For this project I will be focused on using Python as the scripting language for both the front end data streaming as well as the AWS Lambda functions within the pipeline.

The AWS services used in this project include:
- API Gateway
- Kinesis / Kinesis Firehose
- S3
- DynamoDB
- Redshift
- Glue

Secondary software used:
- VS Code
- Excel
- PowerBI

## Connect
Api Gateway

## Buffer
Kinesis (message queue service)
Kinesis Firehose (fore Redshift connection)

## Processing
Lambda functions

## Storage
S3 (raw data store)
DynamoDB (noSQL store, wide column)
Redshift (data warehouse)

## Visualization
PowerBI (through Redshift connection)

# Pipeline Breakdown


## Stream Processing

For the stream processing pipeline I needed to setup a Python script that would mimic incoming transaction data as though it we being fed by multiple operational databases. This would simulate the situation of having multiple retail locations all processing their own invoices and streaming that data out of the OLTP data warehouse into our data pipeline and into a OLAP data warehouse.

## Batch Processing

Contrary to the stream processing, our batch processing pipeline will mimic a workflow that involves bulk data dumps which may occur hourly, daily, etc. This process differs from the stream pipeline in a few key ways:

- Not a continuous stream of data which requires a strong buffer system to manage triggers
- Makes use of AWS Glue Crawlers to tracking new data files stored in an S3 bucket and executes a Spark Glue Job which transfers the data into a RedShift Table

# PowerBI Visualization

# Conclusion