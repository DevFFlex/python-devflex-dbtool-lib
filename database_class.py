import os
import json

class Database:

    def __init__(self,filename) -> None:
        self.__path = os.getcwd()
        self.__directoryName = 'Data'
        self.__directoryPath = os.path.join(self.__path,self.__directoryName)
        self.__filename = filename

        self.__datafilePath = os.path.join(self.__directoryPath,self.__filename) + '.json'

        if not self.isDirectory():
            self.__createData()
    

    def __createData(self):
        if not self.isDirectory():
            os.mkdir(self.__directoryPath)
            print(f'create folder "{self.__directoryName}"')

        if self.__filename == None or self.__filename == '':
            return
        
        with open(self.__datafilePath,'w+') as file:
            pass

    def getData(self) -> dict:
        with open(self.__datafilePath,'r') as file:
            if self.isEmptyData():
                return {}
            else:
                return json.load(file)

    def isDirectory(self):
        return True if os.path.exists(self.__directoryPath) else False
    
    def isEmptyData(self):
        with open(self.__datafilePath,'r') as file:
            if file.read().strip() == '':
                return True
            else:
                return False

    def __save(self,dataOUT : dict):
        with open(self.__datafilePath,'w') as file:
                json.dump(dataOUT,file)

    def appendData(self,dict : dict):
        if self.isEmptyData():
            dictOUT = dict
        else:
            json_data = self.getData()
            json_data.update(dict)
            dictOUT = json_data
        self.__save(dictOUT)

    def removeData(self,key):
        json_obj = self.getData()
        try:
            del json_obj[key]
        except:
            return
        self.__save(json_obj)

    def findData(self,key):
        return key in self.getData() 

