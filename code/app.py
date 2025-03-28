import requests
from typing import  List
from models import Patient, Hospital, Department, Treatment, Patient_treatment
from menues import print_menues


# importerade menyer som ska skrivas ut i terminealen 
m = print_menues()


# url eller länken till appen 
# en funktion som tar routen som argument och appendar till urln  
def url(route: str):
    return f"http://127.0.0.1:8000{route}"




print("""
Hi! This is Healthcare database. Read carefully!""")


########################################## A D D ######################################################################################

# Lägger till en Hospital
# tar inputs från usern som sedan lagras i modellen 
# modellen med datan lagras i new_hospital 
# och skcias med urln och routen till appen som sedan exekverar en query med datan i sig 
# och lagrar datan i min databas
# res skrivs ut för att få fram Response så att man vet om man lyckats att posta
# får man 200 så har man lyckats att posta
def add_hospital(): 
    print("")
    print("Add a hospital: ")
    print("")
    name = input("Name of the hospital: ")
    city = input("City: ")
    new_hospital = Hospital(hospital_name=name, city=city) 
    res = requests.post(url("/add_hospital"), json=new_hospital.dict())
    print(res)  


# Lägger till en patient
# Patient tabellen här en FK dep_id  som är id till departments
# eftersom man inte vet vilken department handlar det om så ville jag hämta alla och skriva ut så att man vet i vilken department
# ska man placera en patient
# dep_info innehåller tabell department som dekoderas där nere 
# data blir till en Dict som ska unpackas och så ska den skriva ut id:n och namn från Department  
def add_patient():
    print(" ")
    print("Add a patient")
    print(" ")
    name = input("First name and Last name: ")
    age = input("Age: ")
    gender = input("Gender (male/female): ") 
    print("")
    dep_info = requests.get(url("/departments"))
    if not dep_info.status_code == 200:      
        return   
    data = dep_info.json()   
    for dep in data:  
        dep = Department(**dep)
        print(f"[id: {dep.id}]  {dep.department_name}")
    dep_id = input(""" 
   Enter a department by department's id: """)
    new_patient = Patient(name=name, age=age, gender=gender, dep_id=dep_id) 
    res = requests.post(url("/add_patient"), json=new_patient.dict())
    print(res)


## Lägger till en Department
def add_department():
    print(" ")
    print("Add a department: ")
    print(" ")
    name = input("Department's name: ")
    contact = input("Phone number: ")
    print("")
    dep_info = requests.get(url("/hospitals"))
    if not dep_info.status_code == 200:
        return 
    data = dep_info.json()
    for dep in data:  
        dep = Hospital(**dep)
        print(f"[id: {dep.id}]  {dep.hospital_name}")
    hos_id = input(""" 
    Enter a hospital by hospital's id: """)
    new_department = Department(department_name=name, phone_number=contact, hos_id=hos_id)  
    res = requests.post(url("/add_department"), json=new_department.dict())
    print(res)


# Lägger till en treatment
def add_treatment():
    print("")
    print("Add a treatment: ")
    print("")
    length = input("Length of the treatment in days: ")
    medicine = input("Prescribed medicine: ")
    cost = input("Price of the treatment in SEK: ")
    new_treatment = Treatment(length_of_treatment_days=length, medicine=medicine, cost=cost) 
    res = requests.post(url("/add_treatment"), json=new_treatment.dict())
    print(res)



########################################## G E T ######################################################################################



# Hämtar data från databasen med urln och routen
# Dekodar data 
# unpackar med for loopen 
# skriver ut datan 
# data appendas och sparas i en lista för att listan kommer med datan kommer jag behöva i main funktionen 
def get_patient():
    patients=[]
    print("") 
    print("See the patients")
    print("")
    res = requests.get(url("/patients"))
    if not res.status_code == 200:
        return 
    data = res.json()
    for pat in data:  
        pat = Patient(**pat) 
        print("_________")
        print(f"ID: {pat.id}")
        print(f"Name: {pat.name}")
        print(f"Age: {pat.age}")
        print(f"Gender: {pat.gender}")     
        print("")
        patients.append(pat)
    return patients



def get_hospital():
    print("")
    print("See Hospitals")
    print("")
    res = requests.get(url("/hospitals"))
    if not res.status_code == 200:
        return 
    data = res.json()
    for hos in data:  
        hos = Hospital(**hos) 
        print("_________")
        print(f"ID: {hos.id}")
        print(f"Hospital: {hos.hospital_name}")
        print(f"City: {hos.city}")
        print("")




def get_department():
    print("")
    print("See Departments")
    print("")
    res = requests.get(url("/departments"))
    if not res.status_code == 200:
        return 
    data = res.json()
    for dep in data:  
        dep = Department(**dep) 
        print("_________")
        print(f"ID: {dep.id}")
        print(f"Department: {dep.department_name}")
        print(f"Contact: {dep.phone_number}")
        print("")



def get_treatment():
    print("")
    print("See Treatments")
    print("")
    res = requests.get(url("/treatments"))
    if not res.status_code == 200:
        return 
    data = res.json()
    for tre in data:  
        tre = Treatment(**tre) 
        print("_________")
        print(f"Treatment ID: {tre.id}")
        print(f"Length: {tre.length_of_treatment_days}")
        print(f"Medicine: {tre.medicine}")
        print(f"Cost: {tre.cost}")     
        print("")



def get_patient_treatment():
    print("""
            Patients x treatment
(many to many table) not available for editing
    """)
    res = requests.get(url("/patient_treatment"))
    if not res.status_code == 200:
        return 
    data = res.json()
    for pat_tre in data:  
        pat_tre  = Patient_treatment(**pat_tre ) 
        print("_________")
        print(f"id: {pat_tre.id}")
        print(f"Patient's id: {pat_tre.pat_id}")
        print(f"Treatment's id: {pat_tre.tre_id}")
    print("")   






