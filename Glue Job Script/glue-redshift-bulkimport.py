import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node S3 bucket
S3bucket_node1 = glueContext.create_dynamic_frame.from_catalog(
    database="glue-transactionsdb",
    table_name="bulkimport_bucket",
    transformation_ctx="S3bucket_node1",
)

# Script generated for node ApplyMapping
ApplyMapping_node2 = ApplyMapping.apply(
    frame=S3bucket_node1,
    mappings=[
        ("invoiceno", "string", "invoiceno", "string"),
        ("stockcode", "string", "stockcode", "string"),
        ("description", "string", "description", "string"),
        ("quantity", "long", "quantity", "long"),
        ("invoicedate", "string", "invoicedate", "string"),
        ("unitprice", "double", "unitprice", "double"),
        ("customerid", "long", "customerid", "long"),
        ("country", "string", "country", "string"),
    ],
    transformation_ctx="ApplyMapping_node2",
)

# Script generated for node AWS Glue Data Catalog
AWSGlueDataCatalog_node1654052826221 = glueContext.write_dynamic_frame.from_catalog(
    frame=ApplyMapping_node2,
    database="glue-transactionsdb",
    table_name="dev_public_bulkimport",
    redshift_tmp_dir=args["TempDir"],
    transformation_ctx="AWSGlueDataCatalog_node1654052826221",
)

job.commit()