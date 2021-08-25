from decouple import config

DIR_PATH = config('DIR_PATH')
FILE_TYPE = config('FILE_TYPE')
BUCKET_NAME = config('BUCKET_NAME')
GOOGLE_APPLICATION_CREDENTIALS = './config/' + config('GOOGLE_APPLICATION_CREDENTIALS')
