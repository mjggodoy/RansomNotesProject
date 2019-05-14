import AdvancedHTMLParser
import re
from utils import Util

class HtaProcessing:

    def __init__(self, listFilesHta=None):

        if listFilesHta is None:
            self.listFilesHta = []
        else:
            self.listFilesHta = listFilesHta

    def extract_url(self, htaFile, listWithUrls):

        count = len(listWithUrls) - 1
        urlList = []
        for item in listWithUrls:
            for item2 in listWithUrls[count]:
                item2 = str(item2)
                url = re.findall("(?P<url>https?://[^\s]+)", item2)
                if url:
                    url = self.fixing_url(url)
                    urlList.append(Util.handle_path(htaFile) + '  ' + url)
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
            #print(listFinal)

        print(listFinal)
        return listFinal, emailList





