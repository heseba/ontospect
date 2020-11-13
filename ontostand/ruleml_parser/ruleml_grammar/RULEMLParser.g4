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
RuleML Parser derived from ANTLR v4 ref guide book example
*/
parser grammar RULEMLParser;

options { tokenVocab=RULEMLLexer; }

ruleMLDoc:
        misc* (atom | ignoredatom)* misc* EOF
        ;

atom    :
         misc* ATOMOPEN misc* statement misc* subject misc* predicate misc* objekt misc* ATOMCLOSE misc*
        ;

ignoredatom
        : misc* ATOMOPEN misc* statement misc* subject misc* ignoredpred misc* unreserved_content misc* ATOMCLOSE misc*
        ;

statement:
         STATEMENT
         ;


subject :
        INDOPEN subjectcontent INDCLOSE
        ;

predicate :
        INDOPEN verb INDCLOSE
        ;

objekt :
        INDOPEN objektcontent INDCLOSE
        ;

misc    :
        SEA_WS
        ;

ignoredpred
        :
        INDOPEN ignoredverb INDCLOSE
        ;

//-----------------------------------------------------------
nodeid  :
        N digit digit digit digit digit
        ;

subjectcontent
        :
        iri | nodeid | unreserved*
        ;

objektcontent
        :
        iri | nodeid | verb | xsd | owlrestriction | unreserved*
        ;

ignoredverb
        : rdfscomment |  rdfslabel | dcdescription | rdftype | seealso | rdfrest | skosdef | skospreflabel
        | skosaltlabel | skoshiddenlabel | skosnotation | annotateds | annotatedp | annotatedt | isdefinedby
        | versioninfo | deprecated | backcompatwith | incompatwith | priorversion | dcsource
        ;

verb
        : subpropertyof | subclassof | rdfsdomain | rdfsrange | ondatatype | owlwithrestrictions
        | equiclass | owlclass | rdfdescription | intersectionof
        | owlsvf | owlavf | onproperty | hasvalue | rdfsdatatype
        | minexclusive | maxexclusive | xsddatatype | funcproperty  | owlonclass
        | owlondatarange | owlqc | objectproperty | rdfnil | unionof | cardinality
        | hasself | owlmaxc | owlmaxqc | owlminc | owlminqc | onproperties | complementof
        | oneof | topop | bottomop | inverseof | topdp | bottomdp | datacomplementof | disjointwith
        | alldisjointclasses | owlmembers | disjointunionof | propertychainaxiom | equiproperty | pdisjointwith
        | alldisjointp | inversefuncp | reflexp | irreflexp | symmp | asymmp | transitivep | sameas | differentfrom
        | alldifferent | negpassert | sourceindividual | assertp | targetindividual | targetvalue | haskey
        | datatypep | annotationp | namedindividual | owlaxiom | owlannotation | rdfsliteral | owlrational
        | owlreal | rdfplainl | xmlliteral | rdflangrange
        ;
xsd
        : xsdvalue POWER POWER xsddatatype
        ;

xsdvalue
        : (PLUS|HYPHEN)* digit+ DOT? digit* | TRUE | FALSE
        ;

xsddatatype
        : XSD alpha+
        ;

unreserved_content
        : INDOPEN .*? INDCLOSE
        ;
//----------------------ignored functors---------------------------------

rdfscomment
        : RDFSCOMMENT
        ;

rdfslabel
        : RDFSLABEL
        ;

dcdescription
        : DCDESCRIPTION
        ;

rdftype
        : RDFTYPE
        ;

seealso
        : SEEALSO
        ;

rdfrest
        : RDFREST
        ;

skosdef : SKOSDEF
        ;

skospreflabel
        : SKOSPREFLABEL
        ;

skosaltlabel
        : SKOSALTLABEL
        ;

skoshiddenlabel
        : SKOSHIDDENLABEL
        ;

skosnotation
        : SKOSNOTATION
        ;

annotateds
        : ANNOTATEDS
        ;

annotatedp
        : ANNOTATEDP
        ;

annotatedt
        : ANNOTATEDT
        ;

isdefinedby
        : ISDEFINEDBY
        ;

versioninfo
        : VERSIONINFO
        ;

deprecated
        : DEPRECATED
        ;

backcompatwith
        : BACKCOMPATWITH
        ;

incompatwith
        : INCOMPATWITH
        ;

priorversion
        : PRIORVERSION
        ;

