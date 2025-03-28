
### Den här filen är en test fil där jag experimenterade innan jag började skapa databaslogik
### Sedan läste jag att det var inte bra att blanda 

# import sqlite3
# import os 
# from typing import Dict, Tuple, List

# #________________________________________________________________
# # Här ska jag skapa databasen 
# ## dvs en Klass med med metoder som först 
# #### skapar en database
# #### kör query från healthcare.sql filen 
# #### och inehåller olika metoder för att hantera data i databasen.
# #________________________________________________________________


# # __init metoden med hjälp av os.path kollar igenom systemet om en fin finns
# # if not då skapar den en databas med funktionen set_up_db
# class DBT():
#     db_con: str

#     def __init__(self, db_con:str ):
#         self.db_con = db_con
#         if not os.path.exists(self.db_con):
#             self.set_up_db()
#             # self.insert_values()
        


# # skapar kopplingen med databasen och namnet kommer anges som argument 
# # Jag kommer använda mig av en databas jag skapade själv 
#     def set_up_db(self):
#         conn = sqlite3.connect(self.db_con)
#         with open (
#             "tables.sql", mode= "r", encoding="utf-8"
#         ) as file:
#             script = file.read()
#             print(script)
#             conn.executescript(script)
#             conn.commit()   
#         conn.close()

# #__________________________________________
# ## återanvänt metod 
# ## en metod kallar databasen, skapar kopplingen med databasen, utför en querry och stänger ner kopplingen  
#     def call_db(self, query):
#         conn = sqlite3.connect(self.db_con)
#         cur = conn.cursor()
#         res = cur.execute(query)
#         data = res.fetchall()
#         cur.close()
#         conn.commit()
#         conn.close()
#         return data
    


# # en metod som visar alla värden från önskad tabell
#     def get_all(self, tabell:str):
#         query = f"""
#         SELECT * FROM {tabell}
#         """
#         data = self.call_db(query)
#         return data
#         pass

# ###################################### FUNKAR ################################################
# # en metod som visar värdet från önskad tabell och önskade kolumner
# ## visar all data från valda tabellen och kollumnen/er

#     def get_any(self, tabell:str, column:Tuple[str, str] | str, where:Tuple[str, str] | None=None ):     
#             query = f"""
#             SELECT {column} FROM {tabell} 
#             """
#             if where:
#                 key, value = where
#                 query2 = f""" 
#                 WHERE {key} = '{value}'
#                 """
#                 query = query + query2
#                 print(query)
#             data = self.call_db(query)
#             return data
#             pass

# # ______________________________________________________________________
# ## Join av valda tabeller och kolummner

#     def join(self, tabell1:str, tabell2:str, column:int ,where:Tuple[str, int]|None=None):     
#         query = f"""
#         SELECT * FROM {tabell1}
#         JOIN {tabell2}
#         ON {tabell1}.{column} = {tabell2}.{column}
#         """.format(tabell1, tabell2, tabell1, column, tabell2, column)
# # vet inte exakt vad format gör
#         if where:
#             col3, val3= where
#             query3 = f"""
#             WHERE {tabell1}.{col3} = '{val3}'
#             """.format(tabell1, col3, val3)
#             query = query + query3      

#         data = self.call_db(query)
#         print(query)
#         return data
#         pass
# #____________________________________________
# # ____________________________________________________
# # ska kolla om jag kan skapa en metod som skapar en kolumn i patients och sätter den som FK 
# # columnen ska heta department_name 

# # ALTER TABLE Customers
# # ADD degree VARCHAR(50);
# #-----option
# # PersonID int FOREIGN KEY REFERENCES Persons(PersonID)


#     def create_column(self, tabell:str, kolumn:str, datatype:str, fk:Dict[str,str] | None=None ):
#         query= f"""
#         ALTER TABLE {tabell} 
#         ADD COLUMN {kolumn} {datatype}
#         """
#         if fk: 
#             ref_tab = fk["ref_tab"]
#             ref_col = fk["ref_col"]
#             col_properties= fk.get("properties", " ") 
#             {col_properties}
#             fk_querry= f""" 
#             REFERENCES {col_properties}{ref_tab}({ref_col})
#             """
#             query = query + fk_querry
#         print(query)
#         data = self.call_db(query)
#         return data
#         pass




# #___________________________________________________________________________________________
# # UPDATE patients SET department_id = 6
# # WHERE patient_id = 1 ;

#     def update (self, *, table:str, where:Tuple[str, str], fields: Dict[str,str]):
#         where_key, where_val = where    ## unpacka dicts
#         field_query = ""

#         for key, val in fields.items():
#             field_query += f"{key} = '{val}',"
#         field_query = field_query[:-1]
#         update_query =f"""
#         UPDATE {table} SET {field_query} WHERE {where_key} = '{where_val}'
#         """

#         print(update_query)
#         self.__call_db(update_query)
#         pass
# # ______________________________________________________________________________________________



#     def insert(self, table:str, fields:Dict[str, str] ):
        
#         keys = ",".join(fields.keys())
#         values = "','".join(fields.values())

#         query = f"""
#         INSERT INTO {table} (
#             {keys}
#         )VALUES (
#             {values}
#         )
#         """
#         return self.__call_db(query)
