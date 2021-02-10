import os
import jpype
import shutil
from jpype import *

class Transfromer:
    def __init__(self):
        print('Transform start....')

    def makeDirectory(self):
        shutil.rmtree(r'ontospect/data/transformed', ignore_errors=True)
        os.mkdir(r'ontospect/data/transformed')

    def transform(self, uniqueid):
        # self.makeDirectory()
        os.mkdir(r'ontospect/data/transformed/' + uniqueid)
        if not jpype.isJVMStarted():
            startJVM(getDefaultJVMPath(), "-ea",
                    "-Djava.class.path=%s" % (os.getcwd() + "/ontospect/transform/TransformToRuleML.jar"), convertStrings=False)
        JDClass = JClass("TransformToRuleML")
        JDClass.main([uniqueid])