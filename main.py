from src.google_cloud_utils import GoogleCloudService
from src.file_utils import FilesToLoad

storage_client = GoogleCloudService()

files_to_load = FilesToLoad()

for file in files_to_load.list:
    # print(file)
    storage_client.upload_file(
        origin_filename=file['filename'], 
        destination_filename=file['destination_filename']
    )


print('DONE')

