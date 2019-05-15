import re
from utils import Util

class FileTxtProcessing:

    def __init__(self, listFilesText = None, processedFiles=None):

        if listFilesText is None:
            self.listFilesText = []
        else:
            self.listFilesText = listFilesText

        if processedFiles is None:

            self.processedFiles = []
        else:
            self.processedFiles = processedFiles
        self.util = Util

    def processTxtFiles(self):

        pathway = []

        for path in self.listFilesText:
            with open(path, encoding='latin-1') as f:
                line = f.readline()
                while line:
                    line = str(line)
                    if ('http:' in line):
                        pathway.append(self.util.handle_path(path) + self.util.handle_url(line))
                    if ('@' in line):
                        email = re.findall(r'\b[\w.-]+?@\w+?\.\w+?\b', line)
                        if email:
                            email = str(email).replace('[', '')
                            email = str(email).replace(']', '')
                            pathway.append(self.util.handle_path(path)+ ' ' + str(email))
                    line = f.readline()
        return pathway


    def iterateTextLists(self):

        value = 0
        mydicturl = {}
        mydictemail = {}
        mydictemaildomain= {}

        for familyMalware in self.processedFiles:

            familyMalware = familyMalware.replace('RansomNoteFiles-master', '')
            familyMalware = familyMalware.replace(';', '')
            familyMalware = familyMalware.split(' ')
            familyMalware = list(filter(None, familyMalware))

            for item in familyMalware:
                if '@' in item:

                    if item in mydictemail:
                        mydictemail[item] += 1
                    else:
                        mydictemail[item] = 1
                    emaildomain = str(item).rsplit('@', 1)[1]

                    if emaildomain in mydictemaildomain:
                        mydictemaildomain[emaildomain] += 1
                    else:
                        mydictemaildomain[emaildomain] = 1

                if 'http' in item:
                    if item in mydicturl:
                        mydicturl[item] += 1
                    else:
                        mydicturl[item] = 1

        return mydictemail, mydicturl, mydictemaildomain






