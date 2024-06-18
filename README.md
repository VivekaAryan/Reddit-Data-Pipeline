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

This project covers the process of connecting Apache Airflow to a Reddit instance in the cloud. [PRAW: the Python Reddit API Wrapper](https://praw.readthedocs.io/en/stable/) was leveraged and injected with Reddit API credentials to extract subreddit posts and metadata from the Reddit app, which was integrated into the Airflow setup. The airflow environment was configured with a Celery backend and PostgreSQL for efficient task management and data storage. The Reddit data within Airflow was transferred to an S3 bucket. AWS Glue was utilized for data manipulation before querying and visualizing the data with Amazon Athena. Additionally, a data warehouse was set up on AWS using Amazon Redshift to demonstrate real-time data loading.

## Overview
This pipeline is structured to accomplish the following tasks:

- __Extraction__: Retrieve data from Reddit utilizing its API.
- __Storage__: Store the raw data efficiently into an S3 bucket managed by Airflow.
- __Transformation__: Employ AWS Glue and Amazon Athena to transform the data effectively.
- __Loading__: Load the transformed data seamlessly into Amazon Redshift, facilitating analytics and query operations.

## Architecture

![Retrospectives - Reddit Data Engineering - Pipeline (2)](https://github.com/VivekaAryan/Reddit-Data-Pipeline/assets/52493029/f5a41578-c7bd-4573-bdb3-e1c48aa88e5b)

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
- Understanding of __PRAW: the Python Reddit API Wrapper__.


## Detailed Workflow
### 1. Setting up Apache Airflow with Celery Backend and Postgres

#### 1.1. Create ```docker-compose.yaml``` file

Create a ```docker-compose.yaml``` file to define, configure, and manage multi-container Docker application. The file sets up a complete Apache Airflow environment with PostgreSQL and Redis as dependencies, and defines various services for initializing, running the webserver, scheduler, and worker processes. This setup is useful for orchestrating complex workflows and data pipelines using Airflow.

__YAML Anchor__: <br>
Defines a common configuration for Airflow services. This helps avoid duplication by allowing the same configuration to be referenced in multiple places. The key elements are:

- ```build```: Specifies the build context and Dockerfile for building the custom Airflow image.
- ```image```: Specifies the custom Airflow image to use.
- ```env_file```: Specifies the environment file to use for Airflow.
- ```volumes```: Mounts directories from the host machine to directories within the Airflow container.
- ```depends_on```: Specifies that the Airflow services depend on the PostgreSQL and Redis services.

__Services__:<br>
This section defines various services using Docker images. Each service represents a container. Services include:

- ```postgres```: PostgreSQL database container with environment variables for user, password, database name, and port mapping.
- ```redis```: Redis database container with port mapping.
- ```airflow-init```: Initializes Airflow by installing dependencies, initializing the database, and starting Airflow. It uses the common configuration defined by the YAML anchor.
- ```airflow-webserver```: Runs the Airflow webserver, exposing it on port 8080. Uses the common configuration.
- ```airflow-scheduler```: Runs the Airflow scheduler, using the common configuration.
- ```airflow-worker```: Runs an Airflow worker using Celery, with the common configuration.

A brief on the tools used:
- __Redis__: Redis (Remote Dictionary Server) is an open-source, in-memory data structure store that can be used as a database, cache, and message broker. 
    - __Utilization__:
        - __Task Queue Management__: When using CeleryExecutor, Airflow uses Redis to queue tasks that need to be executed by workers. Redis handles the messages (tasks) efficiently due to its in-memory nature, allowing quick enqueue and dequeue operations.
        - __Scalability__: Redis helps in scaling the task execution by distributing tasks among multiple worker nodes. As tasks are queued in Redis, they can be pulled and executed by any available worker.In the project, Redis was used as a message broker to manage communication between different components of the Airflow system.

- __PostgreSQL__: PostgreSQL is a powerful, open-source, object-relational database system. In Airflow, PostgreSQL is typically used as the metadata database to store information about the state of tasks, workflows, users, and other operational data necessary for Airflow's functioning.
    - __Utilization__:
        - __State Management__: All state information about DAGs (Directed Acyclic Graphs), task instances, and their execution status are stored in the PostgreSQL database. This includes scheduling information, task start and end times, and execution results.
        - __User Management__: PostgreSQL stores user data and access control information, including user roles and permissions.
        - __Configuration Storage__: Various configuration settings and connections (to external systems) defined in Airflow are also stored in the PostgreSQL database.

- __Celery__: Celery is an open-source, distributed task queue system. It is designed to handle the execution of tasks asynchronously, allowing for scalable and distributed processing. Celery is often used in conjunction with message brokers like Redis or RabbitMQ and a results backend like PostgreSQL to manage and coordinate task execution.
    - __Utilization__:
        - __Task Execution__: Celery workers pick up tasks from the Redis queue, execute them, and then report the results back to the PostgreSQL database.
        - __Concurrency__: Multiple Celery workers can run in parallel, each capable of executing different tasks simultaneously, thus improving the throughput of the Airflow system.
        - __Fault Tolerance__: Celery handles task retries and failures, providing robustness to the workflow execution. If a worker fails to execute a task, Celery can reassign the task to another worker.

#### 1.2. Create ```Dockerfile``` file
This Dockerfile is used to build a custom Apache Airflow image with specific dependencies. Here's a brief summary of each step:

- __Base Image__: Starts with the official Apache Airflow image, version 2.7.1 with Python 3.11.
- __Copy Dependencies__: Copies the requirements.txt file from the local directory to the Airflow directory in the container.
- __Install System Packages__: Switches to the root user, updates package lists, and installs gcc and python3-dev to compile and build Python packages.
- __Switch User__: Switches back to the airflow user to follow security best practices.
- __Install Python Packages__: Installs the Python packages listed in requirements.txt using pip.

This setup ensures that the custom Airflow environment has all the necessary dependencies and configurations to run your workflows efficiently.

#### 1.2. Create ```airflow.env``` file
This environment file is crucial for configuring an Apache Airflow deployment with CeleryExecutor, using Redis as a message broker and PostgreSQL as both the result backend and metadata database. The configurations ensure secure storage of sensitive data and appropriate logging levels, while also preventing unnecessary example DAGs from being loaded.

Here's a summary of each variable:

- ```AIRFLOW__CORE__EXECUTOR=CeleryExecutor```<br>
    Sets the executor type to CeleryExecutor, enabling distributed task execution using Celery.

- ```AIRFLOW__CELERY__BROKER_URL=redis://redis:6379/0```<br>
    Specifies the URL for the Celery message broker. In this case, it's using Redis running on the redis service, accessible at port 6379 and database 0.
    
- ```AIRFLOW__CELERY__RESULT_BACKEND=db+postgresql://postgres@postgres:5432/airflow_reddit```<br>
    Sets the result backend for Celery to a PostgreSQL database. This URL points to a PostgreSQL database named airflow_reddit hosted on the postgres service, with postgres as both the username and password.

- ```AIRFLOW__DATABASE__SQL_ALCHEMY_CONN=postgresql+psycopg2://postgres@postgres:5432/airflow_reddit```<br>
    Configures the SQLAlchemy connection string for the Airflow metadata database. It uses PostgreSQL with the psycopg2 driver, connecting to the airflow_reddit database with postgres as the username and password.

- ```AIRFLOW__CORE__FERNET_KEY=46BKJoQYlPPOexq0OhDZnIlNepKFf87WFwLbfzqDDho=```<br>
    Provides the Fernet key for encrypting sensitive data in the Airflow metadata database. Fernet encryption is used to securely store connection credentials.

- ```AIRFLOW__CORE__LOGGING_LEVEL=INFO```<br>
    Sets the logging level to INFO, which controls the verbosity of Airflow's logging output.

- ```AIRFLOW__CORE__LOAD_EXAMPLES=False```<br>
    Disables the loading of example DAGs. By setting this to False, Airflow won't load the example workflows, keeping the environment clean and focused on user-defined DAGs.

After these are created, test if all the services are correctly setup by running the following command in the terminal:
```bash
docker compose up -d --build
```
Note: Make sure docker desktop is already running.

### 2. Build Reddit Data Pipeline with Airflow
#### 2.1 Define an Airflow DAG for orchestrating ETL
Once set up is finished, define an Apache Airflow Directed Acyclic Graph (DAG)in the ```dag``` folder for orchestrating a two-step ETL (Extract, Transform, Load) pipeline. The tasks are scheduled to run daily, ensuring the ETL pipeline is executed on a regular basis, with proper handling of task dependencies and configurations. 

- __Dag 1:__<br>
 __Extracts data from specified subreddits__ using the ```reddit_pipeline``` function, which connects to Reddit, extracts posts, transforms the data, and saves it as a CSV file.

- __Dag 2:__<br>
__Uploads the extracted data to AWS S3__ using the ```upload_s3_pipeline``` function.

In the end write a task dependency:

```Python
extract >> upload_s3
```

This mean that the upload_s3 task will only run after the extract task has successfully completed.

#### 2.2 Setup ```Config.conf```
The ```config.conf``` file is used to centralize configuration settings for an application, making it easier to manage and change parameters without altering the code. This file is particularly useful in environments where settings need to be easily adjustable, such as development, testing, and production. In the project we store Database Configurations, File Paths, Reddit credentials, AWS credentials and etl settings.

#### 2.3. Create constants.py
This script reads the ```config.conf``` fiel to get necessary configuration setting and sets these setting as variables that can be used in othe rparts of the project. This provides easy access to configuration values, which helps in managing and updating the configuration without changing the code.

#### 2.4 Write ```reddit_etl.py```
This script defines a series of functions to connect to Reddit using the PRAW (Python Reddit API Wrapper) library, extract posts from specified subreddits, transform the extracted data into a structured format using pandas, and load the data into a CSV file. This ETL (Extract, Transform, Load) process is essential for gathering and preparing Reddit data for analysis or further processing. This structured approach enables efficient data collection and preparation, facilitating the use of Reddit data in various data science and analysis tasks.

#### 2.5 Write Reddit pipeline (```reddit_pipeline.py```)
The reddit_pipeline function orchestrates the process of extracting, transforming, and loading data from Reddit. It connects to Reddit using provided credentials, extracts posts from a specified subreddit, transforms the data into a suitable format, and saves the data as a CSV file. This function simplifies the process of gathering and preparing Reddit data for analysis or further processing, making it a reusable component in data workflows.


### 3. Build Reddit Data Pipeline with AWS
#### 3.1. Creating an S3 bucket
Amazon S3 (Simple Storage Service) is a scalable object storage service provided by Amazon Web Services (AWS). It allows you to store and retrieve any amount of data at any time, making it ideal for a wide range of use cases, including backup and restore, disaster recovery, data archives, and content distribution. To begin using S3, you first need to create an S3 bucket, which acts as a container for storing your objects (files and data).

#### 3.2. Write ```aws_etl.py```
This script provides functions to connect to an Amazon S3 bucket, check if a bucket exists (and create it if it doesn't), and upload a file to the bucket using the s3fs library. The functions utilize AWS credentials stored in constants and handle exceptions to ensure smooth execution.

#### 3.3. Write AWS Pipeline (```aws_s3_pipeline.py```)
The upload_s3_pipeline function defines a pipeline to upload a file to an AWS S3 bucket. It pulls the file path from a previous Airflow task, connects to S3, ensures the target bucket exists, and uploads the file to the bucket. This function facilitates the integration of data pipelines with cloud storage, allowing for scalable and reliable data management.

After these are set up, trigger the dag once again for the whole ETL pipeline to run from extracting posts from subreddit, saving the data in a CSV file after transforming the data and loading the data in CSV. The second dag should take the csv and push it to AWS S3 bucket for storing on the cloud.

## Contribution
Contributions, suggestions, and bug reports are welcome! Please follow the standard GitHub practices for pull requests and issue tracking.

## License
This project is licensed under the MIT License.



  
## _Appendix_
- A __Docker container__ is a self-contained, runnable software application or service. On the other hand, a __Docker image__ is the template loaded onto the container to run it, like a set of instructions. You store images for sharing and reuse, but you create and destroy containers over an application's lifecycle.

- ```touch``` is commonly used in Unix-based systems (such as Linux or macOS) to create empty files or update file timestamps. In Windows, you can achieve the same functionality by creating an empty file using
    ```
    NUL > airflow.env
    NUL > docker-compose.yml
    NUL > Dockerfile
    ```

- The ```docker-compose.yml``` file is used to define and run multiple Docker containers as services that collectively make up an __Apache Airflow__ environment along with __PostgreSQL__ and __Redis databases__.
