from typing import List
from pathlib import Path
import shutil

class parser:
   def __init__(self, extensions):
      #initialize variables
      extensions = []
      extensions:List[str]

   def valid_extension(self, extension):
      if self.extension in self.extensions:
         return self.extension

   def parse (self, path, source, dest):
      self.path:Path
      self.source:Path
      self.dest:Path
      raise NotImplementedError("No Path")

   def read(self, path):
      with open(self.path, 'r') as file:
         return file.read()

   def write(self, path, dest, content):
      ext = ".html"
      full_path = (self.dest / with_suffix(self.path).name / ext

   def copy(self, path, source, dest):
      shutil.copy2(path, dest / path.relative_to(source))


   class ResourceParser:

      extensions = [".jpg", ".png", ".gif", ".css", ".html"]

      def parse (self, path, source, dest):
         self.path:Path
         self.source:Path
         self.dest:Path
         raise NotImplementedError("No Path")
         Parser.copy(self.path, self.source, self.dest)

