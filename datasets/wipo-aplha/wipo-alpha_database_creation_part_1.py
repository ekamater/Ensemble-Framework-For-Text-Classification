#!pip install mysql-connector-python 

import mysql.connector

steps=[4] #1: create the database, 2: create the tables 

for step in steps:
    
    if step==1:
        mydb = mysql.connector.connect(
            host="localhost",    
            user="root",        
            password="admin"
            )
        mycursor = mydb.cursor()

        mycursor.execute("CREATE DATABASE wipo_alpha_test CHARACTER SET utf8 COLLATE utf8_general_ci")
        
    elif step==2:
        mydb = mysql.connector.connect(
            host="localhost",    
            user="root",        
            password="admin",
            database="wipo_alpha_test",
            )
            
        mycursor = mydb.cursor()
        
        mycursor.execute("CREATE TABLE patents (files VARCHAR(30), country VARCHAR(3), kind VARCHAR(3),\
                        doc_number INTEGER, applicant_number VARCHAR(30), publication_number VARCHAR(30), \
                        applicant_name_list TEXT, inventor_name_list TEXT, \
                        title_en_text TEXT, abstract_en_exist INTEGER, description_en_exist INTEGER,\
                        claims_en_exist INTEGER, PRIMARY KEY (files))")

        mycursor.execute("CREATE TABLE patents_en_text (files VARCHAR(30), FOREIGN KEY (files) REFERENCES patents(files), \
                         abstract_en_text TEXT, description_en_text MEDIUMTEXT, claims_en_text MEDIUMTEXT)")
                    
        mycursor.execute("CREATE TABLE patent_ipc_codes (files VARCHAR(30), FOREIGN KEY (files) REFERENCES patents(files), \
                         ipcr_code VARCHAR(20), level INTEGER, main boolean, further boolean)")
            
          
  
            