from patient import Patient
from file_manager import FileManager

class PatientManagementSystem:
    @staticmethod
    def add_patient(storage_type):
        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        date_of_birth = input("Enter Date of Birth (dd-mm-yyyy): ")
        while not Patient.validate_date_of_birth(date_of_birth):
            date_of_birth = input("Invalid format! Enter Date of Birth (dd-mm-yyyy): ")
        hometown = input("Enter Hometown: ")
        house_number = input("Enter House Number: ")
        phone_number = input("Enter Phone Number (123-456-7890): ")
        while not Patient.validate_phone_number(phone_number):
            phone_number = input("Invalid format! Enter Phone Number (123-456-7890): ")
        
        new_patient = Patient(first_name, last_name, date_of_birth, hometown, house_number, phone_number)
        patients = FileManager.read_file(storage_type)
        patients.append(new_patient.to_dict())
        FileManager.write_file(storage_type, patients)
        print("Patient added successfully!")

    @staticmethod
    def get_all_patients(storage_type):
        patients = FileManager.read_file(storage_type)
        for patient in patients:
            print(patient)

    @staticmethod
    def search_patient_by_id(patient_id, storage_type):
        patients = FileManager.read_file(storage_type)
        for patient in patients:
            if int(patient['id']) == patient_id:
                print(patient)
                return
        print("Patient not found!")

    @staticmethod
    def delete_patient_by_id(patient_id, storage_type):
        patients = FileManager.read_file(storage_type)
        updated_patients = [p for p in patients if int(p['id']) != patient_id]
        FileManager.write_file(storage_type, updated_patients)
        print("Patient deleted successfully!")