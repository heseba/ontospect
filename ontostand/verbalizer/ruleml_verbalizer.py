from ontostand.ruleml_parser.RULEMLParser import RULEMLParser
from ontostand.ruleml_parser.RULEMLParserVisitor import RULEMLParserVisitor
import re
import wordninja

class RULEMLVerbalizer(RULEMLParserVisitor):
    def __init__(self):
        self.triples = []
        self.NL = []
        self.nodeid = re.compile(r'^N\d{5}$')
        self.equivalentclass = re.compile('owl:equivalentClass')
        self.subclassof = re.compile('rdfs:subClassOf')
        self.intersectionof = re.compile('owl:intersectionOf')
        self.somevaluesfrom  = re.compile('owl:someValuesFrom')
        self.allvaluesfrom = re.compile('owl:allValuesFrom')
        self.unionof = re.compile('owl:unionOf')
        self.onproperty = re.compile('owl:onProperty')
        self.hasvalue = re.compile('owl:hasValue')
        self.hasself = re.compile('owl:hasSelf')
        self.minexclusive = re.compile('xsd:minExclusive')
        self.maxexclusive = re.compile('xsd:maxExclusive')
        self.maxinclusive = re.compile('xsd:maxInclusive')
        self.mininclusive = re.compile('xsd:minInclusive')
        self.mincardinality = re.compile('owl:minCardinality')
        self.maxcardinality = re.compile('owl:maxCardinality')
        self.complementof = re.compile('owl:complementOf')
        self.oneof = re.compile('owl:oneOf')
        self.exactcardinality = re.compile('owl:cardinality')
        self.owlqc = re.compile('owl:qualifiedCardinality')
        self.maxqc = re.compile('owl:maxQualifiedCardinality')
        self.minqc = re.compile('owl:minQualifiedCardinality')
        self.minlength = re.compile('xsd:minLength')
        self.maxlength = re.compile('xsd:maxLength')
        self.disjointwith = re.compile('owl:disjointWith')
        self.inverseof = re.compile('owl:inverseOf')
        self.onclass = re.compile('owl:onClass')
        self.ondatarange = re.compile('owl:onDataRange')

    def visitAtom(self, ctx:RULEMLParser.AtomContext):
        # collect triples except ignored atoms
        predicate = self.visitPredicate(ctx.predicate())
        subject = self.visitSubject(ctx.subject())
        objekt = self.visitObjekt(ctx.objekt())
        # print('|' + subject.center(30) + '|' + predicate.center(30) + '|' + objekt.center(30))
        triple = [subject, predicate, objekt]
        # adding triples to list
        self.triples.append(triple)

    def visitSubject(self, ctx:RULEMLParser.SubjectContext):
        subject = self.visitSubjectcontent(ctx.subjectcontent())
        return subject

    def visitSubjectcontent(self, ctx:RULEMLParser.SubjectcontentContext):
        if ctx.iri():
            subjectcontent = self.visitIri(ctx.iri())
        elif ctx.nodeid():
            subjectcontent = ctx.nodeid().getText()
        else:
            subjectcontent = ctx.getText()
        return subjectcontent

    def visitIri(self, ctx:RULEMLParser.IriContext):
        if ctx.ifragment():
            ifragment = ctx.ifragment().getText()
            if re.match('^has.*$', ifragment):
                iri = re.sub('^has', "", ifragment)
            else:
                iri = ifragment
        else:
            iri = ctx.getText().split("/")[-1]
        # iriname = self.splitwords(iri)
        return iri

    def splitwords(self, iri):
        words = wordninja.split(iri.lower())
        space = ' '
        entity = space.join(words)
        return entity

    def visitPredicate(self, ctx:RULEMLParser.PredicateContext):
        predicate = ctx.verb().getText()
        return predicate

    def visitObjekt(self, ctx:RULEMLParser.ObjektContext):
        objekt = self.visitObjektcontent(ctx.objektcontent())
        return objekt

    def visitObjektcontent(self, ctx:RULEMLParser.ObjektcontentContext):
        if ctx.iri():
            objektcontent = self.visitIri(ctx.iri())
        elif ctx.xsd():
            objektcontent = self.visitXsd(ctx.xsd())
        else:
            objektcontent = ctx.getText()
        return objektcontent

    def visitXsd(self, ctx:RULEMLParser.XsdContext):
        xsdvalue = ctx.xsdvalue().getText()
        return xsdvalue

    def atom_slasher(self):
        subject_index = []
        axiom = []
        for i in range(len(self.triples)):
            if self.nodeid.match(self.triples[i][0]) is None:
                subject_index.append(i)
        if len(subject_index) == 1:
            atom_list = self.triples[subject_index[0]:]
            axiom.append(atom_list)
        if len(subject_index) > 1:
            for i in range(len(subject_index)):
                if subject_index[i] != subject_index[-1]:
                    atom_list = self.triples[subject_index[i]:subject_index[i+1]]
                    axiom.append(atom_list)
                if subject_index[i] == subject_index[-1]:
                    atom_list = self.triples[subject_index[i]:]
                    axiom.append(atom_list)
        result = self.patternidentifier(axiom)
        return result

    def patternidentifier(self, axiom):
        IFTHEN = []
        BELONGSTO =[]
        DISJOINT = []
        RESULT = []
        for atom_list in axiom:
            # if-then pattern when identified equivalentclass
            if self.nodeid.match(atom_list[0][0]) is None and self.equivalentclass.match(atom_list[0][1]):
                conclusion = atom_list[0][0]
                self.NL.append('IF')
                self.verbalizer(atom_list)
                self.NL.append('THEN it is ' + conclusion + '.')
                IFTHEN = IFTHEN + self.NL
                self.NL.clear()
            # belongs-to pattern when identified subClassOf
            if self.nodeid.match(atom_list[0][0]) is None and self.subclassof.match(atom_list[0][1]):
                subject = atom_list[0][0]
                self.NL.append(subject + ' belongs to')
                self.verbalizer(atom_list)
                self.NL[-1] = self.NL[-1] + '.'
                BELONGSTO = BELONGSTO + self.NL
                self.NL.clear()
            if self.nodeid.match(atom_list[0][0]) is None and self.disjointwith.match(atom_list[0][1]):
                subject = atom_list[0][0]
                self.NL.append(subject + ' is disjoint with')
                self.verbalizer(atom_list)
                self.NL[-1] = self.NL[-1] + '.'
                DISJOINT = DISJOINT + self.NL
                self.NL.clear()
        if IFTHEN:
            RESULT = RESULT + IFTHEN
            if BELONGSTO:
                RESULT = RESULT + BELONGSTO
            if DISJOINT:
                RESULT = RESULT + DISJOINT
            print(' '.join(RESULT))
        return RESULT

    def verbalizer(self, atom_list):
        for i in range(len(atom_list)):
            # -----------------------------------------CONNECTIVE-------------------------------------------------------
            # if a statement whose subject and object are both node id, then it is a connective
            if self.nodeid.match(atom_list[i][0]) and self.nodeid.match(atom_list[i][2]):
                # connective: intersectionof
                if self.intersectionof.match(atom_list[i][1]) and self.nodeid.match(atom_list[i - 1][2]) is None:
                    if self.intersectionof.match(atom_list[i-1][1]) and i==2:
                        pass
                    elif self.intersectionof.match(atom_list[i-1][1]) and self.unionof.match(atom_list[i+1][1]):
                        pass
                    elif self.intersectionof.match(atom_list[i-1][1]) and self.nodeid.match(atom_list[i+1][2]):
                        pass
                    else:
                        self.NL.append('and')
                # connective: somevaluesfrom
                if self.somevaluesfrom.match(atom_list[i][1]):
                    for j in range(len(atom_list)):
                        if self.onproperty.match(atom_list[j][1]) and re.match(atom_list[j][0],atom_list[i][0]):
                            self.NL.append(atom_list[j][2] + ' is')
                            break
                # connective: allvaluesfrom
                if self.allvaluesfrom.match(atom_list[i][1]):
                    for j in range(len(atom_list)):
                        if self.onproperty.match(atom_list[j][1]) and re.match(atom_list[j][0],atom_list[i][0]):
                            self.NL.append('every ' + atom_list[j][2])
                            break
                    for k in range(len(atom_list)):
                        if self.intersectionof.match(atom_list[k][1]) and re.match(atom_list[i][2], atom_list[k][0]):
                            self.NL.append('is')
                            break
                        if self.unionof.match(atom_list[k][1]) and re.match(atom_list[i][2], atom_list[k][0]):
                            self.NL.append('is')
                            break
                # connective: unionof
                if self.unionof.match(atom_list[i][1]) and self.nodeid.match(atom_list[i - 1][2]) is None:
                    self.NL.append('or')
                # connective: complementof
                if self.complementof.match(atom_list[i][1]):
                    self.NL.append('except')
                # connective: oneof
                if self.oneof.match(atom_list[i][1]):
                    self.NL.append('one of')
            # ------------------------------------------MEANINGFUL TRIPLE-----------------------------------------------
            # if a statement whose object is an iri, then it is a meaningful triple
            if self.nodeid.match(atom_list[i][2]) is None:
                # equivalent class
                if self.equivalentclass.match(atom_list[i][1]):
                    self.NL.append(atom_list[i][2])
                # intersection of
                if self.intersectionof.match(atom_list[i][1]) and self.nodeid.match(atom_list[i - 1][2]) is None:
                    self.NL.append('and '+ atom_list[i][2])
                elif self.intersectionof.match(atom_list[i][1]) and self.nodeid.match(atom_list[i - 1][2]):
                    self.NL.append(atom_list[i][2])
                # has value
                if self.hasvalue.match(atom_list[i][1]):
                    for j in range(len(atom_list)):
                        if self.onproperty.match(atom_list[j][1]) and re.match(atom_list[j][0],atom_list[i][0]):
                            self.NL.append(atom_list[j][2] + ' ' + atom_list[i][2])
                            break
                    else:
                        self.NL.append(atom_list[i][2])
                # min exclusive
                if self.minexclusive.match(atom_list[i][1]):
                    self.NL.append('greater than ' + atom_list[i][2])
                # max exclusive
                if self.maxexclusive.match(atom_list[i][1]):
                    self.NL.append('less than ' + atom_list[i][2])
                # max inclusive
                if self.maxinclusive.match(atom_list[i][1]):
                    self.NL.append('not greater than ' + atom_list[i][2])
                # min inclusive
                if self.mininclusive.match(atom_list[i][1]):
                    self.NL.append('not less than ' + atom_list[i][2])
                # min length
                if self.minlength.match(atom_list[i][1]):
                    for j in range(len(atom_list)):
                        if self.onproperty.match(atom_list[j][1]) and re.match(atom_list[j][0], atom_list[i][0]):
                            self.NL.append(atom_list[j][2] + ' length is at least ' + atom_list[i][2])
                            break
                    else:
                        self.NL.append('length is at least ' + atom_list[i][2])
                # max length
                if self.maxlength.match(atom_list[i][1]):
                    for j in range(len(atom_list)):
                        if self.onproperty.match(atom_list[j][1]) and re.match(atom_list[j][0], atom_list[i][0]):
                            self.NL.append(atom_list[j][2] + ' length is at most ' + atom_list[i][2])
                            break
                    else:
                        self.NL.append('length is at most ' + atom_list[i][2])
                # some values from
                if self.somevaluesfrom.match(atom_list[i][1]):
                    for j in range(len(atom_list)):
                        if self.onproperty.match(atom_list[j][1]) and re.match(atom_list[j][0], atom_list[i][0]):
                            self.NL.append(atom_list[j][2] + ' is ' + atom_list[i][2])
                            break
                    else:
                        self.NL.append('is ' + atom_list[i][2])
                # all values from
                if self.allvaluesfrom.match(atom_list[i][1]):
                    for j in range(len(atom_list)):
                        if self.onproperty.match(atom_list[j][1]) and re.match(atom_list[j][0], atom_list[i][0]):
                            self.NL.append('every ' + atom_list[j][2] + ' is ' + atom_list[i][2])
                            break
                    else:
                        self.NL.append('is always ' + atom_list[i][2])
                # union of
                if self.unionof.match(atom_list[i][1]) and self.nodeid.match(atom_list[i-1][2]):
                    self.NL.append(atom_list[i][2])
                elif self.unionof.match(atom_list[i][1]) and self.nodeid.match(atom_list[i-1][2]) is None:
                    self.NL.append('or ' + atom_list[i][2])
                # minimum cardinality
                if self.mincardinality.match(atom_list[i][1]):
                    for j in range(len(atom_list)):
                        if self.onproperty.match(atom_list[j][1]) and re.match(atom_list[j][0], atom_list[i][0]):
                            self.NL.append(atom_list[j][2] + ' at least ' + atom_list[i][2])
                            break
                    else:
                        self.NL.append('at least ' + atom_list[i][2])
                # maximum cardinality
                if self.maxcardinality.match(atom_list[i][1]):
                    for j in range(len(atom_list)):
                        if self.onproperty.match(atom_list[j][1]) and re.match(atom_list[j][0], atom_list[i][0]):
                            self.NL.append(atom_list[j][2] + ' at most ' + atom_list[i][2])
                            break
                    else:
                        self.NL.append('at most ' + atom_list[i][2])
                # complement of
                if self.complementof.match(atom_list[i][1]):
                    self.NL.append('except for ' + atom_list[i][2])
                # one of
                if self.oneof.match(atom_list[i][1]):
                    self.NL.append(atom_list[i][2])
                # exact cardinality
                if self.exactcardinality.match(atom_list[i][1]):
                    for j in range(len(atom_list)):
                        if self.onproperty.match(atom_list[j][1]) and re.match(atom_list[j][0], atom_list[i][0]):
                            self.NL.append(atom_list[j][2] + ' exact ' + atom_list[i][2])
                            break
                    else:
                        self.NL.append('exact ' + atom_list[i][2])
                # qualified exact cardinality
                if self.owlqc.match(atom_list[i][1]):
                    for j in range(len(atom_list)):
                        if self.onproperty.match(atom_list[j][1]) and re.match(atom_list[j][0], atom_list[i][0]):
                            for k in range(len(atom_list)):
                                if self.onclass.match(atom_list[k][1]) and re.match(atom_list[k][0], atom_list[i][0]) and self.nodeid.match(atom_list[k][2]) is None:
                                    self.NL.append(atom_list[j][2] + ' exact ' + atom_list[i][2] + ' ' +  atom_list[k][2])
                                    break
                                if self.onclass.match(atom_list[k][1]) and re.match(atom_list[k][0], atom_list[i][0]) and self.nodeid.match(atom_list[k][2]):
                                    self.NL.append(atom_list[j][2] + ' exact ' + atom_list[i][2])
                                    break
                                if self.ondatarange.match(atom_list[k][1]) and re.match(atom_list[k][0], atom_list[i][0]) and self.nodeid.match(atom_list[k][2]) is None:
                                    self.NL.append('exact ' + atom_list[i][2] + ' ' + atom_list[j][2] + '(' + atom_list[k][2] + ')')
                                    break
                                if self.ondatarange.match(atom_list[k][1]) and re.match(atom_list[k][0], atom_list[i][0]) and self.nodeid.match(atom_list[k][2]):
                                    self.NL.append('exact ' + atom_list[i][2] + ' ' + atom_list[j][2])
                                    break
                            else:
                                self.NL.append('exact ' + atom_list[i][2] + ' ' +  atom_list[j][2])
                            break
                    else:
                        self.NL.append('exact ' + atom_list[i][2])
                # maximum qualified cardinality
                if self.maxqc.match(atom_list[i][1]):
                    for j in range(len(atom_list)):
                        if self.onproperty.match(atom_list[j][1]) and re.match(atom_list[j][0], atom_list[i][0]) and self.nodeid.match(atom_list[j][2]) is None:
                            for k in range(len(atom_list)):
                                if self.onclass.match(atom_list[k][1]) and re.match(atom_list[k][0], atom_list[i][0]) and self.nodeid.match(atom_list[k][2]) is None:
                                    self.NL.append(atom_list[j][2] + ' at most ' + atom_list[i][2] + ' '  +  atom_list[k][2])
                                    break
                                if self.onclass.match(atom_list[k][1]) and re.match(atom_list[k][0], atom_list[i][0]) and self.nodeid.match(atom_list[k][2]):
                                    self.NL.append(atom_list[j][2] + ' at most ' + atom_list[i][2])
                                    break
                                if self.ondatarange.match(atom_list[k][1]) and re.match(atom_list[k][0], atom_list[i][0]) and self.nodeid.match(atom_list[k][2]) is None:
                                    self.NL.append('at most ' + atom_list[i][2] + ' ' + atom_list[j][2] + '(' + atom_list[k][2] + ')')
                                    break
                                if self.ondatarange.match(atom_list[k][1]) and re.match(atom_list[k][0], atom_list[i][0]) and self.nodeid.match(atom_list[k][2]):
                                    self.NL.append('at most ' + atom_list[i][2] + ' ' + atom_list[j][2])
                                    break
                            else:
                                self.NL.append('at most ' + atom_list[i][2] + ' ' + atom_list[j][2])
                            break
                        elif self.onproperty.match(atom_list[j][1]) and re.match(atom_list[j][0], atom_list[i][0]) and self.nodeid.match(atom_list[j][2]):
                            for k in range(len(atom_list)):
                                if self.onclass.match(atom_list[k][1]) and re.match(atom_list[k][0], atom_list[i][0]) and self.nodeid.match(atom_list[k][2]) is None:
                                    self.NL.append('at most ' + atom_list[i][2] + ' '  +  atom_list[k][2])
                                    break
                                if self.onclass.match(atom_list[k][1]) and re.match(atom_list[k][0], atom_list[i][0]) and self.nodeid.match(atom_list[k][2]):
                                    self.NL.append('at most ' + atom_list[i][2])
                                    break
                                if self.ondatarange.match(atom_list[k][1]) and re.match(atom_list[k][0], atom_list[i][0]) and self.nodeid.match(atom_list[k][2]) is None:
                                    self.NL.append('at most ' + atom_list[i][2] + '(' + atom_list[k][2] + ')')
                                    break
                                if self.ondatarange.match(atom_list[k][1]) and re.match(atom_list[k][0], atom_list[i][0]) and self.nodeid.match(atom_list[k][2]):
                                    self.NL.append('at most ' + atom_list[i][2])
                                    break
                            else:
                                self.NL.append('at most ' + atom_list[i][2] + ' ' + atom_list[j][2])
                            break
                    else:
                        self.NL.append('at most ' + atom_list[i][2])
                # minimum qualified cardinality
                if self.minqc.match(atom_list[i][1]):
                    for j in range(len(atom_list)):
                        if self.onproperty.match(atom_list[j][1]) and re.match(atom_list[j][0], atom_list[i][0]) and self.nodeid.match(atom_list[j][2]) is None:
                            for k in range(len(atom_list)):
                                if self.onclass.match(atom_list[k][1]) and re.match(atom_list[k][0], atom_list[i][0]) and self.nodeid.match(atom_list[k][2]) is None:
                                    self.NL.append(atom_list[j][2] + ' at least ' + atom_list[i][2] + ' '  +  atom_list[k][2])
                                    break
                                if self.onclass.match(atom_list[k][1]) and re.match(atom_list[k][0], atom_list[i][0]) and self.nodeid.match(atom_list[k][2]):
                                    self.NL.append(atom_list[j][2] + ' at least ' + atom_list[i][2])
                                    break
                                if self.ondatarange.match(atom_list[k][1]) and re.match(atom_list[k][0], atom_list[i][0]) and self.nodeid.match(atom_list[k][2]) is None:
                                    self.NL.append('at least ' + atom_list[i][2] + ' ' + atom_list[j][2] + '(' + atom_list[k][2] + ')')
                                    break
                                if self.ondatarange.match(atom_list[k][1]) and re.match(atom_list[k][0], atom_list[i][0]) and self.nodeid.match(atom_list[k][2]):
                                    self.NL.append('at least ' + atom_list[i][2] + ' ' + atom_list[j][2])
                                    break
                            else:
                                self.NL.append('at least ' + atom_list[i][2] + ' ' + atom_list[j][2])
                            break
                        if self.onproperty.match(atom_list[j][1]) and re.match(atom_list[j][0], atom_list[i][0]) and self.nodeid.match(atom_list[j][2]):
                            for k in range(len(atom_list)):
                                if self.onclass.match(atom_list[k][1]) and re.match(atom_list[k][0], atom_list[i][0]) and self.nodeid.match(atom_list[k][2]) is None:
                                    self.NL.append('at least ' + atom_list[i][2] + ' '  +  atom_list[k][2])
                                    break
                                if self.onclass.match(atom_list[k][1]) and re.match(atom_list[k][0], atom_list[i][0]) and self.nodeid.match(atom_list[k][2]):
                                    self.NL.append('at least ' + atom_list[i][2])
                                    break
                                if self.ondatarange.match(atom_list[k][1]) and re.match(atom_list[k][0], atom_list[i][0]) and self.nodeid.match(atom_list[k][2]) is None:
                                    self.NL.append('at least ' + atom_list[i][2] + '(' + atom_list[k][2] + ')')
                                    break
                                if self.ondatarange.match(atom_list[k][1]) and re.match(atom_list[k][0], atom_list[i][0]) and self.nodeid.match(atom_list[k][2]):
                                    self.NL.append('at least ' + atom_list[i][2])
                                    break
                            else:
                                self.NL.append('at least ' + atom_list[i][2] + ' ' + atom_list[j][2])
                            break
                    else:
                        self.NL.append('at least ' + atom_list[i][2])
                # has self
                if self.hasself.match(atom_list[i][1]):
                    if re.match('true', atom_list[i][2]):
                        for j in range(len(atom_list)):
                            if self.onproperty.match(atom_list[j][1]) and re.match(atom_list[j][0], atom_list[i][0]):
                                self.NL.append(atom_list[j][2] + ' self')
                                break
                        else:
                            self.NL.append('on itself')
                    if re.match('false', atom_list[i][2]):
                        for j in range(len(atom_list)):
                            if self.onproperty.match(atom_list[j][1]) and re.match(atom_list[j][0], atom_list[i][0]):
                                self.NL.append('does not ' + atom_list[j][2] + ' self')
                                break
                        else:
                            self.NL.append('does not on itself')
                # sub class of
                if self.subclassof.match(atom_list[i][1]):
                    self.NL.append(atom_list[i][2])
                # disjoint with
                if self.disjointwith.match(atom_list[i][1]):
                    self.NL.append(atom_list[i][2])
                # inverse of
                if self.inverseof.match(atom_list[i][1]):
                    self.NL.append('is inverse of ' + atom_list[i][2])