dcsource
        : DCSOURCE
        ;
//----------------------owl functors-------------------------------------
ondatatype
        : ONDATATYPE
        ;

owlwithrestrictions
        : WITHRESTRICTIONS
        ;

subpropertyof
        : SUBP
        ;

subclassof
        : SUBC
        ;

rdfsdomain
        : RDFSDOMAIN
        ;

rdfsrange
        : RDFSRANGE
        ;

equiclass
        : EQUICLASS
        ;

owlclass
        : OWLCLASS
        ;

rdfdescription
        : RDFDESCRIPTION
        ;

intersectionof
        : INTERSECTIONOF
        ;

owlsvf  : OWLSVF
        ;

owlavf  : OWLAVF
        ;

onproperty
        : ONP
        ;

hasvalue
        : HASVALUE
        ;

minexclusive
        : MINEXCLUSIVE
        ;

maxexclusive
        : MAXEXCLUSIVE
        ;

owlrestriction
        : OWLRESTRICTION
        ;

rdfsdatatype
        : RDFSDATATYPE
        ;

funcproperty
        : FUNCPROPERTY
        ;

owlondatarange
        : OWLONDATARANGE
        ;

owlonclass
        : OWLONCLASS
        ;
owlqc
        : OWLQC
        ;

objectproperty
        : OBJECTPROPERTY
        ;

rdfnil
        : RDFNIL
        ;

unionof
        : UNIONOF
        ;

cardinality
        : CARDINALITY
        ;

hasself : HASSELF
        ;

owlmaxc : OWLMAXC
        ;

owlmaxqc
        : OWLMAXQC
        ;

owlminc : OWLMINC
        ;

owlminqc
        : OWLMINQC
        ;

onproperties
        : ONPROPERTIES
        ;

complementof
        : COMPLEMENTOF
        ;

oneof   : ONEOF
        ;

topop   : TOPOP
        ;

bottomop: BOTTOMOP
        ;

inverseof
        : INVERSEOF
        ;

topdp   : TOPDP
        ;

bottomdp: BOTTOMDP
        ;

datacomplementof
        : DATACOMPLEMENTOF
        ;

disjointwith
        : DISJOINTWITH
        ;

alldisjointclasses
        : ALLDISJOINTCLASSES
        ;

owlmembers
        : OWLMEMBERS
        ;

disjointunionof
        : DISJOINTUNIONOF
        ;

propertychainaxiom
        : PROPERTYCHAINAXIOM
        ;

equiproperty
        : EQUIPROPERTY
        ;

pdisjointwith
        : PDISJOINTWITH
        ;

alldisjointp
        : ALLDISJOINTP
        ;

inversefuncp
        : INVERSEFUNCP
        ;

reflexp : REFLEXP
        ;

irreflexp
        : IRREFLEXP
        ;

symmp   : SYMMP
        ;

asymmp  : ASYMMP
        ;

transitivep
        : TRANSITIVEP
        ;

sameas  : SAMEAS
        ;

differentfrom
        : DIFFERENTFROM
        ;

alldifferent
        : ALLDIFFERENT
        ;

negpassert
        : NEGPASSERT
        ;

sourceindividual
        : SOURCEINDIVIDUAL
        ;

assertp : ASSERTP
        ;

targetindividual
        : TARGETINDIVIDUAL
        ;

targetvalue
        : TARGETVALUE
        ;

haskey  : HASKEY
        ;

datatypep
        : DATATYPEP
        ;

annotationp
        : ANNOTATIONP
        ;

namedindividual
        : NAMEDINDIVIDUAL
        ;

owlaxiom
        : OWLAXIOM
        ;

owlannotation
        : OWLANNOTATION
        ;

rdfsliteral
        : RDFSLITERAL
        ;

owlrational
        : OWLRATIONAL
        ;

owlreal : OWLREAL
        ;

rdfplainl
        : RDFPLAINL
        ;

xmlliteral
        : XMLLITERAL
        ;

rdflangrange
        : RDFLANGRANGE
        ;
//-----------------------------------------------------------------------
/// IRI            = scheme ":" ihier-part [ "?" iquery ] [ "#" ifragment ]
iri
   : scheme COL ihier_part (QMARK iquery)? (HASH ifragment)?
   ;

/// ihier-part     = "//" iauthority ipath-abempty///                / ipath-absolute///                / ipath-rootless///                / ipath-empty
ihier_part
   : FSLASH2 iauthority ipath_abempty
   | ipath_absolute
   | ipath_rootless
   | ipath_empty
   ;

