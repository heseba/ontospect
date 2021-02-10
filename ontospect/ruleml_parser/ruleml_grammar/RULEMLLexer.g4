/*
 [The "BSD licence"]
 Copyright (c) 2013 Terence Parr
 All rights reserved.

 Redistribution and use in source and binary forms, with or without
 modification, are permitted provided that the following conditions
 are met:
 1. Redistributions of source code must retain the above copyright
    notice, this list of conditions and the following disclaimer.
 2. Redistributions in binary form must reproduce the above copyright
    notice, this list of conditions and the following disclaimer in the
    documentation and/or other materials provided with the distribution.
 3. The name of the author may not be used to endorse or promote products
    derived from this software without specific prior written permission.

 THIS SOFTWARE IS PROVIDED BY THE AUTHOR ``AS IS'' AND ANY EXPRESS OR
 IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES
 OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
 IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY DIRECT, INDIRECT,
 INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT
 NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
 DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
 THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
 (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF
 THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
*/

/**
Author: Yichen Wang
RuleML lexer derived from ANTLR v4 ref guide book example */
lexer grammar RULEMLLexer;



SEA_WS      :   (' '|'\t'|'\r'? '\n')+  -> skip;

ATOMOPEN: '<Atom>';
ATOMCLOSE: '</Atom>' ;
RELOPEN :'<Rel>'  ;
RELCLOSE:'</Rel>';
INDOPEN : '<Ind>';
INDCLOSE: '</Ind>';
//Content        : ContentStartChar ContentChar* ;
WS           :   [ \t\r\n]          -> skip ;
STATEMENT   : '<Rel>statement</Rel>';
//NODEID      : N DIGIT{5} ;
fragment
HEXDIGIT    :   [a-fA-F0-9] ;

fragment
DIGIT       :   [0-9] ;
//------------functor list----------------------------------
RDFTYPE     :   'rdf:type';
SUBP        :   'rdfs:subPropertyOf';
SUBC        :   'rdfs:subClassOf';
RDFSDOMAIN  :   'rdfs:domain';
RDFSRANGE   :   'rdfs:range';
EQUICLASS   :   'owl:equivalentClass';
OWLCLASS    :   'owl:Class';
RDFDESCRIPTION
            :   'rdf:Description';
WITHRESTRICTIONS
            :   'owl:withRestrictions';
INTERSECTIONOF
            :   'owl:intersectionOf';
OWLSVF      :   'owl:someValuesFrom';
OWLAVF      :   'owl:allValuesFrom';
ONP         :   'owl:onProperty';
ONDATATYPE  :   'owl:onDatatype';
HASVALUE    :   'owl:hasValue';
HASSELF     :   'owl:hasSelf';
SEEALSO     :   'rdfs:seeAlso';
RDFSCOMMENT :   'rdfs:comment';
RDFSLABEL   :   'rdfs:label' ;
DCDESCRIPTION:  'dc:description';
DCSOURCE    :   'dc:source';
MINEXCLUSIVE:   'xsd:minExclusive';
MAXEXCLUSIVE:   'xsd:maxExclusive';
XSD         :   'xsd:';
OWLRESTRICTION
            :   'owl:Restriction';
RDFSDATATYPE:   'rdfs:Datatype';
FUNCPROPERTY:   'owl:FunctionalProperty';
OWLONCLASS  :   'owl:onClass';
OWLONDATARANGE
            :   'owl:onDataRange';
OWLQC       :'owl:qualifiedCardinality';
OBJECTPROPERTY
            : 'owl:ObjectProperty';
RDFREST     : 'rdf:rest';
RDFNIL      : 'rdf:nil';
UNIONOF     : 'owl:unionOf';
CARDINALITY : 'owl:cardinality';
OWLMAXC     : 'owl:maxCardinality';
OWLMAXQC    : 'owl:maxQualifiedCardinality';
OWLMINC     : 'owl:minCardinality';
OWLMINQC    : 'owl:minQualifiedCardinality';
ONPROPERTIES: 'owl:onProperties';
COMPLEMENTOF: 'owl:complementOf';
ONEOF       : 'owl:oneOf';
SKOSDEF     : 'skos:definition';
SKOSPREFLABEL
            : 'skos:prefLabel';
