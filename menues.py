
## Här är en klass som inehåller alla menyer som kommer skrivas ut i terminalen 
## Jag kännde att det var lätare att ha i en annan fil 

class print_menues:
    


    def print_menu(arg):
        print(
            """       
Choose a table you want to work with

        A: Patient
        B: Hospital
        C: Department
        D: Treatment
        E: Patient x Treatment
        F: EXIT
        """
        )

    def print_patient_menu(arg):
        print(
            """ 
Table: Patient

        1: See the list of patients
        2: Add a patient
        3: Remove a patient
        4: Edit a patients journal
        5: Change table
        6: Exit
        """
        )

    def print_hospital_menu(arg):
        print(
            """
Table: Hospital

        1: See all hospitals
        2: Add a hospital
        3: Remove a hospital from the list
        4: Change table
        5: Exit
        """
        )

    def print_department_menu(arg):
        print(
            """ 
Table: Department
                
        1: See all departments
        2: Add a department
        3: Remove a department
        4: Change table
        5: Exit
        """
        )


    def print_treatment_menu(arg):
        print(
            """
Table: Treatment

        1: See all treatments
        2: Add a treatment
        3: Remove a treatment
        4: Change table
        5: Exit
        """
        )


    
