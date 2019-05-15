from txtProcessing import FileTxtProcessing
from utils import Util
from htmlProcessing import Htmlprocessing
from htaProcessing import HtaProcessing
from utils import Util


myUtil = Util()
myUtil.extract_zipfile()


listFiles = myUtil.iterateDirectories()
listFilesText, listFilesHtml, listFilesHta, listExtension = myUtil.group_file_extension(listFiles)
mytxtProcessing = FileTxtProcessing(listFilesText)
filestxtProcessed = mytxtProcessing.processTxtFiles()       
mytxtProcessing = FileTxtProcessing(None, filestxtProcessed)
mydictemailtxt, mydicturltxt, mydictemaildomaintxt =  mytxtProcessing.iterateTextLists()
#myUtil.iteratedictionary(mydictemailtxt, 'ranking_mail_malwarenotes')
#myUtil.iteratedictionary(mydicturltxt, 'ranking_url_malwarenotes')
#myUtil.iteratedictionary(mydictemaildomaintxt, 'ranking_maildomains_malwarenotes')


myhtmlProcessing = Htmlprocessing(listFilesHtml, None, None)
fileshtmlProcessedURL, fileshtmlProcessedEmails  = myhtmlProcessing.processHtmlFiles()
myhtmlProcessing = Htmlprocessing(None, fileshtmlProcessedURL, None)
mydicturlhtml = myhtmlProcessing.iterateHtmlLists()
#print(mydicturlhtml)
#myUtil.iteratedictionary(mydicturlhtml, 'ranking_url_html_malwarenotes')
myhtmlProcessing = Htmlprocessing(None, None, fileshtmlProcessedEmails)
mydictemailhtml, mydictemaildomaintxt = myhtmlProcessing.iterateEmailList()
#myUtil.iteratedictionary(mydictemailhtml, 'ranking_email_html_malwarenotes')
#print(mydictemaildomaintxt)
#myUtil.iteratedictionary(mydictemaildomaintxt, 'ranking_emaildomain_html_malwarenotes')


myhtaprocessing = HtaProcessing(listFilesHta)
htaFileProcessing, emailHta = myhtaprocessing.process_hta_files()
myhtaprocessing = HtaProcessing(None, htaFileProcessing, None)
mydicturlhta = myhtaprocessing.iterateHtalLists()
#print(mydicturlhta)
#myUtil.iteratedictionary(mydicturlhta, 'ranking_url_hta_malwarenotes')
myhtaProcessing = HtaProcessing(None, None, emailHta)
mydictemailhta, mydictemaildomainhta = myhtaProcessing.iterateEmailList()
#print(mydictemailhta)
#myUtil.iteratedictionary(mydictemailhta, 'ranking_mail_hta_malwarenotes')
#print(mydictemaildomainhta)
#myUtil.iteratedictionary(mydictemaildomainhta, 'ranking_maildomain_hta_malwarenotes')