SKOSALTLABEL
            : 'skos:altLabel';
SKOSHIDDENLABEL
            : 'skos:hiddenLabel';
SKOSNOTATION: 'skos:notation';
TRUE        : 'true';
FALSE       : 'false';
TOPOP       : 'owl:topObjectProperty';
BOTTOMOP    : 'owl:bottomObjectProperty';
INVERSEOF   : 'owl:inverseOf';
TOPDP       : 'owl:topDataProperty';
BOTTOMDP    : 'owl:bottomDataProperty';
DATACOMPLEMENTOF
            : 'owl:datatypeComplementOf';
DISJOINTWITH: 'owl:disjointWith';
ALLDISJOINTCLASSES
            : 'owl:AllDisjointClasses';
OWLMEMBERS  : 'owl:members';
DISJOINTUNIONOF
            : 'owl:disjointUnionOf';
PROPERTYCHAINAXIOM
            : 'owl:propertyChainAxiom';
EQUIPROPERTY: 'owl:equivalentProperty';
PDISJOINTWITH
            : 'owl:propertyDisjointWith';
ALLDISJOINTP: 'owl:AllDisjointProperties';
INVERSEFUNCP: 'owl:InverseFunctionalProperty';
REFLEXP     : 'owl:ReflexiveProperty';
IRREFLEXP   : 'owl:IrreflexiveProperty';
SYMMP       : 'owl:SymmetricProperty';
ASYMMP      : 'owl:AsymmetricProperty';
TRANSITIVEP : 'owl:TransitiveProperty';
SAMEAS      : 'owl:sameAs';
DIFFERENTFROM
            : 'owl:differentFrom';
ALLDIFFERENT: 'owl:AllDifferent';
NEGPASSERT  : 'owl:NegativePropertyAssertion';
SOURCEINDIVIDUAL
            : 'owl:sourceIndividual';
ASSERTP     : 'owl:assertionProperty';
TARGETINDIVIDUAL
            : 'owl:targetIndividual';
TARGETVALUE : 'owl:targetValue';
HASKEY      : 'owl:hasKey';
DATATYPEP   : 'owl:DatatypeProperty';
ANNOTATIONP : 'owl:AnnotationProperty';
NAMEDINDIVIDUAL
            : 'owl:NamedIndividual';
OWLAXIOM    : 'owl:Axiom';
ANNOTATEDS  : 'owl:annotatedSource';
ANNOTATEDP  : 'owl:annotatedProperty';
ANNOTATEDT  : 'owl:annotatedTarget';
OWLANNOTATION
            : 'owl:Annotation';
ISDEFINEDBY : 'rdfs:isDefinedBy';
VERSIONINFO : 'owl:versionInfo';
DEPRECATED  : 'owl:deprecated';
BACKCOMPATWITH
            : 'owl:backwardCompatibleWith';
INCOMPATWITH: 'owl:incompatibleWith';
PRIORVERSION: 'owl:priorVersion';
RDFSLITERAL : 'rdfs:Literal';
OWLRATIONAL : 'owl:rational';
OWLREAL     : 'owl:real';
RDFPLAINL   : 'rdf:PlainLiteral';
XMLLITERAL  : 'rdf:XMLLiteral';
RDFLANGRANGE: 'rdf:langRange';
//-------------------------------------------------------
POWER       :   '^';

fragment
ContentChar    :   ContentStartChar
            |   '-' | '_' | '.' | DIGIT
            |   '\u00B7'
            |   '\u0300'..'\u036F'
            |   '\u203F'..'\u2040'
            |   '/'
            |   ':'
            |   '#'
            |   ' '
            |   ',' | '(' | ')' | '^'
            ;

fragment
ContentStartChar
            :   [:a-zA-Z]
            |   '\u2070'..'\u218F'
            |   '\u2C00'..'\u2FEF'
            |   '\u3001'..'\uD7FF'
            |   '\uF900'..'\uFDCF'
            |   '\uFDF0'..'\uFFFD'
            |   DIGIT
            ;