########################################## D E L E T E ######################################################################################

# Vi tar input från usern 
# kollar om det är en siffra
# resultatet skickas till delete routen i appen
def delete_patient():
    print("")
    print("Delete a patient")
    print("")
    delete_patient = input("Id of patient you want to remove: ")
    if not str.isdigit(delete_patient):
        print("Id is integer")
        return
    res = requests.delete(url(f"/delete_patient/{delete_patient}"))
    print(res.json())



def delete_hospital():
    print("")
    print("Remove a hospital from the List")
    print("")
    delete_hospital = input("Id of hospital you want to remove: ")
    if not str.isdigit(delete_hospital):
        print("Id is integer")
        return
    res = requests.delete(url(f"/delete_hospital/{delete_hospital}"))
    print(res.json())



def delete_department():
    print("")
    print("Remove a department from the List")
    print("")
    delete_department = input("Enter the id of department: ")
    if not str.isdigit(delete_department):
        print("Id is integer")
        return
    res = requests.delete(url(f"/delete_department/{delete_department}"))
    print(res.json())



def delete_treatment():
    print("")
    print("Remove a treatment from the List")
    print("")
    delete_treatment = input("Enter the treatment's id: ")
    if not str.isdigit(delete_treatment):
        print("Id is integer")
        return
    res = requests.delete(url(f"/delete_treatment/{delete_treatment}"))
    print(res.json())




# ######################################## U P D A T E ######################################################################################

# Modellen Patient görs till en lista där man loppar igenom och för att se om id:n som kom från user input matchar en id i modellen  
# matchen lagras i "index" och sedan till pat
# dep_id sparades ockås vilket kommer jag behöva sedan om jag ska ändra dep_id. Man vill veta vad man hade inann man byter ut den 

# Vi tar inputs och gör dem optional med if satser 
# imput datan skickas till data modellen Patient och som skcikas till appen 

def update_patient(patients: List[Patient]):
    print("")
    print("Update patient")
    print("")
    update_patient = input("Id of patient you want to update: ")
    print(" ")
    if not str.isdigit(update_patient):
        print("Entered value has to be a number")
        return
# om vi hittar rätt pat.id som matchar inputen så lagras siffran i "index"
    index = None
    for i, pat in enumerate(patients):       
        if pat.id == int(update_patient):
            index = i
            dep_id = pat.dep_id
            break

    if index == None:
        print("There is no patient with this ID")
        return
    
    pat = patients[index]
    name = input("Patient's name (leave empty if same): ")
    age = input("Patient's age (leave empty if same): ")
    gender = input("Patient's gender (leave empty if same): ")
    print(f"Current department: [id:{pat.dep_id}]")
    dep_id = input("Enter a department by department's id (leave empty if same): ")

    if not name:
        name = pat.name
    if not age:
        age = pat.age
    if not gender:
        gender = pat.gender
    if not dep_id:
        dep_id = pat.dep_id

    new_patient = Patient(name=name, age=age, gender=gender, dep_id=dep_id)
    res = requests.put(url(f"/update_patient/{update_patient}"), json=new_patient.dict())
    print(res.json())



############################################ M E N U ##############################################################################################################
    
# vi skriver ut menu som importerades från menues as m 
# vi tar tar imputen som kan ha space och små bokstav

# "A" skriver ut en annan meny och öppnar en rad av id satser som tar siffror som inputs för att det gick inte att
# siffror eller bokstäver på båda 
# För varje val utförs det en 

def main():
    m.print_menu()
    letter = input("Please choose a table: ")
    letter = letter.strip().upper()

    if letter == "A": 
        m.print_patient_menu()
        num = input("Please choose your action: ")
        if not str.isdigit(num):
            print("Please enter a valid option") 
            return          
        num=int(num)
        if num == 1:
             get_patient()  
        elif num == 2:
            add_patient()               
        elif num == 3:
            delete_patient()
        elif num == 4:
            pats = get_patient() # vi hämtar datan först och sparar i pats
            update_patient() # pats blir en lista som används som attribut
        elif num == 5:
            return
        elif num == 6:
            print("Enter a valid choice")


    elif letter == "B":  
        m.print_hospital_menu()
        num = input("Please choose your action: ")
        if not str.isdigit(num):
            print("Please enter a valid option") 
            return 
        num=int(num)              
        if num == 1:
             get_hospital()
        elif num == 2:
            add_hospital()       
        elif num == 3:
            delete_hospital()
        elif num == 4:
            return
        elif num == 5 or 6 or 7:
            print("Enter a valid choice")


    elif letter == "C":
        m.print_department_menu()
        num = input("Please choose your action: ")
        if not str.isdigit(num):
            print("Please enter a valid option") 
            return 
        num=int(num)              
        if num == 1:
             get_department()
        elif num == 2:
            add_department()       
        elif num == 3:
            delete_department()
        elif num == 4:
            return
        elif num == 5 or 6 or 7:
            print("Enter a valid choice")


    elif letter == "D":
        m.print_treatment_menu()
        num = input("Please choose your action: ")
        if not str.isdigit(num):
            print("Please enter a valid option") 
            return 
        num=int(num)              
        if num == 1:
             get_treatment()
        elif num == 2:
            add_treatment()       
        elif num == 3:
            delete_treatment()
        elif num == 4:
            return
        elif num ==5 or 6 or 7:
            print("Enter a valid choice")
  
    elif letter == "E":
        get_patient_treatment()

    elif letter == "F":
        exit()

                
#______________________________________________________________

while __name__ == "__main__":
        main()