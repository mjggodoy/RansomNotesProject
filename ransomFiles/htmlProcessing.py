import AdvancedHTMLParser
import re
from utils import Util


class Htmlprocessing:

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
                emailList.append(Util.processemaillLine(htmlFile))

            return processedHtmlFiles, emailList


        def iterateHtmlLists(self):
            mydicturl = {}
            for familyMalware in self.fileshtmlProcessedURL:
                for element in familyMalware:
                    element = element.replace('RansomNoteFiles-master', '')
                    element = element.split(' ')
                    for item in element:
                        if 'http' in item:
                            if item in mydicturl:
                                mydicturl[item] += 1
                            else:
                                mydicturl[item] = 1
            return mydicturl


        def iterateEmailList(self):
            mydictemail = {}
            myemaildomain = {}
            filestxtProcessedemails = list(filter(None, self.fileshtmlProcessedEmails))
            for element in filestxtProcessedemails:
                element = str(element).replace('\"', "").replace('RansomNoteFiles-master', '')
                element = element.split(',')
                element = list(filter(None, element))
                for item in element:
                    item = item.replace(']', '').replace('[','').strip()
                    if '@' in item:
                        item = str(item).rsplit('\'', 1)[0]
                        if item in mydictemail:
                            mydictemail[item] += 1
                        else:
                            mydictemail[item] = 1

                        emaildomain = str(item).rsplit('@', 1)[1]

                        if emaildomain in myemaildomain:
                            myemaildomain[emaildomain] += 1
                        else:
                            myemaildomain[emaildomain] = 1

            return mydictemail, myemaildomain


