import re

class SensorExtractor:
    def __init__(self, model):
        print('Sensor Extraction start....')
        self.model = model
    def get_ssn_sensors(self):
        ssnsensor = set(self.model.get_class('ssn')) & (set(self.model.get_class('SensingDevice')) | set(self.model.get_class('Sensor')))
        sensor_ssn = []
        if ssnsensor:
            sensor_ssn = self.get_leaf(ssnsensor)
            sensor_ssn = set(sensor_ssn)
        if len(sensor_ssn) > 0:
            print('Identified ' + str(len(sensor_ssn)) + ' SSN standard Sensors')
            # get name and iri
            # self.iri_post_process(sensor_ssn)
        else:
            print('There is no SSN standard Sensor')
        return sensor_ssn

    def get_sosa_sensors(self):
        sosa = set(self.model.get_class('sosa')) & set(self.model.get_class('Sensor'))
        sensor_sosa = []
        if sosa:
            sensor_sosa = self.get_leaf(sosa)
            # remove duplicates
            sensor_sosa = set(sensor_sosa)
        if len(sensor_sosa) > 0:
            print('Identified', '' + str(len(sensor_sosa)) + '', 'SOSA standard sensors:')
            # get name and iri
            # self.iri_post_process(sensor_sosa)
        else:
            print('There is no SOSA standard sensor.')
        return sensor_sosa

    def get_diy_sensors(self, sensor_ssn, sensor_sosa):
        sensor = []
        sensor_diy = []
        allclass = self.model.all_classes
        # retrieve the name of all classes and match with keyword
        for i in range(len(allclass)):
            classstring = str(allclass[i])
            iri = classstring.split("*")[1]
            if len(iri.split('#')) > 1:
                name = iri.split('#')[-1]
            else:
                name = iri.split('/')[-1]
            if re.search('sensor', name, re.IGNORECASE) or re.search('sensingDevice', name, re.IGNORECASE):
                sensor.append(allclass[i])
        if sensor:
            sensor_diy = self.get_leaf(sensor)
            sensor_diy = set(sensor_diy) - set(sensor_ssn) - set(sensor_sosa)
        if len(sensor_diy) > 0:
            print('Identified', '' + str(len(sensor_diy)) + '', 'sensors defined by the author:')
            # self.iri_post_process(sensor_diy)
        else:
            print('There is no sensor defined by the author')
        return sensor_diy

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
        sensor_ssn = self.get_ssn_sensors()
        sensor_sosa = self.get_sosa_sensors()
        self.get_diy_sensors(sensor_ssn, sensor_sosa)