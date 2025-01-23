#!pip install bs4
#!pip install lxml
#!pip install langdetect

import os
from bs4 import BeautifulSoup
import mysql.connector
from langdetect import detect
import re

original_clefip2011_path="C:/Users/User/Desktop/WIPO-alpha_MySQL_Database_Creation/wipo-alpha/test"

for folder_level_1 in os.listdir(original_clefip2011_path): #alphatest
    for folder_level_2 in os.listdir(original_clefip2011_path+"/"+folder_level_1): #A
        for folder_level_3 in os.listdir(original_clefip2011_path+"/"+folder_level_1+"/"+folder_level_2): #01
            for folder_level_4 in os.listdir(original_clefip2011_path+"/"+folder_level_1+"/"+folder_level_2+"/"+folder_level_3): #B
                for folder_level_5 in os.listdir(original_clefip2011_path+"/"+folder_level_1+"/"+folder_level_2+"/"+folder_level_3+"/"+folder_level_4): #003
                
                                       
                    title_en_text  = ''     
                    abstract_en_text   = ''                                        
                    description_en_text = ''                                                   
                    claims_en_text = ''


                    for files in os.listdir(original_clefip2011_path+"/"+folder_level_1+"/"+folder_level_2+"/"+folder_level_3+"/"+folder_level_4+"/"+folder_level_5):
                        #print(files)        
                                                                       
                        # Extract all content 

                        content = open(original_clefip2011_path+"/"+folder_level_1+"/"+folder_level_2+"/"+folder_level_3+"/"+folder_level_4+"/"+folder_level_5+"/"+files,'r',encoding='iso-8859-1').read()
                        soup = BeautifulSoup(content, 'lxml')
                        
                        # Get doc info
                          
                        country = ''
                        kind = ''
                        doc_number = 0                  
                        applicant_number = ''
                        publication_number = ''

                        
                        document_info = soup.find_all("record")
                        country=document_info[0]['cy']
                        kind=document_info[0]['kind']
                        doc_number=int(document_info[0]['dnum'])                            
                        applicant_number=document_info[0]['an']                           
                        publication_number=document_info[0]['pn']                            
                                                                       
                        # Get main classification
                                                   
                        main_classification=soup.find_all('ipcs')
                        code_main=main_classification[0]['mc']                        
                        main_section=code_main[0]                                                       
                        main_class=code_main[:3]   
                        main_subclass=code_main[:4]                            
                        main_group=code_main[:7]
                        main_subgroup=code_main

                                                
                        # Get further classification   
                            
                        further_section_list = []
                        further_class_list = []
                        further_subclass_list=[]
                        further_group_list=[]
                        further_subgroup_list=[]
                              
                        for further_classifications in soup.find_all('ipcs'):
                            for further_classification in soup.find_all('ipc'):
                                code_further=further_classification['ic']
                                
                                further_section=code_further[0]  
                                further_section_list.append(further_section) if further_section not in further_section_list else further_section_list
                                                     
                                further_class=code_further[:3]   
                                further_class_list.append(further_class) if further_class not in further_class_list else further_class_list
                                
                                further_subclass=code_further[:4]                            
                                further_subclass_list.append(further_subclass) if further_subclass not in further_subclass_list else further_subclass_list
                                
                                further_group=code_further[:7]
                                further_group_list.append(further_group) if further_group not in further_group_list else further_group_list
                                
                                further_subgroup=code_further
                                further_subgroup_list.append(further_subgroup) if further_subgroup not in further_subgroup_list else further_subgroup_list
                                              
                       # Get applicants
                        
                        applicant_name_list = []
                                    
                        for applicant_all_info in soup.find_all('pas'):
                            for applicant_single_name in applicant_all_info.find_all('pa'):
                                applicant_name_text=applicant_single_name.getText().lower().replace('"', ' ')
                                #applicant_name_text=applicant_name_text.replace('&', 'and').replace('corporation','corp').replace(',', '').replace('.', '').replace('-', ' ')
                                applicant_name_list.append(applicant_name_text) if applicant_name_text not in applicant_name_list else applicant_name_list
                        applicant_name_list = "; ".join(applicant_name_list)

                        # Get inventors
                        
                        inventor_name_list = []
                                    
                        for inventor_all_info in soup.find_all('ins'):
                            for inventor_single_name in inventor_all_info.find_all('in'):
                                inventor_name_text=inventor_single_name.getText().lower().replace('"', ' ')
                                #inventor_name_text=inventor_name_text.replace('&', 'and').replace('corporation','corp').replace(',', '').replace('.', '').replace('-', ' ')
                                inventor_name_list.append(inventor_name_text) if inventor_name_text not in inventor_name_list else inventor_name_list
                        inventor_name_list = "; ".join(inventor_name_list)
                                    
                       # Get title
                                                                
                        title_en=soup.find('ti', attrs={'xml:lang':'EN'})
                        if title_en != None:
                            title_en=title_en.getText().lower().replace('"', ' ')
                            title_en=" ".join(title_en.split())
                            title_en_text=title_en  

                        # Get abstract
                        
                        abstract_en=soup.find('ab', attrs={'xml:lang':'EN'})
                        if abstract_en != None:
                            abstract_en=abstract_en.getText().lower().replace('"', ' ')
                            abstract_en=" ".join(abstract_en.split())
                                        
                            if len(abstract_en) > 0:                                
                                abstract_en_exist=1
                                abstract_en_text=abstract_en
                            else:
                                print(files ,"error - no features in abstract") 


                        # Get description
                                                                            
                        description_en = soup.find('txt', attrs={'xml:lang':'EN'})
                        if description_en != None:
                            description_en=description_en.getText().lower().replace('"', ' ')
                            description_en=" ".join(description_en.split())
                            len_description_en=len(description_en)                           
                            if len_description_en > 0:
                                description_en_exist=1
                                description_en_text=description_en 
                                if len_description_en > 981237:
                                    description_en_text=description_en_text[0:5000]
                            else:
                                print(files,"error - no features in description")  
                        
                                      
                        # Get all claims
                                                           
                        claims_en = soup.find('cl', attrs={'xml:lang':'EN'})
                        if claims_en != None:
                            claims_en=claims_en.getText().lower().replace('"', ' ')
                            claims_en=" ".join(claims_en.split())                          
                            len_cl_en=len(claims_en)
                            if  len_cl_en > 0:
                                    claims_en_exist=1
                                    claims_en_text=claims_en
                                    if len_cl_en > 200000:
                                        claims_en_text=claims_en_text[0:5000]
                            else:
                                print(files,"error - no features in claims") 
                        
                        #print(files, len(abstract_en_text), "\n", len(description_en_text), "\n", len(claims_en_text))                                                                 
                           
