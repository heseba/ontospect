from django.shortcuts import render
from django.shortcuts import HttpResponse
import os
import ontospy
from ontospect.extractor.sensor_extractor import SensorExtractor
from ontospect.extractor.actuator_extractor import ActuatorExtractor
from ontospect.extractor.rule_extractor import RuleExtractor
from ontospect.transform.transform import Transfromer
import json
from antlr4 import *
from ontospect.ruleml_parser.RULEMLParser import RULEMLParser
from ontospect.ruleml_parser.RULEMLLexer import RULEMLLexer
from ontospect.verbalizer.ruleml_verbalizer import RULEMLVerbalizer
import shutil


# Create your views here.
# @csrf_exempt
def index(request):
    return render(request, 'index.html')

def extractors(request):
    onto = request.POST.get('onto_url')
    uniqueid = request.POST.get('uid')
    print(onto)
    model = ontospy.Ontospy(onto, verbose=True)
    sensor_ssn = SensorExtractor(model).get_ssn_sensors()
    sensor_sosa = SensorExtractor(model).get_sosa_sensors()
    sensor_diy = SensorExtractor(model).get_diy_sensors(sensor_ssn, sensor_sosa)
    actuator_sosa = ActuatorExtractor(model).get_sosa_actuators()
    actuator_diy = ActuatorExtractor(model).get_diy_actuators(actuator_sosa)
    sensor_ssn_result = iri_post_process(sensor_ssn)
    sensor_sosa_result = iri_post_process(sensor_sosa)
    sensor_diy_result = iri_post_process(sensor_diy)
    actuator_sosa_result = iri_post_process(actuator_sosa)
    actuator_diy_result = iri_post_process(actuator_diy)
    RuleExtractor(model).start(uniqueid)
    response = HttpResponse()
    response['Content-Type'] = "application/json"
    response.write(json.dumps({'sensorSSN':sensor_ssn_result, 'sensorSOSA':sensor_sosa_result, 'sensorDIY':sensor_diy_result, 'actuatorSOSA':actuator_sosa_result, 'actuatorDIY':actuator_diy_result}))
    return response
# @csrf_exempt
def getFileList(request):
    uniqueid = request.POST.get('uid')
    Transfromer().transform(uniqueid)
    path = r"ontospect/data/transformed/" + uniqueid + "/"
    files = os.listdir(path)
    return HttpResponse(json.dumps(files), content_type='application/json')

def verbalize(request):
    uniqueid = request.POST.get('uid')
    path = r"ontospect/data/transformed/" + uniqueid + "/"
    file = request.POST.get('filename')
    input = FileStream(path + file, encoding='utf-8')
    lexer = RULEMLLexer(input)
    stream = CommonTokenStream(lexer)
    parser = RULEMLParser(stream)
    tree = parser.ruleMLDoc()
    visitor = RULEMLVerbalizer()
    visitor.visit(tree)
    entry = visitor.atom_slasher()
    return HttpResponse(json.dumps(entry), content_type='application/json')

# @csrf_exempt
def upload(request):
    if request.method == "POST":
        file_obj = request.FILES.get('file')
        uniqueid = request.POST.get('uid')
        print("upload name：", file_obj.name)
        print("upload size：", file_obj.size)
        # shutil.rmtree(r'ontospect/data/upload/' + uniqueid + '/', ignore_errors=True)
        os.mkdir(r'ontospect/data/upload/'+ uniqueid + '/')
        filepath = os.path.join(r"ontospect/data/upload/" + uniqueid + "/", file_obj.name)
        f = open(filepath, 'wb')
        for line in file_obj.chunks():
            f.write(line)
        f.close()
        return HttpResponse(json.dumps(filepath), content_type='application/json')

def clean_temp_files(request):
    uniqueid = request.POST.get('uid')
    uploadpath = r'ontospect/data/upload/' + uniqueid
    if os.path.exists(uploadpath):
        shutil.rmtree(uploadpath)
    preprocesspath = r'ontospect/data/preprocessed/' + uniqueid
    if os.path.exists(preprocesspath):
        shutil.rmtree(preprocesspath)
    transformpath = r'ontospect/data/transformed/' + uniqueid
    if os.path.exists(transformpath):
        shutil.rmtree(transformpath)
    return HttpResponse("Done")

def iri_post_process(list):
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