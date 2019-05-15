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
mytxtProcessing.iterateTextLists()

myhtmlProcessing = Htmlprocessing(listFilesHtml, None, None)
fileshtmlProcessedURL, fileshtmlProcessedEmails  = myhtmlProcessing.processHtmlFiles()
myhtmlProcessing = Htmlprocessing(None, fileshtmlProcessedURL, None)
myhtmlProcessing.iterateHtmlLists()
myhtmlProcessing = Htmlprocessing(None, None, fileshtmlProcessedEmails)
myhtmlProcessing.iterateEmailList()

myhtaprocessing = HtaProcessing(listFilesHta)
htaFileProcessing, emailHta = myhtaprocessing.process_hta_files()
myhtaprocessing = HtaProcessing(None, htaFileProcessing, None)
myhtaprocessing.iterateHtalLists()
myhtaProcessing = Htmlprocessing(None, None, emailHta)
myhtaProcessing.iterateEmailList()
