# Define a class called 'Patients' with attributes:
#    patient_name
#    age
#    date_of_latest_admission
#    medical_history
# Define a method called print_patient_details()
#    Print all details on a single line
# Demonstrate usage:
#    Create an instance of the class
#    Call the method to print patient info

class Patients:
    def __init__(self, name, age, admission_date, medical_history):
        self.patient_name = name
        self.age = age
        self.date_of_latest_admission = admission_date
        self.medical_history = medical_history

    def print_patient_details(self):
        print(f"Patient Name: {self.patient_name}, "
              f"Age: {self.age}, "
              f"Date of Latest Admission: {self.date_of_latest_admission}, "
              f"Medical History: {self.medical_history}")


# Example usage
p1 = Patients("Alex Johnson", 18, "2024-05-25", "Allergic to aspirin")
p1.print_patient_details()
