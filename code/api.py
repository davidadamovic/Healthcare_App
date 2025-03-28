
from fastapi import FastAPI
from db import DB
from models import Hospital, Department, Patient, Treatment, Patient_treatment


## här skapas appen app
## skapa en app av en FastAPI konstruktör
app = FastAPI()
db = DB()


#_________________________________________________GET__________________________________________________________
# Get routes för varje tabell i databasen  
# 

@app.get("/patients") # routen 
def get_patients():
    query = """
    SELECT * FROM patient
    """
    data = db.call_db(query)    # queryn exekveras av metoden från DB klassen och resultatet lagras i "data"
    patients = []               # Tom lista som kommer användas för att lagra inhämtad data
    for element in data:        # for loop som unpackar inhämdad data som kommer som en Dickt 
        id, name, age, gender, dep_id = element  # unpackar dicten och får fram alla kolumner i tabellen "patient"
        # kolumnerna ska appendas till variabler fårn Klassen Patient som är en Base Model
        # Behöver inte lagras utanför metoden för att det är bara SELECT query 
        patients.append(Patient(id=id, name=name, age=age, gender=gender, dep_id=dep_id))
    print(data) # skriver ut Dicten 
    return patients # Färdig lista returneras



@app.get("/hospitals")
def get_hospital():
    query = """
    SELECT * FROM hospital
    """
    data = db.call_db(query)
    hospitals = []
    for element in data:
        id, hospital_name, city = element
        hospitals.append(Hospital(id=id, hospital_name=hospital_name, city=city))
    print(data)
    return hospitals



@app.get("/departments")
def get_department():
    query = """
    SELECT * FROM department
    """
    data = db.call_db(query)
    departments = []
    for element in data:
        id, department_name, phone_number, hos_id = element
        departments.append(Department(id=id, department_name=department_name, phone_number=phone_number, hos_id=hos_id))
    print(data)
    return departments



@app.get("/treatments")
def get_treatment():
    query = """
    SELECT * FROM treatment
    """
    data = db.call_db(query)
    treatments = []
    for element in data:
        id, length_of_treatment_days, medicine, cost = element
        treatments.append(Treatment(id=id, length_of_treatment_days=length_of_treatment_days, medicine=medicine, cost=cost))
    print(data)
    return treatments



@app.get("/patient_treatment")
def get_patient_treatment():
    query = """
    SELECT * FROM patient_treatment
    """
    data = db.call_db(query)
    pat_tre = []
    for element in data:
        id, pat_id, tre_id = element
        pat_tre.append(Patient_treatment(id=id, pat_id=pat_id, tre_id=tre_id))
    print(data)
    return pat_tre



# #___________________________________________________POST__________________________________________________________


@app.post("/add_patient")
def add_patient(patient: Patient): # Klass Patient som attribut för att komma åt klassens attribut
    query = """
    INSERT INTO patient (name, age, gender, dep_id)
    VALUES ( ?, ?, ?, ?)
    """
    # queryn exekveras med metodens attribut som inehåller klassens attributen
    db.call_db(query, patient.name, patient.age, patient.gender, patient.dep_id)
    print(patient) 
    return """
    Patient registerd"""



@app.post("/add_hospital")
def add_hospital(hospital: Hospital):
    query = """
    INSERT INTO hospital (hospital_name, city)
    VALUES ( ?, ?)
    """
    db.call_db(query, hospital.hospital_name, hospital.city)
    print(hospital)
    return """
    Hospital registerd"""



@app.post("/add_department")
def add_department(department: Department):
    query = """
    INSERT INTO department (department_name, phone_number, hos_id)
    VALUES ( ?, ?, ?)
    """
    db.call_db(query, department.department_name, department.phone_number, department.hos_id)
    print(department)
    print("""
    Treatment registerd""")


@app.post("/add_treatment")
def add_treatment(treatment: Treatment):
    query = """
    INSERT INTO treatment (length_of_treatment_days, medicine, cost)
    VALUES ( ?, ?, ?)
    """
    db.call_db(query, treatment.length_of_treatment_days, treatment.medicine, treatment.cost)
    print(treatment)
    return """
    Treatment registerd"""


# #________________________________________________DELETE__________________________________________________________


@app.delete("/delete_patient/{id}") # en rad i tabellen patient raderas enligt patientens id 
def delete_patient(id: int):        # id är därför en attribut i denna funktionen
    query = """
    DELETE FROM patient WHERE id = ?
    """
    # query exekveras tillsammans med id som kommer vara user input
    db.call_db(query, id)
    return """
    Patient Removed!"""



@app.delete("/delete_hospital/{id}")
def delete_hospital(id: int):
    query = """
    DELETE FROM hospital WHERE id = ?
    """
    db.call_db(query, id)
    return """
    Hospital Removed!"""


