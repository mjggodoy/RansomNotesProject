import zipfile
from pathlib import Path
import re
import constant

class Util:

    @staticmethod
    def extract_zipfile():

        path_compressed_file = constant.PATHCOMPRESSEDFILE
        path_file = constant.PATH
        zip_ref = zipfile.ZipFile(path_compressed_file)
        zip_ref.extractall(path_file)
        zip_ref.close()

    @staticmethod
    def iterateDirectories():

        rootdir = Path(constant.PATH)
        file_list = [f for f in rootdir.glob('**/*') if f.is_file()]
        return file_list

    @staticmethod
    def group_file_extension(file_list):

        listFilesText = []
        listFilesHtml = []
        listFilesHta = []
        listExtension = []
        for file in file_list:
            file = str(file)
            if file.endswith('.txt'):
                listFilesText.append(file)
            elif file.endswith('.html') or file.endswith('.htm'):
                listFilesHtml.append(file)
            elif file.endswith('.hta'):
                listFilesHta.append(file)
            else:
                listExtension.append(file)
        return listFilesText, listFilesHtml, listFilesHta, listExtension

    @staticmethod
    def handle_path(path):

        pathway = Path(path)
        name_variant = ''
        parts = pathway.parts

        if '.txt' in parts[len(parts) - 1] \
            or '.htm' in parts[len(parts) - 1] \
            or '.html' in parts[len(parts) - 1] \
            or '.hta' in parts[len(parts) - 1]:

            name_variant = str(parts[len(parts) - 2]) + ' ' \
                         + str(parts[len(parts) - 3]) \
                         + ' ' + str(parts[len(parts) - 4] + ' ')

        return name_variant

    @staticmethod
    def handle_url(url):

        url = re.findall("(?P<url>https?://[^\s]+)", url)
        url = str(url)
        url = url.replace(']', '')
        url = url.replace('[', '')
        url = url.replace('[removed]', '')
        url = url.replace("\'", '')

        return url
