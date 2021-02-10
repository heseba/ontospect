<?xml version="1.0"?> 

<!DOCTYPE uridef[
  <!ENTITY rdf "http://www.w3.org/1999/02/22-rdf-syntax-ns">
  <!ENTITY rdfs "http://www.w3.org/2000/01/rdf-schema">
  <!ENTITY owl "http://www.w3.org/2002/07/owl">
  <!ENTITY xsd "http://www.w3.org/2001/XMLSchema">
  <!ENTITY nbsp "&#160;">
]>

<xsl:stylesheet version="2.0"
 xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
 xmlns:rdf="&rdf;#"
 xmlns:rdfs="&rdfs;#"
 xmlns:owl="&owl;#"
 xmlns:xsd="&xsd;#"
 exclude-result-prefixes="rdf rdfs owl xsd"
 >
 
  <xsl:output method="xml" indent="yes" omit-xml-declaration="yes"/>

  <xsl:template match="/"><xsl:apply-templates /></xsl:template>
  <xsl:template match="rdf:RDF"><xsl:apply-templates /></xsl:template>
  

  <!-- transform RDF snytax into Jess triples - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -->
  
  <!-- declare root class instances -->
  <xsl:template match="/rdf:RDF/*">
    <xsl:call-template name="ABox-class"/>
  </xsl:template>


  <!-- named templates - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -->

  <!-- process an instance of a class -->
  <xsl:template name="ABox-class" >

 <Atom>
  <Rel>statement</Rel>
  <Ind><xsl:call-template name="get-ID"/></Ind>
  <Ind>rdf:type</Ind>
  <Ind><xsl:value-of select="name(.)"/></Ind>
 </Atom>

  <xsl:for-each select="*"><xsl:call-template name="ABox-property"/></xsl:for-each> 
  </xsl:template>

  <!-- process an instance of a property -->
  <xsl:template name="ABox-property" >
    <xsl:choose>
      <xsl:when test='count(*)=1'> <!-- has element nodes as children -->
        <xsl:call-template name="process-objectproperty-instance"/>
      </xsl:when>
      <xsl:when test='count(text())=1'> <!-- has text nodes as children -->
        <xsl:call-template name="process-dataproperty-instance"/>
      </xsl:when>
      <xsl:when test='count(*)>1'> <!-- has a collection -->
        <xsl:for-each select="*"><xsl:call-template name="process-collection"/></xsl:for-each>
      </xsl:when>
      <xsl:when test='@rdf:resource'> <!-- has a reference -->
        <xsl:call-template name="process-referenceproperty-instance"/>
      </xsl:when>
    </xsl:choose>
  </xsl:template>

  <!-- process an instance of a objectproperty -->
  <xsl:template name="process-objectproperty-instance" >

 <Atom>
  <Rel>statement</Rel>
  <Ind><xsl:call-template name="get-father-ID"/></Ind>
  <Ind><xsl:value-of select="name(.)"/></Ind>
  <Ind><xsl:call-template name="get-child-ID"/></Ind>
 </Atom>

  <xsl:for-each select="*[position()=1]"><xsl:call-template name="ABox-class"/></xsl:for-each>
  </xsl:template>

  <!-- process a collection -->
  <xsl:template name="process-collection" >

 <Atom>
  <Rel>statement</Rel>
  <Ind><xsl:call-template name="get-grandfather-ID"/></Ind>
  <Ind><xsl:value-of select="name(..)"/></Ind>
  <Ind><xsl:call-template name="get-ID"/></Ind>
 </Atom>

  <xsl:call-template name="ABox-class"/>
  </xsl:template>
  
  <!-- process an instance of a dataproperty -->
  <xsl:template name="process-dataproperty-instance" >

 <Atom>
  <Rel>statement</Rel>
  <Ind><xsl:call-template name="get-father-ID"/></Ind>
  <Ind><xsl:value-of select="name(.)"/></Ind>
  <Ind><xsl:call-template name="get-datavalue"/></Ind>
 </Atom>

  </xsl:template>

  <!-- process an instance of a property referencing a resource in its range-->
  <xsl:template name="process-referenceproperty-instance" >

 <Atom>
  <Rel>statement</Rel>
  <Ind><xsl:call-template name="get-father-ID"/></Ind>
  <Ind><xsl:value-of select="name(.)"/></Ind>
  <Ind><xsl:call-template name="get-namespace-ID"><xsl:with-param name="id"><xsl:value-of select="@rdf:resource"/></xsl:with-param></xsl:call-template> </Ind>
 </Atom>

  </xsl:template>


  <!-- named templates - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -->



  <!-- get ID or About of the current node -->
  <xsl:template name="get-ID" >
    
    <xsl:choose>
      <xsl:when test="@rdf:ID">
        <xsl:call-template name="get-namespace-ID"><xsl:with-param name="id"><xsl:value-of select="@rdf:ID"/></xsl:with-param></xsl:call-template> 
      </xsl:when>
      <xsl:when test="@rdf:about">
        <xsl:call-template name="get-namespace-ID"><xsl:with-param name="id"><xsl:value-of select="@rdf:about"/></xsl:with-param></xsl:call-template> 
      </xsl:when>
      <xsl:otherwise>
        <xsl:value-of select="generate-id(.)"/>
      </xsl:otherwise>
    </xsl:choose> 
  </xsl:template>


  <!-- get datavalue of the current node -->
  <xsl:template name="get-datavalue" >
    
    <xsl:choose>
      <xsl:when test="@rdf:datatype">
        <xsl:value-of select="concat(normalize-space(.),'^^xsd:',substring-after(@rdf:datatype,'#'))"/>
      </xsl:when>
      <xsl:otherwise>
        <xsl:value-of select="normalize-space(.)"/>
      </xsl:otherwise>
    </xsl:choose> 
  </xsl:template>
    
  <!-- get the ID or About of the parent node -->
  <xsl:template name="get-father-ID" >
    
    <xsl:choose>
      <xsl:when test="../@rdf:ID">
        <xsl:call-template name="get-namespace-ID"><xsl:with-param name="id"><xsl:value-of select="../@rdf:ID"/></xsl:with-param></xsl:call-template> 
      </xsl:when>
      <xsl:when test="../@rdf:about">
        <xsl:call-template name="get-namespace-ID"><xsl:with-param name="id"><xsl:value-of select="../@rdf:about"/></xsl:with-param></xsl:call-template> 
      </xsl:when>
      <xsl:otherwise>
        <xsl:value-of select="generate-id(..)"/>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:template>
  
  <!-- get the ID or About of the grandparent node -->
  <xsl:template name="get-grandfather-ID" >
    
    <xsl:choose>
      <xsl:when test="../../@rdf:ID">
        <xsl:call-template name="get-namespace-ID"><xsl:with-param name="id"><xsl:value-of select="../../@rdf:ID"/></xsl:with-param></xsl:call-template> 
      </xsl:when>
      <xsl:when test="../../@rdf:about">
        <xsl:call-template name="get-namespace-ID"><xsl:with-param name="id"><xsl:value-of select="../../@rdf:about"/></xsl:with-param></xsl:call-template> 
      </xsl:when>
      <xsl:otherwise>
        <xsl:value-of select="generate-id(../..)"/>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:template>
  
  
  <!-- get the ID or About of the first child  -->

  <xsl:template name="get-child-ID" >
    <xsl:choose>
      <xsl:when test="@rdf:resource">
        <xsl:call-template name="get-namespace-ID"><xsl:with-param name="id"><xsl:value-of select="@rdf:resource"/></xsl:with-param></xsl:call-template> 
      </xsl:when>
      <xsl:when test="*[position()=1]/@rdf:ID">
        <xsl:call-template name="get-namespace-ID"><xsl:with-param name="id"><xsl:value-of select="*[position()=1]/@rdf:ID"/></xsl:with-param></xsl:call-template> 
      </xsl:when>
      <xsl:when test="*[position()=1]/@rdf:about">
        <xsl:call-template name="get-namespace-ID"><xsl:with-param name="id"><xsl:value-of select="*[position()=1]/@rdf:about"/></xsl:with-param></xsl:call-template> 
      </xsl:when>
      <xsl:otherwise>
        <xsl:value-of select="generate-id(*[position()=1])"/>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:template>
  
  <xsl:template name="get-namespace-ID" >
   <xsl:param name="id" />
    <xsl:choose>
      <xsl:when test="starts-with($id,'&rdf;#')">
        <xsl:value-of select="concat('rdf:',substring-after($id,'#'))"/> 
      </xsl:when>
      <xsl:when test="starts-with($id,'&rdfs;#')">
        <xsl:value-of select="concat('rdfs:',substring-after($id,'#'))"/> 
      </xsl:when>
      <xsl:when test="starts-with($id,'&owl;#')">
        <xsl:value-of select="concat('owl:',substring-after($id,'#'))"/> 
      </xsl:when>  
      <xsl:when test="starts-with($id,'&xsd;#')">
        <xsl:value-of select="concat('xsd:',substring-after($id,'#'))"/> 
      </xsl:when> 
      <xsl:otherwise>
		<xsl:value-of select="$id"/>
	  </xsl:otherwise>                    
    </xsl:choose>
  </xsl:template>
    
  <xsl:template match="*" />
  
   
</xsl:stylesheet>