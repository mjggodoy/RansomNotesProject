import AdvancedHTMLParser
import re
from utils import Util

class HtaProcessing:

    def __init__(self, listFilesHta=None, htaFileProcessing=None, emailHta=None):

        if listFilesHta is None:
            self.listFilesHta = []
        else:
            self.listFilesHta = listFilesHta

        if htaFileProcessing is None:
            self.htaFileProcessing = []
        else:
            self.htaFileProcessing = htaFileProcessing

        if emailHta is None:
            self.emailHta = []
        else:
            self.emailHta = emailHta

        self.util = Util

    def extract_url(self, htaFile, listWithUrls):

        count = len(listWithUrls) - 1
        urlList = []
        for item in listWithUrls:
            for item2 in listWithUrls[count]:
                item2 = str(item2)
                url = re.findall("(?P<url>https?://[^\s]+)", item2)
                if url:
                    url = self.fixing_url(url)
                    urlList.append(self.util.handle_path(htaFile) + '  ' + url)
            count -= 1

        return urlList


    @staticmethod
    def fixing_url(url):

        fixedurl = ''
        for item in url:
            item = str(item).split(',')
            for item2 in item:
                if '</a>' in item2:
                    item = item.remove(item2)
                else:
                    item2 = item2.replace(']', '')
                    item2 = item2.replace('[', '')
                    item2 = item2.replace('"', '')
                    fixedurl = item2

        return fixedurl


    def process_hta_files(self):

        listWithUrls = []
        listFinal = []
        emailList = []

        for htaFile in self.listFilesHta:
            parser = AdvancedHTMLParser.AdvancedHTMLParser()
            parser.parseFile(htaFile)
            linkfromTagName = parser.getElementsByTagName('a')
            listWithUrls.append(linkfromTagName)
            listFinal.append(self.extract_url(htaFile, listWithUrls))
            emailList.append(self.util.processemaillLine(htaFile))

        return listFinal, emailList

    def iterateHtalLists(self):
        mydicturl = {}
        for familyMalware in self.htaFileProcessing:
            for element in familyMalware:
                element = element.replace('RansomNoteFiles-master', '')
                element = element.split('  ')
                element = list(filter(None, element))
                for item in element:
                    item = str(item).strip()
                    if 'http' in item:
                        if item in mydicturl:
                            mydicturl[item] +=1
                        else:
                            mydicturl[item] =1
        return mydicturl

    def iterateEmailList(self):

        mydictemail = {}
        myemaildomain = {}
        emailProcessedemails = list(filter(None, self.emailHta))
        for element in emailProcessedemails:
            for element2 in element:
                element2 = str(element2).split(' ')
                for item in element2:
                    item = item.strip().replace('\'', '')
                    if '@' in item:
                        if item in mydictemail:
                            mydictemail[item] +=1
                        else:
                            mydictemail[item] =1

                        emaildomain = str(item).rsplit('@', 1)[1]

                        if emaildomain in myemaildomain:
                            myemaildomain[emaildomain] += 1
                        else:
                            myemaildomain[emaildomain] = 1

        return mydictemail, myemaildomain





