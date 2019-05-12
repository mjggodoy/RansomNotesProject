from txtProcessing import FileTxtProcessing
from utils import Util
from htmlProcessing import htmlprocessing


myUtil = Util()
myUtil.extract_zipfile()
listFiles = myUtil.iterateDirectories()
listFilesText, listFilesHtml, listFilesHta, listExtension = myUtil.group_file_extension(listFiles)
mytxtProcessing = FileTxtProcessing(listFilesText)
filestxtProcessed = mytxtProcessing.processTxtFiles()       
mytxtProcessing = FileTxtProcessing(None, filestxtProcessed)
mytxtProcessing.iterateTextLists()

myhtmlProcessing = htmlprocessing(listFilesHtml, None, None)
fileshtmlProcessedURL, fileshtmlProcessedEmails  = myhtmlProcessing.processHtmlFiles()
myhtmlProcessing = htmlprocessing(None, fileshtmlProcessedURL, None)
myhtmlProcessing.iterateHtmlLists()
myhtmlProcessing = htmlprocessing(None, None, fileshtmlProcessedEmails)
myhtmlProcessing.iterateEmailList()
