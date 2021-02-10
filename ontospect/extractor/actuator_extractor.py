import re

class ActuatorExtractor:
    def __init__(self, model):
        print('Actuator Extraction start....')
        self.model = model

    def get_sosa_actuators(self):
        sosa = set(self.model.get_class('sosa')) & set(self.model.get_class('Actuator'))
        actuator_sosa = []
        if sosa:
            actuator_sosa = self.get_leaf(sosa)
            actuator_sosa = set(actuator_sosa)
        if len(actuator_sosa) > 0:
            print('Identified', '' + str(len(actuator_sosa)) + '', 'SOSA standard actuators:')
            # self.iri_post_process(actuator_sosa)
        else:
            print('There is no SOSA standard actuator.')
        return actuator_sosa

    def get_diy_actuators(self, actuator_sosa):
        actuator = []
        actuator_diy = []
        allclass = self.model.all_classes
        # retrieve the name of all classes and match with keyword
        for i in range(len(allclass)):
            classstring = str(allclass[i])
            iri = classstring.split("*")[1]
            if len(iri.split('#')) > 1:
                name = iri.split('#')[-1]
            else:
                name = iri.split('/')[-1]
            if re.search('actuat', name, re.IGNORECASE):
                actuator.append(allclass[i])
        if actuator:
            actuator_diy = self.get_leaf(actuator)
            actuator_diy = set(actuator_diy) - set(actuator_sosa)
        if len(actuator_diy) > 0:
            print('Identified', '' + str(len(actuator_diy)) + '', 'actuators defined by the author:')
            # self.iri_post_process(actuator_diy)
        else:
            print('There is no actuator defined by the author')
        return actuator_diy

    # traverse a class tree to get leaf
    def get_leaf(self, treelist):
        result = []
        def _get_leaf(treelist):
            for i in treelist:
                if i.descendants():
                    _get_leaf(i.descendants())
                else:
                    result.append(i)
        _get_leaf(treelist)
        return result

    def iri_post_process(self, list):
        output = []
        for i in list:
            item = str(i)
            iri = item.split("*")[1]
            if len(iri.split('#')) > 1:
                name = iri.split('#')[-1]
            else:
                name = iri.split('/')[-1]
            output_item = [name, iri]
            output.append(output_item)
            # print(name)
        print(output)
        return output



    def start(self):
        actuator_sosa = self.get_sosa_actuators()
        actuator_diy = self.get_diy_actuators(actuator_sosa)
