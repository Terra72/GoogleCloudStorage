import os
from google.cloud import storage
#os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'splendid-light-349913-c9fcf83d3ee2.json'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'keys/splendid-light-349913-2835dbf6f08b.json'

storage_client = storage.Client()


# Create a new Bucket

bucket_name = 'tut1_data_bucket'
bucket = storage_client.bucket(bucket_name)
if storage_client.get_bucket(bucket_name) == None:
    print ("creating new bucket: ", bucket.name)
    bucket = storage_client.create_bucket(bucket,location='US')
else:
    print ("bucket found: ", bucket.name)

# retrieve a specific storage bucket    
my_bucket = storage_client.get_bucket(bucket_name)
# print bucket Detail
#print (vars(bucket))

def upload_to_bucket(blob_name, file_path, bucket_name):
    """
    Upload files 
    """
    try:
        bucket = storage_client.get_bucket(bucket_name)
        blob = bucket.blob(blob_name)
        blob.upload_from_filename(file_path)
        return True
    except Exception as e:
        print("error: ", e)
        return False


file_path = r'C:/Users/daniel.bowden/PycharmProjects/GoogleCloudStorage/data_to_upload'
file_name = 'voice_list.csv'
upload_to_bucket('Voice List JJ1', os.path.join(file_path, file_name).replace("\\","/"), bucket_name)
upload_to_bucket('document/Voice List JJ2', os.path.join(file_path, file_name).replace("\\","/"), bucket_name)

def download_bucket_file(blob_name, file_path, target_bucket_name):
    try:
        bucket = storage_client.get_bucket(target_bucket_name)
        blob = bucket.blob(blob_name)
        with open(file_path, 'wb') as f:
            storage_client.download_blob_to_file(blob, f)
        return True
    except Exception as e:
        print('download_bucket_file error:\n',e)
        return False

print  (os.path.join(os.getcwd(), 'file1.csv'))
download_bucket_file('Voice List JJ1', os.path.join(os.getcwd(), 'data_downloaded', 'file1.csv'), bucket_name)
download_bucket_file('document/Voice List JJ2', os.path.join(os.getcwd(), 'data_downloaded', 'file2.csv'), bucket_name)