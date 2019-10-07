import os, re

class ManagerFiles:


    def __init__(self, bindPath):
        self.bindPath = bindPath
        self.zonesFiles = []

    def getZonesFIles(self):
        namedConfLocal = ""

        for file in os.listdir(self.bindPath):
            if file == "named.conf.local":
                if os.path.isfile(self.bindPath + "/" + file):
                    namedConfLocal = self.bindPath + "/" + file

        namedFile = open(namedConfLocal, "r")
        lines = namedFile.read()
        namedFile.close()

        self.zonesFiles.append(re.findall('zone "(.*?)" {', lines))

        return self.zonesFiles

    