from txtProcessing import FileTxtProcessing
from utils import Util
from htmlProcessing import Htmlprocessing
from htaProcessing import HtaProcessing


myUtil = Util()
myUtil.extract_zipfile()


listFiles = myUtil.iterateDirectories()
listFilesText, listFilesHtml, listFilesHta, listExtension = myUtil.group_file_extension(listFiles)
mytxtProcessing = FileTxtProcessing(listFilesText)
filestxtProcessed = mytxtProcessing.processTxtFiles()       
mytxtProcessing = FileTxtProcessing(None, filestxtProcessed)
mydictemailtxt, mydicturltxt, mydictemaildomaintxt =  mytxtProcessing.iterateTextLists()
print(mydictemailtxt)
print(mydicturltxt)
print(mydictemaildomaintxt)


myhtmlProcessing = Htmlprocessing(listFilesHtml, None, None)
fileshtmlProcessedURL, fileshtmlProcessedEmails  = myhtmlProcessing.processHtmlFiles()
myhtmlProcessing = Htmlprocessing(None, fileshtmlProcessedURL, None)
mydicturlhtml = myhtmlProcessing.iterateHtmlLists()
#print(mydicturlhtml)
myhtmlProcessing = Htmlprocessing(None, None, fileshtmlProcessedEmails)
mydictemailhtml, mydictemaildomaintxt = myhtmlProcessing.iterateEmailList()
#print(mydictemailhtml)
#print(mydictemaildomaintxt)

myhtaprocessing = HtaProcessing(listFilesHta)
htaFileProcessing, emailHta = myhtaprocessing.process_hta_files()
myhtaprocessing = HtaProcessing(None, htaFileProcessing, None)
mydicturlhta = myhtaprocessing.iterateHtalLists()
#print(mydicturlhta)
myhtaProcessing = HtaProcessing(None, None, emailHta)
mydictemailhta, mydictemaildomainhta = myhtaProcessing.iterateEmailList()
#print(mydictemailhta)
#print(mydictemaildomainhta)
