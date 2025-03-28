import pyodbc



## uppgifter som krävs för att skapa kopplingen, vi lägger dem i variabler 
db_server = "DESKTOP-6FUEENN\SQLEXPRESS"
db_name = "Hälsovård"
db_driver = "ODBC Driver 17 for SQL Server"


## skapar kopplingen mellan databasen från SQL programmet och koden här
## trusted conenction=yes vilket betyder att vi behöver ingen inloggning utan den loggas in själv 
connection_string = f"""
DRIVER={db_driver};
SERVER={db_server};
DATABASE={db_name};
trusted_connection=yes;  
"""



#----------------------------------------------------------------------------
## Class med Databaslogiken 
class DB():

# Denna metoden skapar kopplinfen med databasen från SQL programmet och exekverar en querry när den anropas
# Den tar emot alla queries och SELECT kommer inte exekveras eftersom den bara visar data och gör ingen ändring på datan 
    def call_db(self, query, *args):
        data = None 
        conn = pyodbc.connect(connection_string)
        cur = conn.cursor()
        if "SELECT" in query:
            res = cur.execute(query, args)
            data = res.fetchall()
            cur.commit()
            cur.close()
        else:
            conn.execute(query, args)
        conn.commit()
        conn.close()
        return data

#----------------------------------------------------------------------------
# skapar kopplingen med databasen, läser och exekverar en sql typ av fil med queries som skapar tabeller, kollumner och kolumner med PIMARY KEYS
# Jag kommer använda mig av en databas jag skapade själv och den ligger i filen "tables.sql" 
    def init_db(self):
        conn = pyodbc.connect(connection_string)
        with open (
            "tables.sql", mode= "r", encoding="utf-8"
        ) as file:
            script = file.read()
            print(script)
            conn.execute(script)
            conn.commit()   
        conn.close()

#------------------------------------------------------------------------------
#fyller på tabeller med data som ligger i dokumentet "values.sql"
    def fill_db(self):
        conn = pyodbc.connect(connection_string)
        with open (
            "values.sql", mode= "r", encoding="utf-8"
        ) as file:
            script = file.read()
            print(script)
            conn.execute(script)
            conn.commit()   
        conn.close()

#---------------------------------------------------------------------------------------------------------------------------
# Eftersom den här tabellen går ej att skapa med andra tabeller från sql filen samtidigt eftersom den är many to many tabell
# därför kommer jag skapa den här och sätta FOREIGN KEYS på 2 av redan skapade tabeller 
    def fix_tables (self):
        tab5_query = """
        CREATE TABLE patient_treatment (
     	    id INT IDENTITY (1,1) PRIMARY KEY,
     	    pat_id INT REFERENCES patient(id),
    	    tre_id INT REFERENCES treatment(id));
        """
        fk_query2 ="""
        ALTER TABLE patient
        ADD FOREIGN KEY (dep_id) REFERENCES department (id)
        ;
        """
        fk_query3 = """
        ALTER TABLE department
        ADD FOREIGN KEY (hos_id) REFERENCES hospital (id)
        ;
        """
        conn = pyodbc.connect(connection_string)
        conn.execute(tab5_query)
        conn.execute(fk_query2)
        conn.execute(fk_query3)
        conn.commit()
        conn.close()

    
#----------------------------------------------------------------------------
## då kommer den här o köras bara om jag kör den här filen specifikt
## annars kommer den inte köras. Det är bra för att denna filen behöver köras bara en gång

if __name__ == "__main__":
    db_sql = DB()
    # db_sql.init_db()
    # db_sql.fix_tables()
    # db_sql.fill_db()

