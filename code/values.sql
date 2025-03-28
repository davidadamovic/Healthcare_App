

INSERT INTO hospital (hospital_name, city)
	VALUES ('Sankt Görans sjukhus', 'Stockholm'),
		   ('Sollentuna sjukhus', 'Stockholm'),
		   ('Södersjukhuset', 'Stockholm'),
		   ('Södertälje sjukhus', 'Södertälje'),
		   ('Högsbo sjukhus', 'Göteborg'),
		   ('Sörgårdskliniken', 'Mölndal');



INSERT INTO patient (name, age, gender)
	VALUES('David Adamovic', '22', 'male'),
	      ('Alma Berggren Herceglija','21', 'female'),
		  ('Danja Tucakovic', '22', 'female'),
		  ('Nikbakhtan Hamidreza Esfahani', '23', 'male'),
		  ('Aid Mandzukic', '21', 'male'),
		  ('Alex Eusebiu Butilca', '23', 'male'),
		  ('Teodora Nikolic Djordjevic', '21', 'female');



INSERT INTO department (department_name, phone_number)
	VALUES ('Akutmottagning', '078930093'),
	       ('Arbetsterapi', '023212312'),
		   ('Psykiatri', '023212312'),
		   ('Fysioterapi', '023212312'),
		   ('Hjärnskador', '023212312'),
		   ('Hjärtdagvård', '023212312'),
		   ('Spåkförskola', '023212312'),
		   ('Tobaksenheten', '023212312');



INSERT INTO treatment (length_of_treatment_days, medicine, cost)
	VALUES ('12', 'tramadol','123'),
	       ('13', 'nikardipin','455'),
		   ('2323', 'lidokain','565'),
		   ('532', 'flukloxacillin','125'),
		   ('343', 'oxazepam','55'),
		   ('231', 'atenolol','335'),
		   ('123', 'lisinopril','280');
		



--PATIENTS
UPDATE patient SET dep_id = 6
WHERE id = 1 ;
UPDATE patient SET dep_id = 6
WHERE id = 2 ;
UPDATE patient SET dep_id = 2
WHERE id = 3 ;
UPDATE patient SET dep_id = 3
WHERE id = 4 ;
UPDATE patient SET dep_id = 8
WHERE id = 5;
UPDATE patient SET dep_id = 4
WHERE id = 6;
UPDATE patient SET dep_id = 3
WHERE id = 7;

--DEPARTMENTS 
UPDATE department SET hos_id = 1
WHERE id = 1 ;
UPDATE department SET hos_id = 2
WHERE id = 2 ;
UPDATE department SET hos_id = 3
WHERE id = 3 ;
UPDATE department SET hos_id = 4
WHERE id = 4 ;
UPDATE department SET hos_id = 5
WHERE id = 5;
UPDATE department SET hos_id = 6
WHERE id = 6;
UPDATE department SET hos_id = 1 
WHERE id = 7;
UPDATE department SET hos_id = 5 
WHERE id = 8;




INSERT INTO patient_treatment (pat_id, tre_id)
	VALUES (1, 1),
		   (1, 3),
		   (1, 5),
		   (2, 1),
		   (2, 3),
		   (2, 5),
		   (3, 4),
		   (4, 6),
		   (5, 3),
		   (6, 7),
		   (7, 4),
		   (4, 1);






