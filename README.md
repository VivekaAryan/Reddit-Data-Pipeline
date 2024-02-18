# Reddit Data Pipeline
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Airflow](https://img.shields.io/badge/Airflow-blue.svg)](https://airflow.apache.org/docs/)
[![Celery](https://img.shields.io/badge/Celery-green.svg)](https://docs.celeryq.dev/en/stable/getting-started/introduction.html)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-red.svg)](https://www.postgresql.org/docs/)
[![AWS S3](https://img.shields.io/badge/AWS%20S3-yellow.svg)](https://docs.aws.amazon.com/s3/)
[![AWS Glue](https://img.shields.io/badge/AWS%20Glue-blue.svg)](https://docs.aws.amazon.com/glue/)
[![Amazon Athena](https://img.shields.io/badge/Amazon%20Athena-green.svg)](https://docs.aws.amazon.com/athena/)
[![Amazon Redshift](https://img.shields.io/badge/Amazon%20Redshift-red.svg)](https://docs.aws.amazon.com/redshift/)
[![SQL](https://img.shields.io/badge/SQL-yellow.svg)](https://www.w3schools.com/sql/sql_quickref.asp)
[![Python](https://img.shields.io/badge/Python-blue.svg)](https://docs.python.org/3.11/)
[![PySpark](https://img.shields.io/badge/PySpark-green.svg)](https://spark.apache.org/docs/latest/api/python/index.html)
[![API](https://img.shields.io/badge/API-red.svg)](https://aws.amazon.com/what-is/api/#:~:text=API%20stands%20for%20Application%20Programming,other%20using%20requests%20and%20responses.)


This project offers a robust data pipeline solution designed to efficiently extract, transform, and load (ETL) Reddit data into a Redshift data warehouse. Leveraging a blend of industry-standard tools and services, the pipeline ensures seamless data processing and integration.

## Overview
This pipeline is structured to accomplish the following tasks:

- __Extraction__: Retrieve data from Reddit utilizing its API.
- __Storage__: Store the raw data efficiently into an S3 bucket managed by Airflow.
- __Transformation__: Employ AWS Glue and Amazon Athena to transform the data effectively.
- __Loading__: Load the transformed data seamlessly into Amazon Redshift, facilitating analytics and query operations.

## Architecture

![Retrospectives - Reddit Data Engineering - Pipeline](https://github.com/VivekaAryan/Reddit-Data-Pipeline/assets/52493029/5816ce6f-dfff-4493-9797-13af63cd3308)

- __Apache Airflow__: The pipeline orchestrator for scheduling and managing ETL workflows.
- __Celery__: Facilitates distributed task execution, enhancing scalability and performance.
- __PostgreSQL__: Utilized for intermediate data storage and manipulation.
- __Amazon S3__: Provides scalable and durable storage for raw and processed data.
- __AWS Glue__: Offers automated ETL service for data discovery, transformation, and loading.
- __Amazon Athena__: Enables querying data directly from S3, optimizing for cost-effectiveness and efficiency.
- __Amazon Redshift__: The ultimate destination for the transformed and aggregated Reddit data, offering high-performance data warehousing capabilities.

## Requirements and Preparations
- An __AWS Account__ with suitable permissions for S3, Glue, Athena, and Redshift. Ensure that IAM (Identity and Access Management) roles and policies are configured correctly to grant necessary access.
- __Reddit API__ credentials. You can configure your API by following the instructions [here](https://www.reddit.com/wiki/api/).
- Installation of __Postman__ to confirm if the Reddit API credentials are working properly. You can follow the detailed [video](https://www.youtube.com/watch?v=x9boO9x3TDA) to validate your credentials.
- Installation of __Docker__.
- Python version 3.9 or higher.
  
# Important Learnings:
- A __Docker container__ is a self-contained, runnable software application or service. On the other hand, a __Docker image__ is the template loaded onto the container to run it, like a set of instructions. You store images for sharing and reuse, but you create and destroy containers over an application's lifecycle.

# Appendix:
- ```touch``` is commonly used in Unix-based systems (such as Linux or macOS) to create empty files or update file timestamps. In Windows, you can achieve the same functionality by creating an empty file using
```
NUL > airflow.env
NUL > docker-compose.yml
NUL > Dockerfile
```

- The ```docker-compose.yml``` file is used to define and run multiple Docker containers as services that collectively make up an __Apache Airflow__ environment along with __PostgreSQL__ and __Redis databases__.
