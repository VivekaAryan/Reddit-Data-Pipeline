# Pull the official Apache Airflow image, version 2.7.1 with Python 3.11
FROM apache/airflow:2.7.1-python3.11


# Copy the requirements.txt file from the local directory to the /opt/airflow/ directory in the container
COPY requirements.txt /opt/airflow/

# Switch to the root user to install additional system packages
USER root

# Update the package lists and install gcc (GNU Compiler Collection) and python3-dev (Python development headers)
RUN apt-get update && apt-get install -y gcc python3-dev

# Switch back to the airflow user for running subsequent commands in a less privileged mode
USER airflow

# Install the Python packages listed in the requirements.txt file using pip
RUN pip install --no-cache-dir -r /opt/airflow/requirements.txt
