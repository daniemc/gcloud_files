
from google.cloud import storage
from google.cloud.storage import bucket
from config.constants import BUCKET_NAME, GOOGLE_APPLICATION_CREDENTIALS

class GoogleCloudService:

    def __init__(self):
        self.storage_client = storage.Client.from_service_account_json(GOOGLE_APPLICATION_CREDENTIALS)


    def _get_bucket(self):
        return self.storage_client.bucket(BUCKET_NAME)


    def upload_file(self, origin_filename, destination_filename):
        bucket = self._get_bucket()
        
        blob = bucket.blob(destination_filename)
        blob.upload_from_filename(origin_filename)
        print(
            "File {} uploaded.".format(origin_filename)
        )
        