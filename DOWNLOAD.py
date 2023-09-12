import boto3

def get_csv_from_s3 (bucket_name , s3_key , file_name):
            s3 = boto3.client("s3")
            try :
                s3.download_file(bucket_name , s3_key , file_name)
                print("FILE DOWNLOADED SUCCESSFULLY FROM S3")
            except Exception as e:
                print("AN ERROR OCCURRED : {str(e)}")


# SPECIFY THE BUCKET NAME , S3 KEY , AND LOCAL FILE PATH TO SAVE THE DOWNLOAD FILE .

bucket_name = "first-bucket-1kinjal"
file_name = "FIRST_DOWNLOAD.py"
s3_key = "data02.py"

get_csv_from_s3 (bucket_name , s3_key , file_name)