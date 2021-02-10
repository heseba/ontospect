import re
import os
import shutil

class RuleExtractor:
    def __init__(self,model):
        print('Rule Extraction start....')
        self.model = model

    def get_all_classes(self, path):
        class_list = self.model.all_classes
        restriction = 'a owl:Restriction'
        class_restriction = []
        for i in range(len(class_list)):
            if isinstance(class_list[i].rdf_source(), str) \
                    and re.search(restriction, class_list[i].rdf_source()) is not None:
                file = open( path + 'class_' + str(i) + '.xml', 'w', encoding='utf-8')
                # print(class_list[i].rdf_source())
                file.write(class_list[i].rdf_source(format='pretty-xml'))
                class_restriction.append(class_list[i].rdf_source())
                file.close()
        print('Identified', '' + str(len(class_restriction)) + '', 'classes who have restrictions.')
        return class_restriction

    def get_all_object_properties(self):
        op_list = self.model.all_properties_object
        restriction = 'a owl:Restriction'
        op_restriction = []
        for i in range(len(op_list)):
            if isinstance(op_list[i].rdf_source(), str) \
                    and re.search(restriction, op_list[i].rdf_source()) is not None:
                file = open(r'ontospect/data/preprocessed/property_' + str(i) + '.xml', 'w', encoding='utf-8')
                # print(op_list[i].rdf_source())
                file.write(op_list[i].rdf_source(format='pretty-xml'))
                op_restriction.append(op_list[i].rdf_source())
                file.close()
        print('Identified', '' + str(len(op_restriction)) + '', 'object properties who have restrictions.')
        return op_restriction

    def start(self,uniqueid):
        # shutil.rmtree(r'ontospect/data/preprocessed')
        os.mkdir(r'ontospect/data/preprocessed/' + uniqueid + '/')
        path = r'ontospect/data/preprocessed/' + uniqueid + '/'
        self.get_all_classes(path)
        # self.get_all_object_properties()
