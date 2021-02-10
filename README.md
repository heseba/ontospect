# OntoSpect
OntoSpect allows extracting `sensors`, `actuators`, and `rules` from Web of Things ontologies. It is part of our research on Web of Things ([GrOWTH](https://vsr.informatik.tu-chemnitz.de/projects/2019/growth/))[1] and is currently submitted for review to the [International Conference on Web Engineering (ICWE 2021)](https://icwe2021.webengineering.org/).

One of the main challenges in the Internet of Things (IoT) is the lack of semantic interoperability between heterogeneous sources. In the Semantic Web domain, ontologies are one way to achieve semantic interoperability by using a common vocabulary that represents heterogeneous sources. However, recent studies have shown that the amount of concept reuse from existing IoT ontologies is low. As the number of IoT ontologies increases, encouraging users to reuse existing ontologies instead of creating new concepts becomes important. Ontology catalogues are a prominent approach to discover and inspect existing ontologies for reuse. However, such catalogues inspect the ontologies using general criteria which is not enough to understand the content of the ontology. In this paper, we propose a method for automatic ontology inspection (OntoSpect) of IoT ontologies from different application domains based on a generic set of content-related concepts. OntoSpect consists of two main steps: first it extracts the set of IoT concepts, and then generates human-understandable descriptions using a Model-driven Engineering (MDE) approach. We evaluate the quality of concept extraction and natural language description generation with 84 ontologies retrieved from the LOV4IoT catalogue and report on quality metrics. In addition, we conduct an empirical study with 28 ontology users to further assess the quality of the generated descriptions. The results demonstrate the capability of OntoSpect to support ontology users inspecting IoT ontologies.


## Development Environment: 
Python 3.7.3 + Win10 64bit + Firefox + JDK1.8.0_261


## To Run this project locally:
* Install the python environment with correct version

* Install a JRE version higher than 1.8.0_261 (JAVA8)

* Enter the "ontoproject" directory:
```cd ontoproject```

* Install required packages using pip:
```pip instal requirements.txt```
* Run Django's local server:
```python manage.py runserver```
* Open the address printed in terminal, by default: ```http://127.0.0.1:8000/ontospect/```

## Recommended Browser:
This project can now running on `Firefox`, `Chrome`, `Microsoft Edge`, and `Safari`.
We strongly recommend to use `Firefox` to get the best experience.

## References
If you want to use or extend our toolchain, please consider citing the related publications:

[1] Noura M., Heil S., Gaedke M. (2018) GrOWTH: Goal-Oriented End User Development for Web of Things Devices. In: Mikkonen T., Klamma R., Hernández J. (eds) Web Engineering. ICWE 2018. Lecture Notes in Computer Science, vol 10845. Springer, Cham
