class Patients:
    def __init__(self, patient, age, date, medical):     
        self.patient_name = patient
        self.age = age
        self.date_of_latest_admission = date
        self.medical_history = medical

# print the outcome
    def print_patient_details(self):
        print(f"Patient Name: {self.patient_name}, Age: {self.age}, Date of Latest Admission: {self.date_of_latest_admission}, Medical History: {self.medical_history}")

# example of using the class
p = Patients("Alex", 18, 4.9, "Aspirin")        
p.print_patient_details()