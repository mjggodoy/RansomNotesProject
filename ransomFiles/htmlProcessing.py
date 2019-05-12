import AdvancedHTMLParser
import re
from utils import Util


class htmlprocessing:

        def __init__(self, listFilesHtml=None, fileshtmlProcessedURL=None, fileshtmlProcessedEmails=None):

            if listFilesHtml is None:
                self.listFilesHtml = []
            else:
                self.listFilesHtml = listFilesHtml

            if fileshtmlProcessedURL is None:
                self.fileshtmlProcessedURL = []
            else:
                self.fileshtmlProcessedURL = fileshtmlProcessedURL

            if fileshtmlProcessedEmails is None:
                self.fileshtmlProcessedEmails = []
            else:
                self.fileshtmlProcessedEmails = fileshtmlProcessedEmails

            self.util = Util

        def iterateElementsHtml(self, listLinks, html):

            listProcessedLinksIterate = []
            listProcessedLinks = []

            count = len(listLinks) - 1
            for item in listLinks:
                listProcessedLinksIterate.append(str(listLinks[count]) + '****' + html + '****')
                count -= 1

            for item in listProcessedLinksIterate:
                url = re.findall("(?P<url>https?://[^\s]+)", item)
                url = str(url).strip()
                for url in url.split(','):
                    url = url.replace("[removed]", "")
                    url = url.replace("\"", "")
                    url = url.replace("\')", "")
                    url = url.replace("[", "")
                    url = url.replace("]", "")
                    url.strip()
                    if url:
                        listProcessedLinks.append(self.util.handle_path(html) + '   ' + url)
            return listProcessedLinks

        def processHtmlLine(self, htmlFile):

            emailList = []
            with open(htmlFile, encoding='latin-1') as f:
                line = f.readline()
                while line:
                    line = str(line)
                    if ('@' in line):
                        email = re.findall(r'\b[\w.-]+?@\w+?\.\w+?\b', line)
                        email = str(email).replace('[', "")
                        email = str(email).replace(']', "")
                        if email:
                            emailList.append(email + ' ' + self.util.handle_path(htmlFile))
                    line = f.readline()
            return emailList

        def processHtmlFiles(self):
            listLinks = []
            processedHtmlFiles = []
            emailList = []

            for htmlFile in self.listFilesHtml:
                parser = AdvancedHTMLParser.AdvancedHTMLParser()
                parser.parseFile(htmlFile)
                link2 = parser.getElementsByTagName('a')
                listLinks.append(link2)
                processedHtmlFiles.append(self.iterateElementsHtml(listLinks, htmlFile))
                emailList.append(self.processHtmlLine(htmlFile))
            return processedHtmlFiles, emailList


        def iterateHtmlLists(self):
            count = 0
            for familyMalware in self.fileshtmlProcessedURL:
                for element in self.fileshtmlProcessedURL[count]:
                    print(element.replace('RansomNoteFiles-master', ''))
                count += 1

        def iterateEmailList(self):
            filestxtProcessedemails = list(filter(None, self.fileshtmlProcessedEmails))
            for element in filestxtProcessedemails:
                element = str(element).replace('\"', "").replace('RansomNoteFiles-master', '')
                print(element)
