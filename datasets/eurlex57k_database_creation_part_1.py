#!pip install mysql-connector-python 

import mysql.connector

steps=[2] #1: create the database, 2: create the tables 

for step in steps:
    
    if step==1:
        mydb = mysql.connector.connect(
            host="localhost",    
            user="root",        
            password="admin"
            )
        mycursor = mydb.cursor()

        mycursor.execute("CREATE DATABASE eurlex57K_dev CHARACTER SET utf8 COLLATE utf8_general_ci")
        
    elif step==2:
        mydb = mysql.connector.connect(
            host="localhost",    
            user="root",        
            password="admin",
            database="eurlex57K_test",
            )
            
        mycursor = mydb.cursor()
        
        mycursor.execute("CREATE TABLE documents (celex_id VARCHAR(50), uri TEXT, type_1 VARCHAR(50),\
                        title_text TEXT, header_text TEXT, recitals_text TEXT, main_body_text TEXT,\
                        attachments_text TEXT, PRIMARY KEY (celex_id))")

        mycursor.execute("CREATE TABLE document_concepts (celex_id VARCHAR(50), FOREIGN KEY (celex_id) REFERENCES documents(celex_id), \
                         concept VARCHAR(20))")      