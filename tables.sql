


CREATE TABLE hospital (
	id INT IDENTITY (1,1) PRIMARY KEY,
	hospital_name VARCHAR(50) NOT NULL, 
	city CHAR (50) NOT NULL,  

);

CREATE TABLE patient (
	id INT IDENTITY (1,1) PRIMARY KEY ,
	name VARCHAR(30) NOT NULL,
	age INT NOT NULL,
	gender CHAR (10),
	dep_id INT    
);	

CREATE TABLE department (
	id INT IDENTITY (1,1) PRIMARY KEY,
	department_name VARCHAR(30),
	phone_number INT,
	hos_id INT 
	
);

CREATE TABLE treatment (
	id INT IDENTITY (1,1)  PRIMARY KEY,
	length_of_treatment_days INT,
	medicine VARCHAR(20), 
	cost INT

);





------------------------------------------------ Försök-------------------------------------

-- CREATE TABLE patient_treatment (
-- 	id INT IDENTITY (1,1) PRIMARY KEY,
-- 	pat_id INT REFERENCES patient(id),
-- 	tre_id INT REFERENCES treatment(id)

-- );


--- CREATE TABLE department (
-- 	id INT IDENTITY (1,1) PRIMARY KEY,
-- 	department_name VARCHAR(30),
-- 	phone_number INT,
-- 	hos_id INT REFERENCES hospital(id)

-- );

-- CREATE TABLE patient (
-- 	id INT IDENTITY (1,1) PRIMARY KEY,
-- 	name VARCHAR(30) NOT NULL,
-- 	age INT NOT NULL,
-- 	gender CHAR (10)
-- );


-- CREATE TABLE hospital (
-- 	id INT IDENTITY (1,1) PRIMARY KEY,
-- 	hospital_name VARCHAR(50), 
-- 	city CHAR (50), 
-- 	pat_id INT REFERENCES patient(id)
-- );


-- CREATE TABLE treatment (
-- 	id INT IDENTITY (1,1) PRIMARY KEY, 
-- 	length_of_treatment_days INT, 
-- 	medicine VARCHAR(20),
-- 	dep_id INT REFERENCES department(id)
-- );