@app.delete("/delete_department/{id}")
def delete_department(id: int):
    query = """
    DELETE FROM department WHERE id = ?
    """
    db.call_db(query, id)
    return """
    Department Removed!"""



@app.delete("/delete_treatment/{id}")
def delete_treatment(id: int):
    query = """
    DELETE FROM treatment WHERE id = ?
    """
    db.call_db(query, id)
    return """
    Treatment Removed!"""



# #_______________________________________________PUT__________________________________________________________

@app.put("/update_patient/{id}")  # Vald rad i tabellen patient redigeras 
def update_patient(id: int, new_patient: Patient): 
    query = """
    UPDATE patient
    SET name =?, age =?, gender =?, dep_id = ? 
    WHERE id = ?
    """
    # query exekveras tillsammans med id som kommer vara user input
    db.call_db(query, new_patient.name, new_patient.age, new_patient.gender, new_patient.dep_id, id)
    return """
    Patient Updated!"""







#______________________________________________________________________________________________________________________________
# första försök att bygga appen 
#______________________________




# @app.get("/hospitals/{hospital_id}")

# def get_hospitals(hospital_id:int ):
#     data = db.get_any(
#         tabell= "hospitals",
#         column=("hospital_name" "," "city" "," "adress"),       # kan va en eller flera argument/kolumner
#         where=("hospital_id", str(hospital_id))                  # optional 
#          )
#     return data  

#  ","  - denna kommatecken är inget o skoja med 

#----------------------------
# @app.get("/patients/{id}")

# def get_patients(department_id:int ):
#     data = db.get_any(
#         tabell= "patient",
#         # column=("*"),
#         column=("name" "," "age" "," "gender"),       
#         where=("department_id", str(department_id))                  
#          )
#     return data  



#------------------------------------
# SELECT * FROM patients 
# JOIN patient_treatment 
# ON patients.patient_id = patient_treatment.patient_id
# WHERE patients.department_id = 6

# en Join av två tabeller patients och patient_treatment
# vi får fram all data från de två tabellerna om alla personer som satt
# på samma avdelning data om personer 


# @app.get("/join/patients/patient_treatment/{department_id}")

# def join(department_id:int):
#     data = db.join(
#         tabell1= "patients",
#         tabell2= "patient_treatment",
#         column="patient_id",
#         where= ("department_id", str(department_id))                   
#          )
#     return data  




#-------------------------behövs inte. har fixat en bätte app där uppe----------------------

#Get one specific thing by chosing table, column and value 

# @app.get("/hospital")
# def get_hospital():
#     data = db.get_one(
#         tabell="hospitals",
#         key = "city",
#         value= 'Stockholm'
#         )
#     print(data)
#     return data 



# @app.get("/department")
# def get_department():
#     data = db.get_one(
#         tabell="departments",
#         key = "urine_and_blood_test",
#         value= 'needed'
#         )
#     print(data)
#     return data 


#_____________________________POST______________________________________
# @app.post("/create_person")
# def create_person(person: Person):
    # create_person_query = """
    # INSERT INTO person ( 
    #     name, 
    #     title, 
    #     email, 
    #     phone 
    # ) VALUES (
    #     ?, ?, ?, ?
    # )
    # """
    # print(person)
    # db.call_db(
    #     create_person_query,
    #     person.name,
    #     person.title,
    #     person.email,
    #     person.phone_number,
    # )
    # return "Created person"

#....................................

# förstår inte vad ska jag göra i thunder client för att skapa kolumnen 
# Jag vet att man ska till PUT POST men vad skriver man som JSON content
 
# {
#     "patient_id": 
#     "name": 
#     "age": 
#     "gender": 
#     "date_of_attendence": 
#     "department_id":
#     "department_name": 
# }

# försökte med argumenten också men det blir svårt att ha Dikten där

# {   
#     "col_properties": "FOREIGN KEY REFERENCES",
#     "ref_tab": "departments",
#     "ref_col": "patients.department_name"
# }

# @app.post("/create_column")
# def new_column(patient: Patient, departments: Department):
#     data = db.create_column(
#         tabell="patients",
#         kolumn="department_name",
#         datatype="VARCHAR(50)",
#         fk= {"col_properties": "FOREIGN KEY REFERENCES",
#              "ref_tab": departments, 
#              "ref_col": patient.department_name}
#     )
#     return data 
#     pass




#_____________________________PUT________________________________________
## update person 
# @app.put("/update_person")
# def update_person(person: Person):
#     data = db.update(
#         table = "person", 
#         fields= {"name": person.name, "age":str(person.age) },
#         where= ("id", str(person.id)),
#         )
#     return data
#     pass


