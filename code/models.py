from pydantic import BaseModel

## Base model klasser som definerar data modeller och underlättar datalogiken  

class Hospital (BaseModel):
	id: int | None   ## int eller None för att göra id optional eftersom id:n ska autoincrementas i databasen som jag skapade
	hospital_name: str 
	city: str


class Patient (BaseModel):
    id: int | None
    name: str
    age: int
    gender: str
    dep_id: int 


class Department (BaseModel):
	id: int | None
	department_name: str
	phone_number: int
	hos_id:int 


class Treatment (BaseModel):
	id: int | None
	length_of_treatment_days: int
	medicine: str
	cost:int 


class Patient_treatment (BaseModel):
	id: int | None
	pat_id: int 
	tre_id: int 