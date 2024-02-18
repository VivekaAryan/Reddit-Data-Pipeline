import s3fs
from utils.constants import AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY

# Connecting to S3
def connect_to_s3():
    try:
        s3 = s3fs.S3FileSystem(anon = False,
                               key = AWS_ACCESS_KEY_ID,
                               secret = AWS_ACCESS_KEY)
        return s3
    
    except Exception as e:
        print(e)

# Chekcing if the bucket exists or not. Create bucket if it does not exist.
def create_bucket_if_not_exist(s3:s3fs.S3FileSystem, bucket:str):
    try:
        if not s3.exists(bucket):
            s3.mkdir(bucket)
            print("Bucket created")
        else:
            print("Bucket already exists")

    except Exception as e:
        print(e)

# Uploading the data into S3 bucket.
def upload_to_s3(s3: s3fs.S3FileSystem, file_path:str, bucket:str, s3_file_name:str):
    try:
        s3.put(file_path, bucket+'/raw/'+ s3_file_name)
        print('File uploaded to S3.')
    
    except FileNotFoundError:
        print('File not found.')