/// IRI-reference  = IRI / irelative-ref
iri_reference
   : iri
   | irelative_ref
   ;

/// absolute-IRI   = scheme ":" ihier-part [ "?" iquery ]
absolute_iri
   : scheme COL ihier_part (QMARK iquery)?
   ;

/// irelative-ref  = irelative-part [ "?" iquery ] [ "#" ifragment ]
irelative_ref
   : irelative_part (QMARK iquery)? (HASH ifragment)?
   ;

/// irelative-part = "//" iauthority ipath-abempty///                     / ipath-absolute///                     / ipath-noscheme///                     / ipath-empty
irelative_part
   : FSLASH2 iauthority ipath_abempty
   | ipath_absolute
   | ipath_noscheme
   | ipath_empty
   ;

/// iauthority     = [ iuserinfo "@" ] ihost [ ":" port ]
iauthority
   : (iuserinfo AT)? ihost (COL port)?
   ;

/// iuserinfo      = *( iunreserved / pct-encoded / sub-delims / ":" )
iuserinfo
   : (iunreserved | pct_encoded | sub_delims | COL)*
   ;

/// ihost          = IP-literal / IPv4address / ireg-name
ihost
   : ip_literal
   | ip_v4_address
   | ireg_name
   ;

/// ireg-name      = *( iunreserved / pct-encoded / sub-delims )
ireg_name
   : (iunreserved | pct_encoded | sub_delims)*
   ;

/// ipath          = ipath-abempty   ; begins with "/" or is empty///                / ipath-absolute  ; begins with "/" but not "//"///                / ipath-noscheme  ; begins with a non-colon segment///                / ipath-rootless  ; begins with a segment///                / ipath-empty     ; zero characters
ipath
   : ipath_abempty
   | ipath_absolute
   | ipath_noscheme
   | ipath_rootless
   | ipath_empty
   ;

/// ipath-abempty  = *( "/" isegment )
ipath_abempty
   : (FSLASH isegment)*
   ;

/// ipath-absolute = "/" [ isegment-nz *( "/" isegment ) ]
ipath_absolute
   : FSLASH (isegment_nz (FSLASH isegment)*)?
   ;

/// ipath-noscheme = isegment-nz-nc *( "/" isegment )
ipath_noscheme
   : isegment_nz_nc (FSLASH isegment)*
   ;

/// ipath-rootless = isegment-nz *( "/" isegment )
ipath_rootless
   : isegment_nz (FSLASH isegment)*
   ;

/// ipath-empty    = 0<ipchar>
ipath_empty
   :/* nothing */
   ;

/// isegment       = *ipchar
isegment
   : ipchar*
   ;

/// isegment-nz    = 1*ipchar
isegment_nz
   : ipchar +
   ;

/// isegment-nz-nc = 1*( iunreserved / pct-encoded / sub-delims / "@" )///                ; non-zero-length segment without any colon ":"
isegment_nz_nc
   : (iunreserved | pct_encoded | sub_delims | AT) +
   ;

/// ipchar         = iunreserved / pct-encoded / sub-delims / ":" / "@"
ipchar
   : iunreserved
   | pct_encoded
   | sub_delims
   | (COL | AT)
   ;

/// iquery         = *( ipchar / iprivate / "/" / "?" )
iquery
   : (ipchar | (IPRIVATE | FSLASH | QMARK))*
   ;

/// ifragment      = *( ipchar / "/" / "?" )
ifragment
   : (ipchar | (FSLASH | QMARK))*
   ;

/// iunreserved    = ALPHA / DIGIT / "-" / "." / "_" / "~" / ucschar
iunreserved
   : alpha
   | digit
   | (HYPHEN | DOT | USCORE | TILDE | UCSCHAR)
   ;

/// scheme         = ALPHA *( ALPHA / DIGIT / "+" / "-" / "." )
scheme
   : alpha (alpha | digit | (PLUS | HYPHEN | DOT))*
   ;

/// port           = *DIGIT
port
   : digit*
   ;

/// IP-literal     = "[" ( IPv6address / IPvFuture  ) "]"
ip_literal
   : OBRACK (ip_v6_address | ip_v_future) CBRACK
   ;

/// IPvFuture      = "v" 1*HEXDIG "." 1*( unreserved / sub-delims / ":" )
ip_v_future
   : V hexdig + DOT (unreserved | sub_delims | COL) +
   ;

