from zipfile import ZipFile

class BBSubmission:
    """ Early version of processing submission from Blackboard"""
    
    def __init__(self, zipfile):
        """ Store zipfile, already opened for reading """
        self.archive = zipfile
        
    def findFile(self, target_file):
        """ search if desired file is found inthe archive """
        return target_file in self.archive.namelist()

    def getFile(self, target_file):
        """ extract desired file from zipfile """
        if not self.findFile(target_file):
            raise FileNotFoundError
        self.archive.extract(target_file)

    def testSubmission(self, test_file, src_files, result_file):
        """ test the submission """
        self.getFile(test_file)
        for src_file in src_files:
            self.getFile(src_file)
        self.runTest(test_file)