######################## Connect to the datbase - fill in the patents and patents_text tables ########################
                            
                        mydb = mysql.connector.connect(
                            host="localhost",    
                            user="root",        
                            password="admin",
                            database="wipo_alpha_test"
                            )
                        
                        mycursor = mydb.cursor()
                                
                        # Pass the patent info
                        
                        sql = "INSERT INTO patents (files, country, kind, doc_number, \
                        applicant_number, publication_number, \
                        applicant_name_list, inventor_name_list, \
                        title_en_text, abstract_en_exist, description_en_exist, claims_en_exist)\
                         VALUES (%s, %s, %s, %s, \
                        %s, %s,\
                        %s, %s, \
                        %s, %s, %s, %s)"
  
                        
                        val = (files, country, kind, doc_number, \
                        applicant_number, publication_number, \
                        applicant_name_list, inventor_name_list,  \
                        title_en_text, abstract_en_exist, description_en_exist, claims_en_exist)                 
                                               
                        mycursor.execute(sql, val)
                        mydb.commit()
                        

                        sql0 = "INSERT INTO patents_en_text (files, \
                        abstract_en_text, description_en_text, claims_en_text) VALUES (%s, \
                        %s, %s, %s)"
                            
               
                        val0 = (files,\
                        abstract_en_text, description_en_text, claims_en_text)  
                                                                                
                        mycursor.execute(sql0, val0)
                        mydb.commit()
                                

