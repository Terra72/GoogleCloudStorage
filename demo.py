import os
from google.cloud import storage




def createBucket(bucket_name):
    """ 
    Create a new Bucket
    """
    new_bucket = storage_client.bucket(bucket_name)
    if storage_client.get_bucket(bucket_name) == None:
        print ("creating new bucket: ", new_bucket.name)
        new_bucket = storage_client.create_bucket(new_bucket,location='US')
    else:
        print ("bucket already found: ", new_bucket.name)


    return new_bucket

def retrieve_bucket(bucket_name):
    """
    retrieve a specific storage bucket 
    """   
    my_bucket = storage_client.get_bucket(bucket_name)
    return my_bucket

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
        print("File:%s Successfuly uploaded" % blob_name) 
        return True
    except Exception as e:
        print("error: ", e)
        return False




def download_bucket_file(blob_name, file_path, target_bucket_name):
    """
    Download target files in the bucket
    """
    try:
        bucket = storage_client.get_bucket(target_bucket_name)
        blob = bucket.blob(blob_name)
        with open(file_path, 'wb') as f:
            storage_client.download_blob_to_file(blob, f)
        print("File:%s Successfuly downloaded" % blob_name)
        return True
    except Exception as e:
        print('download_bucket_file error:\n',e)
        return False




if __name__ == "__main__":
    storage_key_file = os.listdir('keys/cloud_storage1')[0]

    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'keys/cloud_storage1/' + storage_key_file

    storage_client = storage.Client()

    bucket_name = 'tut1_data_bucket'
    createBucket(bucket_name)
    my_bucket = retrieve_bucket(bucket_name)


    # file_path = r'C:/Users/daniel.bowden/PycharmProjects/GoogleCloudStorage/data_to_upload'
    file_path = os.getcwd() + '/data_to_upload/'
    file_name = 'voice_list.csv'
    upload_to_bucket('Voice List JJ1', os.path.join(file_path, file_name).replace("\\","/"), bucket_name)
    upload_to_bucket('document/Voice List JJ2', os.path.join(file_path, file_name).replace("\\","/"), bucket_name)

    download_bucket_file('Voice List JJ1', os.path.join(os.getcwd(), 'data_downloaded', 'file1.csv'), bucket_name)
    download_bucket_file('document/Voice List JJ2', os.path.join(os.getcwd(), 'data_downloaded', 'file2.csv'), bucket_name)