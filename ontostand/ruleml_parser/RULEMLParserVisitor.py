# Generated from D:/OneDrive/ontoproject/ontostand/ruleml_parser/ruleml_grammar\RULEMLParser.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .RULEMLParser import RULEMLParser
else:
    from RULEMLParser import RULEMLParser

# This class defines a complete generic visitor for a parse tree produced by RULEMLParser.

class RULEMLParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by RULEMLParser#ruleMLDoc.
    def visitRuleMLDoc(self, ctx:RULEMLParser.RuleMLDocContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#atom.
    def visitAtom(self, ctx:RULEMLParser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#ignoredatom.
    def visitIgnoredatom(self, ctx:RULEMLParser.IgnoredatomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#statement.
    def visitStatement(self, ctx:RULEMLParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#subject.
    def visitSubject(self, ctx:RULEMLParser.SubjectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#predicate.
    def visitPredicate(self, ctx:RULEMLParser.PredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#objekt.
    def visitObjekt(self, ctx:RULEMLParser.ObjektContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#misc.
    def visitMisc(self, ctx:RULEMLParser.MiscContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#ignoredpred.
    def visitIgnoredpred(self, ctx:RULEMLParser.IgnoredpredContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#nodeid.
    def visitNodeid(self, ctx:RULEMLParser.NodeidContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#subjectcontent.
    def visitSubjectcontent(self, ctx:RULEMLParser.SubjectcontentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#objektcontent.
    def visitObjektcontent(self, ctx:RULEMLParser.ObjektcontentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#ignoredverb.
    def visitIgnoredverb(self, ctx:RULEMLParser.IgnoredverbContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#verb.
    def visitVerb(self, ctx:RULEMLParser.VerbContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#xsd.
    def visitXsd(self, ctx:RULEMLParser.XsdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#xsdvalue.
    def visitXsdvalue(self, ctx:RULEMLParser.XsdvalueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#xsddatatype.
    def visitXsddatatype(self, ctx:RULEMLParser.XsddatatypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#unreserved_content.
    def visitUnreserved_content(self, ctx:RULEMLParser.Unreserved_contentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#rdfscomment.
    def visitRdfscomment(self, ctx:RULEMLParser.RdfscommentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#rdfslabel.
    def visitRdfslabel(self, ctx:RULEMLParser.RdfslabelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#dcdescription.
    def visitDcdescription(self, ctx:RULEMLParser.DcdescriptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#rdftype.
    def visitRdftype(self, ctx:RULEMLParser.RdftypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#seealso.
    def visitSeealso(self, ctx:RULEMLParser.SeealsoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#rdfrest.
    def visitRdfrest(self, ctx:RULEMLParser.RdfrestContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#skosdef.
    def visitSkosdef(self, ctx:RULEMLParser.SkosdefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#skospreflabel.
    def visitSkospreflabel(self, ctx:RULEMLParser.SkospreflabelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#skosaltlabel.
    def visitSkosaltlabel(self, ctx:RULEMLParser.SkosaltlabelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#skoshiddenlabel.
    def visitSkoshiddenlabel(self, ctx:RULEMLParser.SkoshiddenlabelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#skosnotation.
    def visitSkosnotation(self, ctx:RULEMLParser.SkosnotationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#annotateds.
    def visitAnnotateds(self, ctx:RULEMLParser.AnnotatedsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#annotatedp.
    def visitAnnotatedp(self, ctx:RULEMLParser.AnnotatedpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#annotatedt.
    def visitAnnotatedt(self, ctx:RULEMLParser.AnnotatedtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#isdefinedby.
    def visitIsdefinedby(self, ctx:RULEMLParser.IsdefinedbyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#versioninfo.
    def visitVersioninfo(self, ctx:RULEMLParser.VersioninfoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#deprecated.
    def visitDeprecated(self, ctx:RULEMLParser.DeprecatedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#backcompatwith.
    def visitBackcompatwith(self, ctx:RULEMLParser.BackcompatwithContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#incompatwith.
    def visitIncompatwith(self, ctx:RULEMLParser.IncompatwithContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#priorversion.
    def visitPriorversion(self, ctx:RULEMLParser.PriorversionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#dcsource.
    def visitDcsource(self, ctx:RULEMLParser.DcsourceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#ondatatype.
    def visitOndatatype(self, ctx:RULEMLParser.OndatatypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#owlwithrestrictions.
    def visitOwlwithrestrictions(self, ctx:RULEMLParser.OwlwithrestrictionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#subpropertyof.
    def visitSubpropertyof(self, ctx:RULEMLParser.SubpropertyofContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#subclassof.
    def visitSubclassof(self, ctx:RULEMLParser.SubclassofContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#rdfsdomain.
    def visitRdfsdomain(self, ctx:RULEMLParser.RdfsdomainContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#rdfsrange.
    def visitRdfsrange(self, ctx:RULEMLParser.RdfsrangeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#equiclass.
    def visitEquiclass(self, ctx:RULEMLParser.EquiclassContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#owlclass.
    def visitOwlclass(self, ctx:RULEMLParser.OwlclassContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#rdfdescription.
    def visitRdfdescription(self, ctx:RULEMLParser.RdfdescriptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#intersectionof.
    def visitIntersectionof(self, ctx:RULEMLParser.IntersectionofContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#owlsvf.
    def visitOwlsvf(self, ctx:RULEMLParser.OwlsvfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#owlavf.
    def visitOwlavf(self, ctx:RULEMLParser.OwlavfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#onproperty.
    def visitOnproperty(self, ctx:RULEMLParser.OnpropertyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#hasvalue.
    def visitHasvalue(self, ctx:RULEMLParser.HasvalueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#minexclusive.
    def visitMinexclusive(self, ctx:RULEMLParser.MinexclusiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#maxexclusive.
    def visitMaxexclusive(self, ctx:RULEMLParser.MaxexclusiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#owlrestriction.
    def visitOwlrestriction(self, ctx:RULEMLParser.OwlrestrictionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#rdfsdatatype.
    def visitRdfsdatatype(self, ctx:RULEMLParser.RdfsdatatypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#funcproperty.
    def visitFuncproperty(self, ctx:RULEMLParser.FuncpropertyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#owlondatarange.
    def visitOwlondatarange(self, ctx:RULEMLParser.OwlondatarangeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#owlonclass.
    def visitOwlonclass(self, ctx:RULEMLParser.OwlonclassContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#owlqc.
    def visitOwlqc(self, ctx:RULEMLParser.OwlqcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#objectproperty.
    def visitObjectproperty(self, ctx:RULEMLParser.ObjectpropertyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#rdfnil.
    def visitRdfnil(self, ctx:RULEMLParser.RdfnilContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#unionof.
    def visitUnionof(self, ctx:RULEMLParser.UnionofContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#cardinality.
    def visitCardinality(self, ctx:RULEMLParser.CardinalityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#hasself.
    def visitHasself(self, ctx:RULEMLParser.HasselfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#owlmaxc.
    def visitOwlmaxc(self, ctx:RULEMLParser.OwlmaxcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#owlmaxqc.
    def visitOwlmaxqc(self, ctx:RULEMLParser.OwlmaxqcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#owlminc.
    def visitOwlminc(self, ctx:RULEMLParser.OwlmincContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#owlminqc.
    def visitOwlminqc(self, ctx:RULEMLParser.OwlminqcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#onproperties.
    def visitOnproperties(self, ctx:RULEMLParser.OnpropertiesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#complementof.
    def visitComplementof(self, ctx:RULEMLParser.ComplementofContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#oneof.
    def visitOneof(self, ctx:RULEMLParser.OneofContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#topop.
    def visitTopop(self, ctx:RULEMLParser.TopopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#bottomop.
    def visitBottomop(self, ctx:RULEMLParser.BottomopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#inverseof.
    def visitInverseof(self, ctx:RULEMLParser.InverseofContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#topdp.
    def visitTopdp(self, ctx:RULEMLParser.TopdpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#bottomdp.
    def visitBottomdp(self, ctx:RULEMLParser.BottomdpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#datacomplementof.
    def visitDatacomplementof(self, ctx:RULEMLParser.DatacomplementofContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#disjointwith.
    def visitDisjointwith(self, ctx:RULEMLParser.DisjointwithContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#alldisjointclasses.
    def visitAlldisjointclasses(self, ctx:RULEMLParser.AlldisjointclassesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#owlmembers.
    def visitOwlmembers(self, ctx:RULEMLParser.OwlmembersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#disjointunionof.
    def visitDisjointunionof(self, ctx:RULEMLParser.DisjointunionofContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#propertychainaxiom.
    def visitPropertychainaxiom(self, ctx:RULEMLParser.PropertychainaxiomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#equiproperty.
    def visitEquiproperty(self, ctx:RULEMLParser.EquipropertyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#pdisjointwith.
    def visitPdisjointwith(self, ctx:RULEMLParser.PdisjointwithContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#alldisjointp.
    def visitAlldisjointp(self, ctx:RULEMLParser.AlldisjointpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#inversefuncp.
    def visitInversefuncp(self, ctx:RULEMLParser.InversefuncpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#reflexp.
    def visitReflexp(self, ctx:RULEMLParser.ReflexpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#irreflexp.
    def visitIrreflexp(self, ctx:RULEMLParser.IrreflexpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#symmp.
    def visitSymmp(self, ctx:RULEMLParser.SymmpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#asymmp.
    def visitAsymmp(self, ctx:RULEMLParser.AsymmpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#transitivep.
    def visitTransitivep(self, ctx:RULEMLParser.TransitivepContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#sameas.
    def visitSameas(self, ctx:RULEMLParser.SameasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#differentfrom.
    def visitDifferentfrom(self, ctx:RULEMLParser.DifferentfromContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#alldifferent.
    def visitAlldifferent(self, ctx:RULEMLParser.AlldifferentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#negpassert.
    def visitNegpassert(self, ctx:RULEMLParser.NegpassertContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#sourceindividual.
    def visitSourceindividual(self, ctx:RULEMLParser.SourceindividualContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#assertp.
    def visitAssertp(self, ctx:RULEMLParser.AssertpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#targetindividual.
    def visitTargetindividual(self, ctx:RULEMLParser.TargetindividualContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#targetvalue.
    def visitTargetvalue(self, ctx:RULEMLParser.TargetvalueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#haskey.
    def visitHaskey(self, ctx:RULEMLParser.HaskeyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#datatypep.
    def visitDatatypep(self, ctx:RULEMLParser.DatatypepContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#annotationp.
    def visitAnnotationp(self, ctx:RULEMLParser.AnnotationpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#namedindividual.
    def visitNamedindividual(self, ctx:RULEMLParser.NamedindividualContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#owlaxiom.
    def visitOwlaxiom(self, ctx:RULEMLParser.OwlaxiomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#owlannotation.
    def visitOwlannotation(self, ctx:RULEMLParser.OwlannotationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#rdfsliteral.
    def visitRdfsliteral(self, ctx:RULEMLParser.RdfsliteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#owlrational.
    def visitOwlrational(self, ctx:RULEMLParser.OwlrationalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#owlreal.
    def visitOwlreal(self, ctx:RULEMLParser.OwlrealContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#rdfplainl.
    def visitRdfplainl(self, ctx:RULEMLParser.RdfplainlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#xmlliteral.
    def visitXmlliteral(self, ctx:RULEMLParser.XmlliteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#rdflangrange.
    def visitRdflangrange(self, ctx:RULEMLParser.RdflangrangeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#iri.
    def visitIri(self, ctx:RULEMLParser.IriContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#ihier_part.
    def visitIhier_part(self, ctx:RULEMLParser.Ihier_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#iri_reference.
    def visitIri_reference(self, ctx:RULEMLParser.Iri_referenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#absolute_iri.
    def visitAbsolute_iri(self, ctx:RULEMLParser.Absolute_iriContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#irelative_ref.
    def visitIrelative_ref(self, ctx:RULEMLParser.Irelative_refContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#irelative_part.
    def visitIrelative_part(self, ctx:RULEMLParser.Irelative_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#iauthority.
    def visitIauthority(self, ctx:RULEMLParser.IauthorityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#iuserinfo.
    def visitIuserinfo(self, ctx:RULEMLParser.IuserinfoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#ihost.
    def visitIhost(self, ctx:RULEMLParser.IhostContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#ireg_name.
    def visitIreg_name(self, ctx:RULEMLParser.Ireg_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#ipath.
    def visitIpath(self, ctx:RULEMLParser.IpathContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#ipath_abempty.
    def visitIpath_abempty(self, ctx:RULEMLParser.Ipath_abemptyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#ipath_absolute.
    def visitIpath_absolute(self, ctx:RULEMLParser.Ipath_absoluteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#ipath_noscheme.
    def visitIpath_noscheme(self, ctx:RULEMLParser.Ipath_noschemeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#ipath_rootless.
    def visitIpath_rootless(self, ctx:RULEMLParser.Ipath_rootlessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#ipath_empty.
    def visitIpath_empty(self, ctx:RULEMLParser.Ipath_emptyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#isegment.
    def visitIsegment(self, ctx:RULEMLParser.IsegmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#isegment_nz.
    def visitIsegment_nz(self, ctx:RULEMLParser.Isegment_nzContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#isegment_nz_nc.
    def visitIsegment_nz_nc(self, ctx:RULEMLParser.Isegment_nz_ncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#ipchar.
    def visitIpchar(self, ctx:RULEMLParser.IpcharContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#iquery.
    def visitIquery(self, ctx:RULEMLParser.IqueryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#ifragment.
    def visitIfragment(self, ctx:RULEMLParser.IfragmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#iunreserved.
    def visitIunreserved(self, ctx:RULEMLParser.IunreservedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#scheme.
    def visitScheme(self, ctx:RULEMLParser.SchemeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#port.
    def visitPort(self, ctx:RULEMLParser.PortContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#ip_literal.
    def visitIp_literal(self, ctx:RULEMLParser.Ip_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#ip_v_future.
    def visitIp_v_future(self, ctx:RULEMLParser.Ip_v_futureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#ip_v6_address.
    def visitIp_v6_address(self, ctx:RULEMLParser.Ip_v6_addressContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#h16.
    def visitH16(self, ctx:RULEMLParser.H16Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#ls32.
    def visitLs32(self, ctx:RULEMLParser.Ls32Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#ip_v4_address.
    def visitIp_v4_address(self, ctx:RULEMLParser.Ip_v4_addressContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#dec_octet.
    def visitDec_octet(self, ctx:RULEMLParser.Dec_octetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#pct_encoded.
    def visitPct_encoded(self, ctx:RULEMLParser.Pct_encodedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#unreserved.
    def visitUnreserved(self, ctx:RULEMLParser.UnreservedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#reserved.
    def visitReserved(self, ctx:RULEMLParser.ReservedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#gen_delims.
    def visitGen_delims(self, ctx:RULEMLParser.Gen_delimsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#sub_delims.
    def visitSub_delims(self, ctx:RULEMLParser.Sub_delimsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#alpha.
    def visitAlpha(self, ctx:RULEMLParser.AlphaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#hexdig.
    def visitHexdig(self, ctx:RULEMLParser.HexdigContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#digit.
    def visitDigit(self, ctx:RULEMLParser.DigitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RULEMLParser#non_zero_digit.
    def visitNon_zero_digit(self, ctx:RULEMLParser.Non_zero_digitContext):
        return self.visitChildren(ctx)



del RULEMLParser