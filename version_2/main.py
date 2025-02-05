import re
import datetime
import csv
import json

# List to store patient data in memory
patients = []

# Load data from file

def load_data(storage_type):
    global patients
    try:
        if storage_type == "CSV":
            with open("patients.csv", mode="r") as file:
                reader = csv.DictReader(file)
                patients = [row for row in reader]
        elif storage_type == "JSON":
            with open("patients.json", mode="r") as file:
                patients = json.load(file)
    except FileNotFoundError:
        patients = []

# Save data to file
def save_data(storage_type):
    if storage_type == "CSV":
        with open("patients.csv", mode="w", newline="") as file:
            fieldnames = ["id", "first_name", "last_name", "date_of_birth", "age", "hometown", "house_number", "phone_number"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(patients)
    elif storage_type == "JSON":
        with open("patients.json", mode="w") as file:
            json.dump(patients, file)

# Validate date of birth
def validate_date_of_birth(dob):
    date_pattern = r"^\d{2}-\d{2}-\d{4}$"  # dd-mm-yyyy format
    if not re.match(date_pattern, dob):
        return None

    try:
        dob_as_date = datetime.datetime.strptime(dob, "%d-%m-%Y").date()
        return dob_as_date
    except ValueError:
        return None

# Validate phone number
def validate_phone_number(phone):
    phone_pattern = r"^\d{3}-\d{3}-\d{4}$"
    return re.match(phone_pattern, phone) is not None

# Calculate age
def calculate_age(dob):
    today = datetime.date.today()
    return today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

# Add new patient
def add_patient(storage_type):
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")

    dob = None
    while not dob:
        dob_input = input("Enter date of birth (dd-mm-yyyy): ")
        dob = validate_date_of_birth(dob_input)
        if not dob:
            print("Invalid date of birth. Try again.")

    age = calculate_age(dob)
    hometown = input("Enter hometown: ")
    house_number = input("Enter house number: ")

    phone_number = None
    while not phone_number:
        phone_input = input("Enter phone number (000-000-0000): ")
        if validate_phone_number(phone_input):
            phone_number = phone_input
        else:
            print("Invalid phone number format. Try again.")

    patient_id = len(patients) + 1
    new_patient = {
        "id": str(patient_id),
        "first_name": first_name,
        "last_name": last_name,
        "date_of_birth": dob.strftime("%d-%m-%Y"),
        "age": str(age),
        "hometown": hometown,
        "house_number": house_number,
        "phone_number": phone_number,
    }

    patients.append(new_patient)
    save_data(storage_type)
    print("Patient added successfully!")

# Get all patients
def get_all_patients(storage_type):
    if not patients:
        print("No patients found.")
        return

    for patient in patients:
        print(patient)

# Search patient by ID
def search_patient_by_id(patient_id, storage_type):
    for patient in patients:
        if patient["id"] == str(patient_id):
            print(patient)
            return
    print("Patient not found.")

# Update patient by ID
def update_patient_by_id(patient_id, storage_type):
    for patient in patients:
        if patient["id"] == str(patient_id):
            print("Current details:", patient)

            for key in ["first_name", "last_name", "date_of_birth", "hometown", "house_number", "phone_number"]:
                new_value = input(f"Enter new value for {key} (leave blank to keep current): ")
                if new_value:
                    if key == "date_of_birth":
                        dob = validate_date_of_birth(new_value)
                        if dob:
                            patient[key] = dob.strftime("%d-%m-%Y")
                            patient["age"] = str(calculate_age(dob))
                        else:
                            print("Invalid date format. Skipping.")
                    elif key == "phone_number":
                        if validate_phone_number(new_value):
                            patient[key] = new_value
                        else:
                            print("Invalid phone format. Skipping.")
                    else:
                        patient[key] = new_value

            save_data(storage_type)
            print("Patient updated successfully!")
            return

    print("Patient not found.")

# Delete patient by ID
def delete_patient_by_id(patient_id, storage_type):
    global patients
    for i, patient in enumerate(patients):
        if patient["id"] == str(patient_id):
            patients.pop(i)
            save_data(storage_type)
            print("Patient deleted successfully!")
            return

    print("Patient not found.")

# Main function
def main():
    print("Choose storage type: 1. CSV  2. JSON")
    choice = input("Enter your choice: ")
    storage_type = "CSV" if choice == "1" else "JSON"

    load_data(storage_type)

    while True:
        print("\nMenu:")
        print("1. Add Patient")
        print("2. Get All Patients")
        print("3. Search Patient by ID")
        print("4. Update Patient by ID")
        print("5. Delete Patient by ID")
        print("6. Exit")

        option = input("Enter your choice: ")

        if option == "1":
            add_patient(storage_type)
        elif option == "2":
            get_all_patients(storage_type)
        elif option == "3":
            patient_id = input("Enter patient ID: ")
            search_patient_by_id(patient_id, storage_type)
        elif option == "4":
            patient_id = input("Enter patient ID: ")
            update_patient_by_id(patient_id, storage_type)
        elif option == "5":
            patient_id = input("Enter patient ID: ")
            delete_patient_by_id(patient_id, storage_type)
        elif option == "6":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
