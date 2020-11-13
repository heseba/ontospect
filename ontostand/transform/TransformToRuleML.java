/*
 * Created on 08.01.2005
 *
 * TODO To change the template for this generated file go to
 * Window - Preferences - Java - Code Style - Code Templates
 */

/**
 * @author mei, yichen
 *
 * TODO To change the template for this generated type comment go to
 * Window - Preferences - Java - Code Style - Code Templates
 */
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

import javax.xml.transform.Transformer;
import javax.xml.transform.TransformerConfigurationException;
import javax.xml.transform.TransformerException;
import javax.xml.transform.TransformerFactory;
import javax.xml.transform.stream.StreamResult;
import javax.xml.transform.stream.StreamSource;




public class TransformToRuleML {


	public static void main(String[] args)  throws TransformerException, TransformerConfigurationException,
    FileNotFoundException, IOException
	{
        String path = "ontostand/data/preprocessed/" + args[0] + "/";
        File file = new File(path);   
        File[] array = file.listFiles();
        for(int i=0;i<array.length;i++)
        {   
            if(array[i].isFile())//file
            {   
            String fileName = array[i].getName().replaceAll("[.][^.]+$", "");
            String xmlFileName = "ontostand/data/preprocessed/" + args[0] + "/" +fileName+".xml";
            String xslFileName = "ontostand/transform/OWL2RuleML.xsl";
            String outOFxslFileName = "ontostand/data/transformed/" + args[0] + "/" +fileName+".ruleml";
        
            // long startTime = System.currentTimeMillis();
            // System.out.println("start: " + startTime);
            
            TransformerFactory tFactory = TransformerFactory.newInstance();
            Transformer transformer = tFactory.newTransformer(new StreamSource(xslFileName));
            FileOutputStream fos = new FileOutputStream(outOFxslFileName);
            transformer.transform(new StreamSource(xmlFileName), new StreamResult(fos));
            fos.close();
            // System.out.println("************* The result is in " + outOFxslFileName + " *************");

            // long endOfXSLT = System.currentTimeMillis();
            // System.out.println("end : " + endOfXSLT);
            // System.out.println("XSLT: " + (endOfXSLT-startTime)); 
  
            }
  
        }
 	    System.out.println("************* Transform complete! ********************");
	}
}

