# Generated from D:/OneDrive/ontoproject/ontostand/ruleml_parser/ruleml_grammar\RULEMLParser.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .RULEMLParser import RULEMLParser
else:
    from RULEMLParser import RULEMLParser

# This class defines a complete listener for a parse tree produced by RULEMLParser.
class RULEMLParserListener(ParseTreeListener):

    # Enter a parse tree produced by RULEMLParser#ruleMLDoc.
    def enterRuleMLDoc(self, ctx:RULEMLParser.RuleMLDocContext):
        pass

    # Exit a parse tree produced by RULEMLParser#ruleMLDoc.
    def exitRuleMLDoc(self, ctx:RULEMLParser.RuleMLDocContext):
        pass


    # Enter a parse tree produced by RULEMLParser#atom.
    def enterAtom(self, ctx:RULEMLParser.AtomContext):
        pass

    # Exit a parse tree produced by RULEMLParser#atom.
    def exitAtom(self, ctx:RULEMLParser.AtomContext):
        pass


    # Enter a parse tree produced by RULEMLParser#ignoredatom.
    def enterIgnoredatom(self, ctx:RULEMLParser.IgnoredatomContext):
        pass

    # Exit a parse tree produced by RULEMLParser#ignoredatom.
    def exitIgnoredatom(self, ctx:RULEMLParser.IgnoredatomContext):
        pass


    # Enter a parse tree produced by RULEMLParser#statement.
    def enterStatement(self, ctx:RULEMLParser.StatementContext):
        pass

    # Exit a parse tree produced by RULEMLParser#statement.
    def exitStatement(self, ctx:RULEMLParser.StatementContext):
        pass


    # Enter a parse tree produced by RULEMLParser#subject.
    def enterSubject(self, ctx:RULEMLParser.SubjectContext):
        pass

    # Exit a parse tree produced by RULEMLParser#subject.
    def exitSubject(self, ctx:RULEMLParser.SubjectContext):
        pass


    # Enter a parse tree produced by RULEMLParser#predicate.
    def enterPredicate(self, ctx:RULEMLParser.PredicateContext):
        pass

    # Exit a parse tree produced by RULEMLParser#predicate.
    def exitPredicate(self, ctx:RULEMLParser.PredicateContext):
        pass


    # Enter a parse tree produced by RULEMLParser#objekt.
    def enterObjekt(self, ctx:RULEMLParser.ObjektContext):
        pass

    # Exit a parse tree produced by RULEMLParser#objekt.
    def exitObjekt(self, ctx:RULEMLParser.ObjektContext):
        pass


    # Enter a parse tree produced by RULEMLParser#misc.
    def enterMisc(self, ctx:RULEMLParser.MiscContext):
        pass

    # Exit a parse tree produced by RULEMLParser#misc.
    def exitMisc(self, ctx:RULEMLParser.MiscContext):
        pass


    # Enter a parse tree produced by RULEMLParser#ignoredpred.
    def enterIgnoredpred(self, ctx:RULEMLParser.IgnoredpredContext):
        pass

    # Exit a parse tree produced by RULEMLParser#ignoredpred.
    def exitIgnoredpred(self, ctx:RULEMLParser.IgnoredpredContext):
        pass


    # Enter a parse tree produced by RULEMLParser#nodeid.
    def enterNodeid(self, ctx:RULEMLParser.NodeidContext):
        pass

    # Exit a parse tree produced by RULEMLParser#nodeid.
    def exitNodeid(self, ctx:RULEMLParser.NodeidContext):
        pass


    # Enter a parse tree produced by RULEMLParser#subjectcontent.
    def enterSubjectcontent(self, ctx:RULEMLParser.SubjectcontentContext):
        pass

    # Exit a parse tree produced by RULEMLParser#subjectcontent.
    def exitSubjectcontent(self, ctx:RULEMLParser.SubjectcontentContext):
        pass


    # Enter a parse tree produced by RULEMLParser#objektcontent.
    def enterObjektcontent(self, ctx:RULEMLParser.ObjektcontentContext):
        pass

    # Exit a parse tree produced by RULEMLParser#objektcontent.
    def exitObjektcontent(self, ctx:RULEMLParser.ObjektcontentContext):
        pass


    # Enter a parse tree produced by RULEMLParser#ignoredverb.
    def enterIgnoredverb(self, ctx:RULEMLParser.IgnoredverbContext):
        pass

    # Exit a parse tree produced by RULEMLParser#ignoredverb.
    def exitIgnoredverb(self, ctx:RULEMLParser.IgnoredverbContext):
        pass


    # Enter a parse tree produced by RULEMLParser#verb.
    def enterVerb(self, ctx:RULEMLParser.VerbContext):
        pass

    # Exit a parse tree produced by RULEMLParser#verb.
    def exitVerb(self, ctx:RULEMLParser.VerbContext):
        pass


    # Enter a parse tree produced by RULEMLParser#xsd.
    def enterXsd(self, ctx:RULEMLParser.XsdContext):
        pass

    # Exit a parse tree produced by RULEMLParser#xsd.
    def exitXsd(self, ctx:RULEMLParser.XsdContext):
        pass


    # Enter a parse tree produced by RULEMLParser#xsdvalue.
    def enterXsdvalue(self, ctx:RULEMLParser.XsdvalueContext):
        pass

    # Exit a parse tree produced by RULEMLParser#xsdvalue.
    def exitXsdvalue(self, ctx:RULEMLParser.XsdvalueContext):
        pass


    # Enter a parse tree produced by RULEMLParser#xsddatatype.
    def enterXsddatatype(self, ctx:RULEMLParser.XsddatatypeContext):
        pass

    # Exit a parse tree produced by RULEMLParser#xsddatatype.
    def exitXsddatatype(self, ctx:RULEMLParser.XsddatatypeContext):
        pass


    # Enter a parse tree produced by RULEMLParser#unreserved_content.
    def enterUnreserved_content(self, ctx:RULEMLParser.Unreserved_contentContext):
        pass

    # Exit a parse tree produced by RULEMLParser#unreserved_content.
    def exitUnreserved_content(self, ctx:RULEMLParser.Unreserved_contentContext):
        pass


    # Enter a parse tree produced by RULEMLParser#rdfscomment.
    def enterRdfscomment(self, ctx:RULEMLParser.RdfscommentContext):
        pass

    # Exit a parse tree produced by RULEMLParser#rdfscomment.
    def exitRdfscomment(self, ctx:RULEMLParser.RdfscommentContext):
        pass


    # Enter a parse tree produced by RULEMLParser#rdfslabel.
    def enterRdfslabel(self, ctx:RULEMLParser.RdfslabelContext):
        pass

    # Exit a parse tree produced by RULEMLParser#rdfslabel.
    def exitRdfslabel(self, ctx:RULEMLParser.RdfslabelContext):
        pass


    # Enter a parse tree produced by RULEMLParser#dcdescription.
    def enterDcdescription(self, ctx:RULEMLParser.DcdescriptionContext):
        pass

    # Exit a parse tree produced by RULEMLParser#dcdescription.
    def exitDcdescription(self, ctx:RULEMLParser.DcdescriptionContext):
        pass


    # Enter a parse tree produced by RULEMLParser#rdftype.
    def enterRdftype(self, ctx:RULEMLParser.RdftypeContext):
        pass

    # Exit a parse tree produced by RULEMLParser#rdftype.
    def exitRdftype(self, ctx:RULEMLParser.RdftypeContext):
        pass


    # Enter a parse tree produced by RULEMLParser#seealso.
    def enterSeealso(self, ctx:RULEMLParser.SeealsoContext):
        pass

    # Exit a parse tree produced by RULEMLParser#seealso.
    def exitSeealso(self, ctx:RULEMLParser.SeealsoContext):
        pass


    # Enter a parse tree produced by RULEMLParser#rdfrest.
    def enterRdfrest(self, ctx:RULEMLParser.RdfrestContext):
        pass

    # Exit a parse tree produced by RULEMLParser#rdfrest.
    def exitRdfrest(self, ctx:RULEMLParser.RdfrestContext):
        pass


    # Enter a parse tree produced by RULEMLParser#skosdef.
    def enterSkosdef(self, ctx:RULEMLParser.SkosdefContext):
        pass

    # Exit a parse tree produced by RULEMLParser#skosdef.
    def exitSkosdef(self, ctx:RULEMLParser.SkosdefContext):
        pass


    # Enter a parse tree produced by RULEMLParser#skospreflabel.
    def enterSkospreflabel(self, ctx:RULEMLParser.SkospreflabelContext):
        pass

    # Exit a parse tree produced by RULEMLParser#skospreflabel.
    def exitSkospreflabel(self, ctx:RULEMLParser.SkospreflabelContext):
        pass


    # Enter a parse tree produced by RULEMLParser#skosaltlabel.
    def enterSkosaltlabel(self, ctx:RULEMLParser.SkosaltlabelContext):
        pass

    # Exit a parse tree produced by RULEMLParser#skosaltlabel.
    def exitSkosaltlabel(self, ctx:RULEMLParser.SkosaltlabelContext):
        pass


    # Enter a parse tree produced by RULEMLParser#skoshiddenlabel.
    def enterSkoshiddenlabel(self, ctx:RULEMLParser.SkoshiddenlabelContext):
        pass

    # Exit a parse tree produced by RULEMLParser#skoshiddenlabel.
    def exitSkoshiddenlabel(self, ctx:RULEMLParser.SkoshiddenlabelContext):
        pass


    # Enter a parse tree produced by RULEMLParser#skosnotation.
    def enterSkosnotation(self, ctx:RULEMLParser.SkosnotationContext):
        pass

    # Exit a parse tree produced by RULEMLParser#skosnotation.
    def exitSkosnotation(self, ctx:RULEMLParser.SkosnotationContext):
        pass


    # Enter a parse tree produced by RULEMLParser#annotateds.
    def enterAnnotateds(self, ctx:RULEMLParser.AnnotatedsContext):
        pass

    # Exit a parse tree produced by RULEMLParser#annotateds.
    def exitAnnotateds(self, ctx:RULEMLParser.AnnotatedsContext):
        pass


    # Enter a parse tree produced by RULEMLParser#annotatedp.
    def enterAnnotatedp(self, ctx:RULEMLParser.AnnotatedpContext):
        pass

    # Exit a parse tree produced by RULEMLParser#annotatedp.
    def exitAnnotatedp(self, ctx:RULEMLParser.AnnotatedpContext):
        pass


    # Enter a parse tree produced by RULEMLParser#annotatedt.
    def enterAnnotatedt(self, ctx:RULEMLParser.AnnotatedtContext):
        pass

    # Exit a parse tree produced by RULEMLParser#annotatedt.
    def exitAnnotatedt(self, ctx:RULEMLParser.AnnotatedtContext):
        pass


    # Enter a parse tree produced by RULEMLParser#isdefinedby.
    def enterIsdefinedby(self, ctx:RULEMLParser.IsdefinedbyContext):
        pass

    # Exit a parse tree produced by RULEMLParser#isdefinedby.
    def exitIsdefinedby(self, ctx:RULEMLParser.IsdefinedbyContext):
        pass


    # Enter a parse tree produced by RULEMLParser#versioninfo.
    def enterVersioninfo(self, ctx:RULEMLParser.VersioninfoContext):
        pass

    # Exit a parse tree produced by RULEMLParser#versioninfo.
    def exitVersioninfo(self, ctx:RULEMLParser.VersioninfoContext):
        pass


    # Enter a parse tree produced by RULEMLParser#deprecated.
    def enterDeprecated(self, ctx:RULEMLParser.DeprecatedContext):
        pass

    # Exit a parse tree produced by RULEMLParser#deprecated.
    def exitDeprecated(self, ctx:RULEMLParser.DeprecatedContext):
        pass


    # Enter a parse tree produced by RULEMLParser#backcompatwith.
    def enterBackcompatwith(self, ctx:RULEMLParser.BackcompatwithContext):
        pass

    # Exit a parse tree produced by RULEMLParser#backcompatwith.
    def exitBackcompatwith(self, ctx:RULEMLParser.BackcompatwithContext):
        pass


    # Enter a parse tree produced by RULEMLParser#incompatwith.
    def enterIncompatwith(self, ctx:RULEMLParser.IncompatwithContext):
        pass

    # Exit a parse tree produced by RULEMLParser#incompatwith.
    def exitIncompatwith(self, ctx:RULEMLParser.IncompatwithContext):
        pass


    # Enter a parse tree produced by RULEMLParser#priorversion.
    def enterPriorversion(self, ctx:RULEMLParser.PriorversionContext):
        pass

    # Exit a parse tree produced by RULEMLParser#priorversion.
    def exitPriorversion(self, ctx:RULEMLParser.PriorversionContext):
        pass


    # Enter a parse tree produced by RULEMLParser#dcsource.
    def enterDcsource(self, ctx:RULEMLParser.DcsourceContext):
        pass

    # Exit a parse tree produced by RULEMLParser#dcsource.
    def exitDcsource(self, ctx:RULEMLParser.DcsourceContext):
        pass


    # Enter a parse tree produced by RULEMLParser#ondatatype.
    def enterOndatatype(self, ctx:RULEMLParser.OndatatypeContext):
        pass

    # Exit a parse tree produced by RULEMLParser#ondatatype.
    def exitOndatatype(self, ctx:RULEMLParser.OndatatypeContext):
        pass


    # Enter a parse tree produced by RULEMLParser#owlwithrestrictions.
    def enterOwlwithrestrictions(self, ctx:RULEMLParser.OwlwithrestrictionsContext):
        pass

    # Exit a parse tree produced by RULEMLParser#owlwithrestrictions.
    def exitOwlwithrestrictions(self, ctx:RULEMLParser.OwlwithrestrictionsContext):
        pass


    # Enter a parse tree produced by RULEMLParser#subpropertyof.
    def enterSubpropertyof(self, ctx:RULEMLParser.SubpropertyofContext):
        pass

    # Exit a parse tree produced by RULEMLParser#subpropertyof.
    def exitSubpropertyof(self, ctx:RULEMLParser.SubpropertyofContext):
        pass


    # Enter a parse tree produced by RULEMLParser#subclassof.
    def enterSubclassof(self, ctx:RULEMLParser.SubclassofContext):
        pass

    # Exit a parse tree produced by RULEMLParser#subclassof.
    def exitSubclassof(self, ctx:RULEMLParser.SubclassofContext):
        pass


    # Enter a parse tree produced by RULEMLParser#rdfsdomain.
    def enterRdfsdomain(self, ctx:RULEMLParser.RdfsdomainContext):
        pass

    # Exit a parse tree produced by RULEMLParser#rdfsdomain.
    def exitRdfsdomain(self, ctx:RULEMLParser.RdfsdomainContext):
        pass


    # Enter a parse tree produced by RULEMLParser#rdfsrange.
    def enterRdfsrange(self, ctx:RULEMLParser.RdfsrangeContext):
        pass

    # Exit a parse tree produced by RULEMLParser#rdfsrange.
    def exitRdfsrange(self, ctx:RULEMLParser.RdfsrangeContext):
        pass


    # Enter a parse tree produced by RULEMLParser#equiclass.
    def enterEquiclass(self, ctx:RULEMLParser.EquiclassContext):
        pass

    # Exit a parse tree produced by RULEMLParser#equiclass.
    def exitEquiclass(self, ctx:RULEMLParser.EquiclassContext):
        pass


    # Enter a parse tree produced by RULEMLParser#owlclass.
    def enterOwlclass(self, ctx:RULEMLParser.OwlclassContext):
        pass

    # Exit a parse tree produced by RULEMLParser#owlclass.
    def exitOwlclass(self, ctx:RULEMLParser.OwlclassContext):
        pass


    # Enter a parse tree produced by RULEMLParser#rdfdescription.
    def enterRdfdescription(self, ctx:RULEMLParser.RdfdescriptionContext):
        pass

    # Exit a parse tree produced by RULEMLParser#rdfdescription.
    def exitRdfdescription(self, ctx:RULEMLParser.RdfdescriptionContext):
        pass


    # Enter a parse tree produced by RULEMLParser#intersectionof.
    def enterIntersectionof(self, ctx:RULEMLParser.IntersectionofContext):
        pass

    # Exit a parse tree produced by RULEMLParser#intersectionof.
    def exitIntersectionof(self, ctx:RULEMLParser.IntersectionofContext):
        pass


    # Enter a parse tree produced by RULEMLParser#owlsvf.
    def enterOwlsvf(self, ctx:RULEMLParser.OwlsvfContext):
        pass

    # Exit a parse tree produced by RULEMLParser#owlsvf.
    def exitOwlsvf(self, ctx:RULEMLParser.OwlsvfContext):
        pass


    # Enter a parse tree produced by RULEMLParser#owlavf.
    def enterOwlavf(self, ctx:RULEMLParser.OwlavfContext):
        pass

    # Exit a parse tree produced by RULEMLParser#owlavf.
    def exitOwlavf(self, ctx:RULEMLParser.OwlavfContext):
        pass


    # Enter a parse tree produced by RULEMLParser#onproperty.
    def enterOnproperty(self, ctx:RULEMLParser.OnpropertyContext):
        pass

    # Exit a parse tree produced by RULEMLParser#onproperty.
    def exitOnproperty(self, ctx:RULEMLParser.OnpropertyContext):
        pass


    # Enter a parse tree produced by RULEMLParser#hasvalue.
    def enterHasvalue(self, ctx:RULEMLParser.HasvalueContext):
        pass

    # Exit a parse tree produced by RULEMLParser#hasvalue.
    def exitHasvalue(self, ctx:RULEMLParser.HasvalueContext):
        pass


    # Enter a parse tree produced by RULEMLParser#minexclusive.
    def enterMinexclusive(self, ctx:RULEMLParser.MinexclusiveContext):
        pass

    # Exit a parse tree produced by RULEMLParser#minexclusive.
    def exitMinexclusive(self, ctx:RULEMLParser.MinexclusiveContext):
        pass


    # Enter a parse tree produced by RULEMLParser#maxexclusive.
    def enterMaxexclusive(self, ctx:RULEMLParser.MaxexclusiveContext):
        pass

    # Exit a parse tree produced by RULEMLParser#maxexclusive.
    def exitMaxexclusive(self, ctx:RULEMLParser.MaxexclusiveContext):
        pass


    # Enter a parse tree produced by RULEMLParser#owlrestriction.
    def enterOwlrestriction(self, ctx:RULEMLParser.OwlrestrictionContext):
        pass

    # Exit a parse tree produced by RULEMLParser#owlrestriction.
    def exitOwlrestriction(self, ctx:RULEMLParser.OwlrestrictionContext):
        pass


    # Enter a parse tree produced by RULEMLParser#rdfsdatatype.
    def enterRdfsdatatype(self, ctx:RULEMLParser.RdfsdatatypeContext):
        pass

    # Exit a parse tree produced by RULEMLParser#rdfsdatatype.
    def exitRdfsdatatype(self, ctx:RULEMLParser.RdfsdatatypeContext):
        pass


    # Enter a parse tree produced by RULEMLParser#funcproperty.
    def enterFuncproperty(self, ctx:RULEMLParser.FuncpropertyContext):
        pass

    # Exit a parse tree produced by RULEMLParser#funcproperty.
    def exitFuncproperty(self, ctx:RULEMLParser.FuncpropertyContext):
        pass


    # Enter a parse tree produced by RULEMLParser#owlondatarange.
    def enterOwlondatarange(self, ctx:RULEMLParser.OwlondatarangeContext):
        pass

    # Exit a parse tree produced by RULEMLParser#owlondatarange.
    def exitOwlondatarange(self, ctx:RULEMLParser.OwlondatarangeContext):
        pass


    # Enter a parse tree produced by RULEMLParser#owlonclass.
    def enterOwlonclass(self, ctx:RULEMLParser.OwlonclassContext):
        pass

    # Exit a parse tree produced by RULEMLParser#owlonclass.
    def exitOwlonclass(self, ctx:RULEMLParser.OwlonclassContext):
        pass


    # Enter a parse tree produced by RULEMLParser#owlqc.
    def enterOwlqc(self, ctx:RULEMLParser.OwlqcContext):
        pass

    # Exit a parse tree produced by RULEMLParser#owlqc.
    def exitOwlqc(self, ctx:RULEMLParser.OwlqcContext):
        pass


    # Enter a parse tree produced by RULEMLParser#objectproperty.
    def enterObjectproperty(self, ctx:RULEMLParser.ObjectpropertyContext):
        pass

    # Exit a parse tree produced by RULEMLParser#objectproperty.
    def exitObjectproperty(self, ctx:RULEMLParser.ObjectpropertyContext):
        pass


    # Enter a parse tree produced by RULEMLParser#rdfnil.
    def enterRdfnil(self, ctx:RULEMLParser.RdfnilContext):
        pass

    # Exit a parse tree produced by RULEMLParser#rdfnil.
    def exitRdfnil(self, ctx:RULEMLParser.RdfnilContext):
        pass


    # Enter a parse tree produced by RULEMLParser#unionof.
    def enterUnionof(self, ctx:RULEMLParser.UnionofContext):
        pass

    # Exit a parse tree produced by RULEMLParser#unionof.
    def exitUnionof(self, ctx:RULEMLParser.UnionofContext):
        pass


    # Enter a parse tree produced by RULEMLParser#cardinality.
    def enterCardinality(self, ctx:RULEMLParser.CardinalityContext):
        pass

    # Exit a parse tree produced by RULEMLParser#cardinality.
    def exitCardinality(self, ctx:RULEMLParser.CardinalityContext):
        pass


    # Enter a parse tree produced by RULEMLParser#hasself.
    def enterHasself(self, ctx:RULEMLParser.HasselfContext):
        pass

    # Exit a parse tree produced by RULEMLParser#hasself.
    def exitHasself(self, ctx:RULEMLParser.HasselfContext):
        pass


    # Enter a parse tree produced by RULEMLParser#owlmaxc.
    def enterOwlmaxc(self, ctx:RULEMLParser.OwlmaxcContext):
        pass

    # Exit a parse tree produced by RULEMLParser#owlmaxc.
    def exitOwlmaxc(self, ctx:RULEMLParser.OwlmaxcContext):
        pass


    # Enter a parse tree produced by RULEMLParser#owlmaxqc.
    def enterOwlmaxqc(self, ctx:RULEMLParser.OwlmaxqcContext):
        pass

    # Exit a parse tree produced by RULEMLParser#owlmaxqc.
    def exitOwlmaxqc(self, ctx:RULEMLParser.OwlmaxqcContext):
        pass


    # Enter a parse tree produced by RULEMLParser#owlminc.
    def enterOwlminc(self, ctx:RULEMLParser.OwlmincContext):
        pass

    # Exit a parse tree produced by RULEMLParser#owlminc.
    def exitOwlminc(self, ctx:RULEMLParser.OwlmincContext):
        pass


    # Enter a parse tree produced by RULEMLParser#owlminqc.
    def enterOwlminqc(self, ctx:RULEMLParser.OwlminqcContext):
        pass

    # Exit a parse tree produced by RULEMLParser#owlminqc.
    def exitOwlminqc(self, ctx:RULEMLParser.OwlminqcContext):
        pass


    # Enter a parse tree produced by RULEMLParser#onproperties.
    def enterOnproperties(self, ctx:RULEMLParser.OnpropertiesContext):
        pass

    # Exit a parse tree produced by RULEMLParser#onproperties.
    def exitOnproperties(self, ctx:RULEMLParser.OnpropertiesContext):
        pass


    # Enter a parse tree produced by RULEMLParser#complementof.
    def enterComplementof(self, ctx:RULEMLParser.ComplementofContext):
        pass

    # Exit a parse tree produced by RULEMLParser#complementof.
    def exitComplementof(self, ctx:RULEMLParser.ComplementofContext):
        pass


    # Enter a parse tree produced by RULEMLParser#oneof.
    def enterOneof(self, ctx:RULEMLParser.OneofContext):
        pass

    # Exit a parse tree produced by RULEMLParser#oneof.
    def exitOneof(self, ctx:RULEMLParser.OneofContext):
        pass


    # Enter a parse tree produced by RULEMLParser#topop.
    def enterTopop(self, ctx:RULEMLParser.TopopContext):
        pass

    # Exit a parse tree produced by RULEMLParser#topop.
    def exitTopop(self, ctx:RULEMLParser.TopopContext):
        pass


    # Enter a parse tree produced by RULEMLParser#bottomop.
    def enterBottomop(self, ctx:RULEMLParser.BottomopContext):
        pass

    # Exit a parse tree produced by RULEMLParser#bottomop.
    def exitBottomop(self, ctx:RULEMLParser.BottomopContext):
        pass


    # Enter a parse tree produced by RULEMLParser#inverseof.
    def enterInverseof(self, ctx:RULEMLParser.InverseofContext):
        pass

    # Exit a parse tree produced by RULEMLParser#inverseof.
    def exitInverseof(self, ctx:RULEMLParser.InverseofContext):
        pass


    # Enter a parse tree produced by RULEMLParser#topdp.
    def enterTopdp(self, ctx:RULEMLParser.TopdpContext):
        pass

    # Exit a parse tree produced by RULEMLParser#topdp.
    def exitTopdp(self, ctx:RULEMLParser.TopdpContext):
        pass


    # Enter a parse tree produced by RULEMLParser#bottomdp.
    def enterBottomdp(self, ctx:RULEMLParser.BottomdpContext):
        pass

    # Exit a parse tree produced by RULEMLParser#bottomdp.
    def exitBottomdp(self, ctx:RULEMLParser.BottomdpContext):
        pass


    # Enter a parse tree produced by RULEMLParser#datacomplementof.
    def enterDatacomplementof(self, ctx:RULEMLParser.DatacomplementofContext):
        pass

    # Exit a parse tree produced by RULEMLParser#datacomplementof.
    def exitDatacomplementof(self, ctx:RULEMLParser.DatacomplementofContext):
        pass


    # Enter a parse tree produced by RULEMLParser#disjointwith.
    def enterDisjointwith(self, ctx:RULEMLParser.DisjointwithContext):
        pass

    # Exit a parse tree produced by RULEMLParser#disjointwith.
    def exitDisjointwith(self, ctx:RULEMLParser.DisjointwithContext):
        pass


    # Enter a parse tree produced by RULEMLParser#alldisjointclasses.
    def enterAlldisjointclasses(self, ctx:RULEMLParser.AlldisjointclassesContext):
        pass

    # Exit a parse tree produced by RULEMLParser#alldisjointclasses.
    def exitAlldisjointclasses(self, ctx:RULEMLParser.AlldisjointclassesContext):
        pass


    # Enter a parse tree produced by RULEMLParser#owlmembers.
    def enterOwlmembers(self, ctx:RULEMLParser.OwlmembersContext):
        pass

    # Exit a parse tree produced by RULEMLParser#owlmembers.
    def exitOwlmembers(self, ctx:RULEMLParser.OwlmembersContext):
        pass


    # Enter a parse tree produced by RULEMLParser#disjointunionof.
    def enterDisjointunionof(self, ctx:RULEMLParser.DisjointunionofContext):
        pass

    # Exit a parse tree produced by RULEMLParser#disjointunionof.
    def exitDisjointunionof(self, ctx:RULEMLParser.DisjointunionofContext):
        pass


    # Enter a parse tree produced by RULEMLParser#propertychainaxiom.
    def enterPropertychainaxiom(self, ctx:RULEMLParser.PropertychainaxiomContext):
        pass

    # Exit a parse tree produced by RULEMLParser#propertychainaxiom.
    def exitPropertychainaxiom(self, ctx:RULEMLParser.PropertychainaxiomContext):
        pass


    # Enter a parse tree produced by RULEMLParser#equiproperty.
    def enterEquiproperty(self, ctx:RULEMLParser.EquipropertyContext):
        pass

    # Exit a parse tree produced by RULEMLParser#equiproperty.
    def exitEquiproperty(self, ctx:RULEMLParser.EquipropertyContext):
        pass


    # Enter a parse tree produced by RULEMLParser#pdisjointwith.
    def enterPdisjointwith(self, ctx:RULEMLParser.PdisjointwithContext):
        pass

    # Exit a parse tree produced by RULEMLParser#pdisjointwith.
    def exitPdisjointwith(self, ctx:RULEMLParser.PdisjointwithContext):
        pass


    # Enter a parse tree produced by RULEMLParser#alldisjointp.
    def enterAlldisjointp(self, ctx:RULEMLParser.AlldisjointpContext):
        pass

    # Exit a parse tree produced by RULEMLParser#alldisjointp.
    def exitAlldisjointp(self, ctx:RULEMLParser.AlldisjointpContext):
        pass


    # Enter a parse tree produced by RULEMLParser#inversefuncp.
    def enterInversefuncp(self, ctx:RULEMLParser.InversefuncpContext):
        pass

    # Exit a parse tree produced by RULEMLParser#inversefuncp.
    def exitInversefuncp(self, ctx:RULEMLParser.InversefuncpContext):
        pass


    # Enter a parse tree produced by RULEMLParser#reflexp.
    def enterReflexp(self, ctx:RULEMLParser.ReflexpContext):
        pass

    # Exit a parse tree produced by RULEMLParser#reflexp.
    def exitReflexp(self, ctx:RULEMLParser.ReflexpContext):
        pass


    # Enter a parse tree produced by RULEMLParser#irreflexp.
    def enterIrreflexp(self, ctx:RULEMLParser.IrreflexpContext):
        pass

    # Exit a parse tree produced by RULEMLParser#irreflexp.
    def exitIrreflexp(self, ctx:RULEMLParser.IrreflexpContext):
        pass


    # Enter a parse tree produced by RULEMLParser#symmp.
    def enterSymmp(self, ctx:RULEMLParser.SymmpContext):
        pass

    # Exit a parse tree produced by RULEMLParser#symmp.
    def exitSymmp(self, ctx:RULEMLParser.SymmpContext):
        pass


    # Enter a parse tree produced by RULEMLParser#asymmp.
    def enterAsymmp(self, ctx:RULEMLParser.AsymmpContext):
        pass

    # Exit a parse tree produced by RULEMLParser#asymmp.
    def exitAsymmp(self, ctx:RULEMLParser.AsymmpContext):
        pass


    # Enter a parse tree produced by RULEMLParser#transitivep.
    def enterTransitivep(self, ctx:RULEMLParser.TransitivepContext):
        pass

    # Exit a parse tree produced by RULEMLParser#transitivep.
    def exitTransitivep(self, ctx:RULEMLParser.TransitivepContext):
        pass


    # Enter a parse tree produced by RULEMLParser#sameas.
    def enterSameas(self, ctx:RULEMLParser.SameasContext):
        pass

    # Exit a parse tree produced by RULEMLParser#sameas.
    def exitSameas(self, ctx:RULEMLParser.SameasContext):
        pass


    # Enter a parse tree produced by RULEMLParser#differentfrom.
    def enterDifferentfrom(self, ctx:RULEMLParser.DifferentfromContext):
        pass

    # Exit a parse tree produced by RULEMLParser#differentfrom.
    def exitDifferentfrom(self, ctx:RULEMLParser.DifferentfromContext):
        pass


    # Enter a parse tree produced by RULEMLParser#alldifferent.
    def enterAlldifferent(self, ctx:RULEMLParser.AlldifferentContext):
        pass

    # Exit a parse tree produced by RULEMLParser#alldifferent.
    def exitAlldifferent(self, ctx:RULEMLParser.AlldifferentContext):
        pass


    # Enter a parse tree produced by RULEMLParser#negpassert.
    def enterNegpassert(self, ctx:RULEMLParser.NegpassertContext):
        pass

    # Exit a parse tree produced by RULEMLParser#negpassert.
    def exitNegpassert(self, ctx:RULEMLParser.NegpassertContext):
        pass


    # Enter a parse tree produced by RULEMLParser#sourceindividual.
    def enterSourceindividual(self, ctx:RULEMLParser.SourceindividualContext):
        pass

    # Exit a parse tree produced by RULEMLParser#sourceindividual.
    def exitSourceindividual(self, ctx:RULEMLParser.SourceindividualContext):
        pass


    # Enter a parse tree produced by RULEMLParser#assertp.
    def enterAssertp(self, ctx:RULEMLParser.AssertpContext):
        pass

    # Exit a parse tree produced by RULEMLParser#assertp.
    def exitAssertp(self, ctx:RULEMLParser.AssertpContext):
        pass


    # Enter a parse tree produced by RULEMLParser#targetindividual.
    def enterTargetindividual(self, ctx:RULEMLParser.TargetindividualContext):
        pass

    # Exit a parse tree produced by RULEMLParser#targetindividual.
    def exitTargetindividual(self, ctx:RULEMLParser.TargetindividualContext):
        pass


    # Enter a parse tree produced by RULEMLParser#targetvalue.
    def enterTargetvalue(self, ctx:RULEMLParser.TargetvalueContext):
        pass

    # Exit a parse tree produced by RULEMLParser#targetvalue.
    def exitTargetvalue(self, ctx:RULEMLParser.TargetvalueContext):
        pass


    # Enter a parse tree produced by RULEMLParser#haskey.
    def enterHaskey(self, ctx:RULEMLParser.HaskeyContext):
        pass

    # Exit a parse tree produced by RULEMLParser#haskey.
    def exitHaskey(self, ctx:RULEMLParser.HaskeyContext):
        pass


    # Enter a parse tree produced by RULEMLParser#datatypep.
    def enterDatatypep(self, ctx:RULEMLParser.DatatypepContext):
        pass

    # Exit a parse tree produced by RULEMLParser#datatypep.
    def exitDatatypep(self, ctx:RULEMLParser.DatatypepContext):
        pass


    # Enter a parse tree produced by RULEMLParser#annotationp.
    def enterAnnotationp(self, ctx:RULEMLParser.AnnotationpContext):
        pass

    # Exit a parse tree produced by RULEMLParser#annotationp.
    def exitAnnotationp(self, ctx:RULEMLParser.AnnotationpContext):
        pass


    # Enter a parse tree produced by RULEMLParser#namedindividual.
    def enterNamedindividual(self, ctx:RULEMLParser.NamedindividualContext):
        pass

    # Exit a parse tree produced by RULEMLParser#namedindividual.
    def exitNamedindividual(self, ctx:RULEMLParser.NamedindividualContext):
        pass


    # Enter a parse tree produced by RULEMLParser#owlaxiom.
    def enterOwlaxiom(self, ctx:RULEMLParser.OwlaxiomContext):
        pass

    # Exit a parse tree produced by RULEMLParser#owlaxiom.
    def exitOwlaxiom(self, ctx:RULEMLParser.OwlaxiomContext):
        pass


    # Enter a parse tree produced by RULEMLParser#owlannotation.
    def enterOwlannotation(self, ctx:RULEMLParser.OwlannotationContext):
        pass

    # Exit a parse tree produced by RULEMLParser#owlannotation.
    def exitOwlannotation(self, ctx:RULEMLParser.OwlannotationContext):
        pass


    # Enter a parse tree produced by RULEMLParser#rdfsliteral.
    def enterRdfsliteral(self, ctx:RULEMLParser.RdfsliteralContext):
        pass

    # Exit a parse tree produced by RULEMLParser#rdfsliteral.
    def exitRdfsliteral(self, ctx:RULEMLParser.RdfsliteralContext):
        pass


    # Enter a parse tree produced by RULEMLParser#owlrational.
    def enterOwlrational(self, ctx:RULEMLParser.OwlrationalContext):
        pass

    # Exit a parse tree produced by RULEMLParser#owlrational.
    def exitOwlrational(self, ctx:RULEMLParser.OwlrationalContext):
        pass


    # Enter a parse tree produced by RULEMLParser#owlreal.
    def enterOwlreal(self, ctx:RULEMLParser.OwlrealContext):
        pass

    # Exit a parse tree produced by RULEMLParser#owlreal.
    def exitOwlreal(self, ctx:RULEMLParser.OwlrealContext):
        pass


    # Enter a parse tree produced by RULEMLParser#rdfplainl.
    def enterRdfplainl(self, ctx:RULEMLParser.RdfplainlContext):
        pass

    # Exit a parse tree produced by RULEMLParser#rdfplainl.
    def exitRdfplainl(self, ctx:RULEMLParser.RdfplainlContext):
        pass


    # Enter a parse tree produced by RULEMLParser#xmlliteral.
    def enterXmlliteral(self, ctx:RULEMLParser.XmlliteralContext):
        pass

    # Exit a parse tree produced by RULEMLParser#xmlliteral.
    def exitXmlliteral(self, ctx:RULEMLParser.XmlliteralContext):
        pass


    # Enter a parse tree produced by RULEMLParser#rdflangrange.
    def enterRdflangrange(self, ctx:RULEMLParser.RdflangrangeContext):
        pass

    # Exit a parse tree produced by RULEMLParser#rdflangrange.
    def exitRdflangrange(self, ctx:RULEMLParser.RdflangrangeContext):
        pass


    # Enter a parse tree produced by RULEMLParser#iri.
    def enterIri(self, ctx:RULEMLParser.IriContext):
        pass

    # Exit a parse tree produced by RULEMLParser#iri.
    def exitIri(self, ctx:RULEMLParser.IriContext):
        pass


    # Enter a parse tree produced by RULEMLParser#ihier_part.
    def enterIhier_part(self, ctx:RULEMLParser.Ihier_partContext):
        pass

    # Exit a parse tree produced by RULEMLParser#ihier_part.
    def exitIhier_part(self, ctx:RULEMLParser.Ihier_partContext):
        pass


    # Enter a parse tree produced by RULEMLParser#iri_reference.
    def enterIri_reference(self, ctx:RULEMLParser.Iri_referenceContext):
        pass

    # Exit a parse tree produced by RULEMLParser#iri_reference.
    def exitIri_reference(self, ctx:RULEMLParser.Iri_referenceContext):
        pass


    # Enter a parse tree produced by RULEMLParser#absolute_iri.
    def enterAbsolute_iri(self, ctx:RULEMLParser.Absolute_iriContext):
        pass

    # Exit a parse tree produced by RULEMLParser#absolute_iri.
    def exitAbsolute_iri(self, ctx:RULEMLParser.Absolute_iriContext):
        pass


    # Enter a parse tree produced by RULEMLParser#irelative_ref.
    def enterIrelative_ref(self, ctx:RULEMLParser.Irelative_refContext):
        pass

    # Exit a parse tree produced by RULEMLParser#irelative_ref.
    def exitIrelative_ref(self, ctx:RULEMLParser.Irelative_refContext):
        pass


    # Enter a parse tree produced by RULEMLParser#irelative_part.
    def enterIrelative_part(self, ctx:RULEMLParser.Irelative_partContext):
        pass

    # Exit a parse tree produced by RULEMLParser#irelative_part.
    def exitIrelative_part(self, ctx:RULEMLParser.Irelative_partContext):
        pass


    # Enter a parse tree produced by RULEMLParser#iauthority.
    def enterIauthority(self, ctx:RULEMLParser.IauthorityContext):
        pass

    # Exit a parse tree produced by RULEMLParser#iauthority.
    def exitIauthority(self, ctx:RULEMLParser.IauthorityContext):
        pass


    # Enter a parse tree produced by RULEMLParser#iuserinfo.
    def enterIuserinfo(self, ctx:RULEMLParser.IuserinfoContext):
        pass

    # Exit a parse tree produced by RULEMLParser#iuserinfo.
    def exitIuserinfo(self, ctx:RULEMLParser.IuserinfoContext):
        pass


    # Enter a parse tree produced by RULEMLParser#ihost.
    def enterIhost(self, ctx:RULEMLParser.IhostContext):
        pass

    # Exit a parse tree produced by RULEMLParser#ihost.
    def exitIhost(self, ctx:RULEMLParser.IhostContext):
        pass


    # Enter a parse tree produced by RULEMLParser#ireg_name.
    def enterIreg_name(self, ctx:RULEMLParser.Ireg_nameContext):
        pass

    # Exit a parse tree produced by RULEMLParser#ireg_name.
    def exitIreg_name(self, ctx:RULEMLParser.Ireg_nameContext):
        pass


    # Enter a parse tree produced by RULEMLParser#ipath.
    def enterIpath(self, ctx:RULEMLParser.IpathContext):
        pass

    # Exit a parse tree produced by RULEMLParser#ipath.
    def exitIpath(self, ctx:RULEMLParser.IpathContext):
        pass


    # Enter a parse tree produced by RULEMLParser#ipath_abempty.
    def enterIpath_abempty(self, ctx:RULEMLParser.Ipath_abemptyContext):
        pass

    # Exit a parse tree produced by RULEMLParser#ipath_abempty.
    def exitIpath_abempty(self, ctx:RULEMLParser.Ipath_abemptyContext):
        pass


    # Enter a parse tree produced by RULEMLParser#ipath_absolute.
    def enterIpath_absolute(self, ctx:RULEMLParser.Ipath_absoluteContext):
        pass

    # Exit a parse tree produced by RULEMLParser#ipath_absolute.
    def exitIpath_absolute(self, ctx:RULEMLParser.Ipath_absoluteContext):
        pass


    # Enter a parse tree produced by RULEMLParser#ipath_noscheme.
    def enterIpath_noscheme(self, ctx:RULEMLParser.Ipath_noschemeContext):
        pass

    # Exit a parse tree produced by RULEMLParser#ipath_noscheme.
    def exitIpath_noscheme(self, ctx:RULEMLParser.Ipath_noschemeContext):
        pass


    # Enter a parse tree produced by RULEMLParser#ipath_rootless.
    def enterIpath_rootless(self, ctx:RULEMLParser.Ipath_rootlessContext):
        pass

    # Exit a parse tree produced by RULEMLParser#ipath_rootless.
    def exitIpath_rootless(self, ctx:RULEMLParser.Ipath_rootlessContext):
        pass


    # Enter a parse tree produced by RULEMLParser#ipath_empty.
    def enterIpath_empty(self, ctx:RULEMLParser.Ipath_emptyContext):
        pass

    # Exit a parse tree produced by RULEMLParser#ipath_empty.
    def exitIpath_empty(self, ctx:RULEMLParser.Ipath_emptyContext):
        pass


    # Enter a parse tree produced by RULEMLParser#isegment.
    def enterIsegment(self, ctx:RULEMLParser.IsegmentContext):
        pass

    # Exit a parse tree produced by RULEMLParser#isegment.
    def exitIsegment(self, ctx:RULEMLParser.IsegmentContext):
        pass


    # Enter a parse tree produced by RULEMLParser#isegment_nz.
    def enterIsegment_nz(self, ctx:RULEMLParser.Isegment_nzContext):
        pass

    # Exit a parse tree produced by RULEMLParser#isegment_nz.
    def exitIsegment_nz(self, ctx:RULEMLParser.Isegment_nzContext):
        pass


    # Enter a parse tree produced by RULEMLParser#isegment_nz_nc.
    def enterIsegment_nz_nc(self, ctx:RULEMLParser.Isegment_nz_ncContext):
        pass

    # Exit a parse tree produced by RULEMLParser#isegment_nz_nc.
    def exitIsegment_nz_nc(self, ctx:RULEMLParser.Isegment_nz_ncContext):
        pass


    # Enter a parse tree produced by RULEMLParser#ipchar.
    def enterIpchar(self, ctx:RULEMLParser.IpcharContext):
        pass

    # Exit a parse tree produced by RULEMLParser#ipchar.
    def exitIpchar(self, ctx:RULEMLParser.IpcharContext):
        pass


    # Enter a parse tree produced by RULEMLParser#iquery.
    def enterIquery(self, ctx:RULEMLParser.IqueryContext):
        pass

    # Exit a parse tree produced by RULEMLParser#iquery.
    def exitIquery(self, ctx:RULEMLParser.IqueryContext):
        pass


    # Enter a parse tree produced by RULEMLParser#ifragment.
    def enterIfragment(self, ctx:RULEMLParser.IfragmentContext):
        pass

    # Exit a parse tree produced by RULEMLParser#ifragment.
    def exitIfragment(self, ctx:RULEMLParser.IfragmentContext):
        pass


    # Enter a parse tree produced by RULEMLParser#iunreserved.
    def enterIunreserved(self, ctx:RULEMLParser.IunreservedContext):
        pass

    # Exit a parse tree produced by RULEMLParser#iunreserved.
    def exitIunreserved(self, ctx:RULEMLParser.IunreservedContext):
        pass


    # Enter a parse tree produced by RULEMLParser#scheme.
    def enterScheme(self, ctx:RULEMLParser.SchemeContext):
        pass

    # Exit a parse tree produced by RULEMLParser#scheme.
    def exitScheme(self, ctx:RULEMLParser.SchemeContext):
        pass


    # Enter a parse tree produced by RULEMLParser#port.
    def enterPort(self, ctx:RULEMLParser.PortContext):
        pass

    # Exit a parse tree produced by RULEMLParser#port.
    def exitPort(self, ctx:RULEMLParser.PortContext):
        pass


    # Enter a parse tree produced by RULEMLParser#ip_literal.
    def enterIp_literal(self, ctx:RULEMLParser.Ip_literalContext):
        pass

    # Exit a parse tree produced by RULEMLParser#ip_literal.
    def exitIp_literal(self, ctx:RULEMLParser.Ip_literalContext):
        pass


    # Enter a parse tree produced by RULEMLParser#ip_v_future.
    def enterIp_v_future(self, ctx:RULEMLParser.Ip_v_futureContext):
        pass

    # Exit a parse tree produced by RULEMLParser#ip_v_future.
    def exitIp_v_future(self, ctx:RULEMLParser.Ip_v_futureContext):
        pass


    # Enter a parse tree produced by RULEMLParser#ip_v6_address.
    def enterIp_v6_address(self, ctx:RULEMLParser.Ip_v6_addressContext):
        pass

    # Exit a parse tree produced by RULEMLParser#ip_v6_address.
    def exitIp_v6_address(self, ctx:RULEMLParser.Ip_v6_addressContext):
        pass


    # Enter a parse tree produced by RULEMLParser#h16.
    def enterH16(self, ctx:RULEMLParser.H16Context):
        pass

    # Exit a parse tree produced by RULEMLParser#h16.
    def exitH16(self, ctx:RULEMLParser.H16Context):
        pass


    # Enter a parse tree produced by RULEMLParser#ls32.
    def enterLs32(self, ctx:RULEMLParser.Ls32Context):
        pass

    # Exit a parse tree produced by RULEMLParser#ls32.
    def exitLs32(self, ctx:RULEMLParser.Ls32Context):
        pass


    # Enter a parse tree produced by RULEMLParser#ip_v4_address.
    def enterIp_v4_address(self, ctx:RULEMLParser.Ip_v4_addressContext):
        pass

    # Exit a parse tree produced by RULEMLParser#ip_v4_address.
    def exitIp_v4_address(self, ctx:RULEMLParser.Ip_v4_addressContext):
        pass


    # Enter a parse tree produced by RULEMLParser#dec_octet.
    def enterDec_octet(self, ctx:RULEMLParser.Dec_octetContext):
        pass

    # Exit a parse tree produced by RULEMLParser#dec_octet.
    def exitDec_octet(self, ctx:RULEMLParser.Dec_octetContext):
        pass


    # Enter a parse tree produced by RULEMLParser#pct_encoded.
    def enterPct_encoded(self, ctx:RULEMLParser.Pct_encodedContext):
        pass

    # Exit a parse tree produced by RULEMLParser#pct_encoded.
    def exitPct_encoded(self, ctx:RULEMLParser.Pct_encodedContext):
        pass


    # Enter a parse tree produced by RULEMLParser#unreserved.
    def enterUnreserved(self, ctx:RULEMLParser.UnreservedContext):
        pass

    # Exit a parse tree produced by RULEMLParser#unreserved.
    def exitUnreserved(self, ctx:RULEMLParser.UnreservedContext):
        pass


    # Enter a parse tree produced by RULEMLParser#reserved.
    def enterReserved(self, ctx:RULEMLParser.ReservedContext):
        pass

    # Exit a parse tree produced by RULEMLParser#reserved.
    def exitReserved(self, ctx:RULEMLParser.ReservedContext):
        pass


    # Enter a parse tree produced by RULEMLParser#gen_delims.
    def enterGen_delims(self, ctx:RULEMLParser.Gen_delimsContext):
        pass

    # Exit a parse tree produced by RULEMLParser#gen_delims.
    def exitGen_delims(self, ctx:RULEMLParser.Gen_delimsContext):
        pass


    # Enter a parse tree produced by RULEMLParser#sub_delims.
    def enterSub_delims(self, ctx:RULEMLParser.Sub_delimsContext):
        pass

    # Exit a parse tree produced by RULEMLParser#sub_delims.
    def exitSub_delims(self, ctx:RULEMLParser.Sub_delimsContext):
        pass


    # Enter a parse tree produced by RULEMLParser#alpha.
    def enterAlpha(self, ctx:RULEMLParser.AlphaContext):
        pass

    # Exit a parse tree produced by RULEMLParser#alpha.
    def exitAlpha(self, ctx:RULEMLParser.AlphaContext):
        pass


    # Enter a parse tree produced by RULEMLParser#hexdig.
    def enterHexdig(self, ctx:RULEMLParser.HexdigContext):
        pass

    # Exit a parse tree produced by RULEMLParser#hexdig.
    def exitHexdig(self, ctx:RULEMLParser.HexdigContext):
        pass


    # Enter a parse tree produced by RULEMLParser#digit.
    def enterDigit(self, ctx:RULEMLParser.DigitContext):
        pass

    # Exit a parse tree produced by RULEMLParser#digit.
    def exitDigit(self, ctx:RULEMLParser.DigitContext):
        pass


    # Enter a parse tree produced by RULEMLParser#non_zero_digit.
    def enterNon_zero_digit(self, ctx:RULEMLParser.Non_zero_digitContext):
        pass

    # Exit a parse tree produced by RULEMLParser#non_zero_digit.
    def exitNon_zero_digit(self, ctx:RULEMLParser.Non_zero_digitContext):
        pass



del RULEMLParser