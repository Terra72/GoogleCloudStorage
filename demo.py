import os
from google.cloud import storage
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'splendid-light-349913-c9fcf83d3ee2.json'

storage_client = storage.Client()


# Create a new Bucket

bucket_name = 'tut1_data_bucket'
bucket = storage_client.bucket(bucket_name)
if storage_client.get_bucket(bucket_name) == None:
    print ("creating new bucket: ", bucket.name)
    bucket = storage_client.create_bucket(bucket,location='US')
else:
    print ("bucket found: ", bucket.name)

# print bucket Detail
print (vars(bucket))