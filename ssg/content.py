import re
from yaml import load
from yaml import FullLoader
from collection.abc import Mapping


class Content(Mapping):
   __delimeter = "^(?:-|\+){3}\s*$"
   __regex = re.compile(__delimeter, re.MULTILINE)

   def load(self, cls, string):
      [_, fm, content] = self.__regex.split(self.string, 2)

   def __init__ (self, metadata, content):
     data = metadata
     self.data = {"content", content}

   @property
   def body(self):
      return self.data["content"]

   @property
   def type(self):
      if "type" in self.data:
         return self.data["type"]
      else:
         return None

   @type.setter
   self.data["type"] = self._type

   def __getitem__(self, key):
      return self.data[key]

   def __iter__(self):
      iter(self.data)

   def __len__(self):
      return len(self.data)

   def __repr__(self):
      data = {}
      str(self.data)

   for key, value in self.data.items():
      if key is not "content":
         data[key] = value