//----------------------------------------------------//
/*
 * Lexer rules
 *//// ucschar        = %xA0-D7FF / %xF900-FDCF / %xFDF0-FFEF///                / %x10000-1FFFD / %x20000-2FFFD / %x30000-3FFFD///                / %x40000-4FFFD / %x50000-5FFFD / %x60000-6FFFD///                / %x70000-7FFFD / %x80000-8FFFD / %x90000-9FFFD///                / %xA0000-AFFFD / %xB0000-BFFFD / %xC0000-CFFFD///                / %xD0000-DFFFD / %xE1000-EFFFD

UCSCHAR
   : '\u00A0' .. '\uD7FF'
   | '\uF900' .. '\uFDCF'
   | '\uFDF0' .. '\uFFEF'
   | '\u{10000}' .. '\u{1FFFD}'
   | '\u{20000}' .. '\u{2FFFD}'
   | '\u{30000}' .. '\u{3FFFD}'
   | '\u{40000}' .. '\u{4FFFD}'
   | '\u{50000}' .. '\u{5FFFD}'
   | '\u{60000}' .. '\u{6FFFD}'
   | '\u{70000}' .. '\u{7FFFD}'
   | '\u{80000}' .. '\u{8FFFD}'
   | '\u{90000}' .. '\u{9FFFD}'
   | '\u{A0000}' .. '\u{AFFFD}'
   | '\u{B0000}' .. '\u{BFFFD}'
   | '\u{C0000}' .. '\u{CFFFD}'
   | '\u{D0000}' .. '\u{DFFFD}'
   | '\u{E1000}' .. '\u{EFFFD}'
   ;

/// iprivate       = %xE000-F8FF / %xF0000-FFFFD / %x100000-10FFFD

IPRIVATE
   : '\uE000' .. '\uF8FF'
   | '\u{F0000}' .. '\u{FFFFD}'
   | '\u{100000}' .. '\u{10FFFD}'
   ;


D0
   : '0'
   ;


D1
   : '1'
   ;


D2
   : '2'
   ;


D3
   : '3'
   ;


D4
   : '4'
   ;


D5
   : '5'
   ;


D6
   : '6'
   ;


D7
   : '7'
   ;


D8
   : '8'
   ;


D9
   : '9'
   ;


A
   : [aA]
   ;


B
   : [bB]
   ;


C
   : [cC]
   ;


D
   : [dD]
   ;


E
   : [eE]
   ;


F
   : [fF]
   ;


G
   : [gG]
   ;


H
   : [hH]
   ;


I
   : [iI]
   ;


J
   : [jJ]
   ;


K
   : [kK]
   ;


L
   : [lL]
   ;


M
   : [mM]
   ;


N
   : [nN]
   ;


O
   : [oO]
   ;


P
   : [pP]
   ;


Q
   : [qQ]
   ;


R
   : [rR]
   ;


S
   : [sS]
   ;


T
   : [tT]
   ;


U
   : [uU]
   ;


V
   : [vV]
   ;


W
   : [wW]
   ;


X
   : [xX]
   ;


Y
   : [yY]
   ;


Z
   : [zZ]
   ;


COL2
   : '::'
   ;


COL
   : ':'
   ;


DOT
   : '.'
   ;


PERCENT
   : '%'
   ;


HYPHEN
   : '-'
   ;


TILDE
   : '~'
   ;


USCORE
   : '_'
   ;


EXCL
   : '!'
   ;


DOLLAR
   : '$'
   ;


AMP
   : '&'
   ;


SQUOTE
   : '\''
   ;

DQUOTE
    : '"'
    ;

OPAREN
   : '('
   ;


CPAREN
   : ')'
   ;


STAR
   : '*'
   ;


PLUS
   : '+'
   ;


COMMA
   : ','
   ;


SCOL
   : ';'
   ;


EQUALS
   : '='
   ;


FSLASH2
   : '//'
   ;


FSLASH
   : '/'
   ;


QMARK
   : '?'
   ;


HASH
   : '#'
   ;


OBRACK
   : '['
   ;


CBRACK
   : ']'
   ;


AT
   : '@'
   ;

AOBRACK
    : '<'
    ;

ACBRACK
    : '>'
    ;