######################## Connect to the datbase - fill in the patent_ipc_codes table ########################
                        
                                                
                        # Main code    

                        further=False if main_section not in further_section_list else True
                                
                        sql6 = "INSERT INTO patent_ipc_codes (files, \
                        ipcr_code, level, main, further)\
                        VALUES (%s, %s, \
                        %s, %s, %s)"
                                    
                        val6 = (files, main_section, 1, True, further) 
                        mycursor.execute(sql6, val6)
                        mydb.commit()
                        
                        ###
                        further=False if main_class not in further_class_list else True
                                
                        sql7 = "INSERT INTO patent_ipc_codes (files, \
                        ipcr_code, level, main, further)\
                        VALUES (%s, %s, \
                        %s, %s, %s)"
                                    
                        val7 = (files, main_class, 2, True, further) 
                        mycursor.execute(sql7, val7)
                        mydb.commit()
                                
                        ##        
                        further=False if main_subclass not in further_subclass_list else True
                                
                        sql8 = "INSERT INTO patent_ipc_codes (files, \
                        ipcr_code, level, main, further)\
                        VALUES (%s, %s, \
                        %s, %s, %s)"
                                    
                        val8 = (files, main_subclass, 3, True, further) 
                        mycursor.execute(sql8, val8)
                        mydb.commit()
                                
                        ##        
                        further_group=False if main_group not in further_group_list else True
                                
                        sql9 = "INSERT INTO patent_ipc_codes (files, \
                        ipcr_code, level, main, further)\
                        VALUES (%s, %s, \
                        %s, %s, %s)"
                                    
                        val9 = (files, main_group, 4, True, further) 
                        mycursor.execute(sql9, val9)
                        mydb.commit()
                                
                        ##
                        further=False if main_subgroup not in further_subgroup_list else True
                                
                        sql10 = "INSERT INTO patent_ipc_codes (files, \
                        ipcr_code, level, main, further)\
                        VALUES (%s, %s, \
                        %s, %s, %s)"
                                    
                        val10 = (files, main_subgroup, 5, True, further) 
                        mycursor.execute(sql10, val10)
                        mydb.commit()
                                
                        # When further code is not listed in the main code(s)

                        for further_section in further_section_list:
                            if further_section!=main_section:
                                
                                sql11 = "INSERT INTO patent_ipc_codes (files, \
                                ipcr_code, level, main, further)\
                                VALUES (%s, %s, \
                                %s, %s, %s)"
                                    
                                val11 = (files, further_section, 1, False, True) 
                                mycursor.execute(sql11, val11)
                                mydb.commit()
                                
                                
                        for further_class in further_class_list:
                            if further_class!=main_class:
                                
                                sql12 = "INSERT INTO patent_ipc_codes (files, \
                                ipcr_code, level, main, further)\
                                VALUES (%s, %s, \
                                %s, %s, %s)"
                                    
                                val12 = (files, further_class, 2, False, True) 
                                mycursor.execute(sql12, val12)
                                mydb.commit()
                                
                        for further_subclass in further_subclass_list:
                            if further_subclass!=main_subclass:
                                
                                sql13 = "INSERT INTO patent_ipc_codes (files, \
                                ipcr_code, level, main, further)\
                                VALUES (%s, %s, \
                                %s, %s, %s)"
                                    
                                val13 = (files, further_subclass, 3, False, True) 
                                mycursor.execute(sql13, val13)
                                mydb.commit()
                                
                        for further_group in further_group_list:
                            if further_group!=main_group:
                                
                                sql14 = "INSERT INTO patent_ipc_codes (files, \
                                ipcr_code, level, main, further)\
                                VALUES (%s, %s, \
                                %s, %s, %s)"
                                    
                                val14 = (files, further_group, 4, False, True) 
                                mycursor.execute(sql14, val14)
                                mydb.commit()
                                
                        for further_subgroup in further_subgroup_list:
                            if further_subgroup!=main_subgroup:
                                
                                sql15 = "INSERT INTO patent_ipc_codes (files, \
                                ipcr_code, level, main, further)\
                                VALUES (%s, %s, \
                                %s, %s, %s)"
                                    
                                val15 = (files, further_subgroup, 5, False, True) 
                                mycursor.execute(sql15, val15)
                                mydb.commit()
                                
                        mycursor.close()
                        mydb.close()