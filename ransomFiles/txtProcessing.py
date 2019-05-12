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

      for familyMalware in self.processedFiles:
          familyMalware = familyMalware.replace('RansomNoteFiles-master', '')
          print(familyMalware)
