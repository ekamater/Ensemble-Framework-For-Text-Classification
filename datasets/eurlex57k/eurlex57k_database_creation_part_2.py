#!pip install bs4
#!pip install lxml
#!pip install langdetect

import os
from bs4 import BeautifulSoup
import mysql.connector
from langdetect import detect
import re
import json

original_clefip2011_path="/eurlex57k/dataset/dev"

title_text  = ''     
header_text  = ''
recitals_text   = ''                                        
main_body_text = ''                                                   
attachments_text = ''

for files in os.listdir(original_clefip2011_path):
    print(files)        
                                                                       
    # Extract all content 

    content = open(original_clefip2011_path+"/"+files,'r',encoding='iso-8859-1').read()
    soup = BeautifulSoup(content, 'html.parser')
                        
    # Get doc info
    recitals_exist=0
    main_body_exist=0
    attachments_exist = 0
    celex_id=''
    uri = ''
    type_1 = ''
    concepts = ''
    #document_info = soup.find_all("type")
    document_info = json.loads(soup.text)

    #Get title
    title=document_info['title']
    if title != None:
        title=title.lower().replace('"', ' ').replace(';', ' ')
        title=" ".join(title.split())
        title_text=title   

    #Get header
    header=document_info['header']
    if header != None:
        header=header.lower().replace('"', ' ').replace(';', ' ')
        header=" ".join(header.split())
        header_text=header 

    #Get recitals
    recitals=document_info['recitals']
    if recitals != None:
        recitals_exist=1
        recitals=recitals.lower().replace('"', ' ').replace(';', ' ')
        recitals=" ".join(recitals.split())
        recitals_text=recitals 
        
    #Get main_body
    main_body=document_info['main_body']
    if main_body != None:
        main_body_exist=1
        main_body=recitals.lower().replace('"', ' ').replace(';', ' ')
        main_body=" ".join(main_body.split())
        main_body_text=main_body 
        
    #Get attachments
    attachments=document_info['attachments']
    if attachments != None:
        attachments_exist=1
        attachments=attachments.lower().replace('"', ' ').replace(';', ' ')
        attachments=" ".join(attachments.split())
        attachments_text=attachments 

        
    celex_id=document_info['celex_id']
    uri = document_info['uri']
    type_1 = document_info['type']
    
    concepts_list = []                                                       
    i=0
    number_of_concepts=len(document_info['concepts'])        
    for i in range (number_of_concepts):
        concept = document_info['concepts'][i]
        concepts_list.append(concept) if concept not in concepts_list else concepts_list
        #print(concept, concepts_list)
                       
######################## Connect to the datbase - fill in the patents and documents tables ########################
                            
    mydb = mysql.connector.connect(
        host="localhost",    
        user="root",        
        password="admin",
        database="eurlex57K_dev"
        )
                            
    mycursor = mydb.cursor()
                                    
    # Pass the patent info
                            
    sql = "INSERT INTO documents (celex_id, uri, type_1, title_text, header_text, \
        recitals_text, main_body_text, attachments_text)\
        VALUES (%s, %s, %s, %s, %s,\
                %s, %s, %s)"
                             
    val = (celex_id, uri, type_1, title_text, header_text, recitals_text, main_body_text, attachments_text)            
    
    mycursor.execute(sql, val)
    mydb.commit()
                                    
    ######################## Connect to the datbase - fill in the document_concepts table ########################

    for concept in concepts_list:
                                       
        sql1 = "INSERT INTO document_concepts (celex_id, concept) VALUES (%s, %s)"
                                    
        val1 = (celex_id, concept) 
    
        mycursor.execute(sql1, val1)
        mydb.commit()
    
    mycursor.close()
    mydb.close()