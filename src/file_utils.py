import fnmatch
from config.constants import DIR_PATH, FILE_TYPE
import os


class FilesToLoad():

    list = []

    def __init__(self):
        files_to_load = self._get_files_to_load()
        self.list = files_to_load
        

    def _get_files_to_load(self):
        files_from_path = self._read_files_from_path()
        files_to_load = []   
        for name in files_from_path:                             
                clean_filename = self._get_clean_filenames(name)                
                file_to_load = {
                    'filename': clean_filename['filename'], 
                    'destination_filename': clean_filename['destination_filename']
                }
                files_to_load.append(file_to_load)                   
                    
        return files_to_load

    def _get_clean_filenames(self, filename_to_clean):
        clean_filename_destination = filename_to_clean.replace(DIR_PATH, '')
        filename = filename_to_clean.replace(os.sep, '/')
        destination_filename = clean_filename_destination.replace(os.sep, '/')

        return {
            'filename': filename,
            'destination_filename': destination_filename
        }


    def _is_valid_file(self, name):        
        if fnmatch.fnmatch(name, '*.' + FILE_TYPE):
            return True
        return False                


    def _read_files_from_path(self):
        files_from_path = []
        for root, _, files in os.walk(DIR_PATH, topdown=False):
            for name in files:
                if self._is_valid_file(name):
                    files_from_path.append(os.path.join(root, name))
        return files_from_path
            