/// IPv6address    =                            6( h16 ":" ) ls32///                /                       "::" 5( h16 ":" ) ls32///                / [               h16 ] "::" 4( h16 ":" ) ls32///                / [ *1( h16 ":" ) h16 ] "::" 3( h16 ":" ) ls32///                / [ *2( h16 ":" ) h16 ] "::" 2( h16 ":" ) ls32///                / [ *3( h16 ":" ) h16 ] "::"    h16 ":"   ls32///                / [ *4( h16 ":" ) h16 ] "::"              ls32///                / [ *5( h16 ":" ) h16 ] "::"              h16///                / [ *6( h16 ":" ) h16 ] "::"
ip_v6_address
   : h16 COL h16 COL h16 COL h16 COL h16 COL h16 COL ls32
   | COL2 h16 COL h16 COL h16 COL h16 COL h16 COL ls32
   | h16? COL2 h16 COL h16 COL h16 COL h16 COL ls32
   | ((h16 COL)? h16)? COL2 h16 COL h16 COL h16 COL ls32
   | (((h16 COL)? h16 COL)? h16)? COL2 h16 COL h16 COL ls32
   | ((((h16 COL)? h16 COL)? h16 COL)? h16)? COL2 h16 COL ls32
   | (((((h16 COL)? h16 COL)? h16 COL)? h16 COL)? h16)? COL2 ls32
   | ((((((h16 COL)? h16 COL)? h16 COL)? h16 COL)? h16 COL)? h16)? COL2 h16
   | (((((((h16 COL)? h16 COL)? h16 COL)? h16 COL)? h16 COL)? h16 COL)? h16)? COL2
   ;

/// h16            = 1*4HEXDIG
h16
   : hexdig hexdig hexdig hexdig
   | hexdig hexdig hexdig
   | hexdig hexdig
   | hexdig
   ;

/// ls32           = ( h16 ":" h16 ) / IPv4address
ls32
   : h16 COL h16
   | ip_v4_address
   ;

/// IPv4address    = dec-octet "." dec-octet "." dec-octet "." dec-octet
ip_v4_address
   : dec_octet DOT dec_octet DOT dec_octet DOT dec_octet
   ;

/// dec-octet      = DIGIT                 ; 0-9///                / %x31-39 DIGIT         ; 10-99///                / "1" 2DIGIT            ; 100-199///                / "2" %x30-34 DIGIT     ; 200-249///                / "25" %x30-35          ; 250-255
dec_octet
   : digit
   | non_zero_digit digit
   | D1 digit digit
   | D2 (D0 | D1 | D2 | D3 | D4) digit
   | D2 D5 (D0 | D1 | D2 | D3 | D4 | D5)
   ;

/// pct-encoded    = "%" HEXDIG HEXDIG
pct_encoded
   : PERCENT hexdig hexdig
   ;

/// unreserved     = ALPHA / DIGIT / "-" / "." / "_" / "~"
unreserved
   : alpha
   | digit
   | (HYPHEN | DOT | USCORE | TILDE)
   ;

/// reserved       = ruleml_parser-delims / sub-delims
reserved
   : gen_delims
   | sub_delims
   ;

/// ruleml_parser-delims     = ":" / "/" / "?" / "#" / "[" / "]" / "@"
gen_delims
   : COL
   | FSLASH
   | QMARK
   | HASH
   | OBRACK
   | CBRACK
   | AT
   ;

/// sub-delims     = "!" / "$" / "&" / "'" / "(" / ")"///                / "*" / "+" / "," / ";" / "="
sub_delims
   : EXCL
   | DOLLAR
   | AMP
   | SQUOTE
   | OPAREN
   | CPAREN
   | STAR
   | PLUS
   | COMMA
   | SCOL
   | EQUALS
   ;

alpha
   : A
   | B
   | C
   | D
   | E
   | F
   | G
   | H
   | I
   | J
   | K
   | L
   | M
   | N
   | O
   | P
   | Q
   | R
   | S
   | T
   | U
   | V
   | W
   | X
   | Y
   | Z
   ;

hexdig
   : digit
   | (A | B | C | D | E | F)
   ;

digit
   : D0
   | non_zero_digit
   ;

non_zero_digit
   : D1
   | D2
   | D3
   | D4
   | D5
   | D6
   | D7
   | D8
   | D9
   ;