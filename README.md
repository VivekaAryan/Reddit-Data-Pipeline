# Reddit-Data-Pipeline

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
