import re
import datetime

# List to store all patients
patients = []

# Function to validate the date of birth
def validate_date_of_birth(dob):
    date_pattern = r"^\d{2}-\d{2}-\d{4}$"  # dd-mm-yyyy format
    if not re.match(date_pattern, dob):
        print("Invalid date format. Please use dd-mm-yyyy.")
        return None

    try:
        dob_as_date = datetime.datetime.strptime(dob, "%d-%m-%Y").date()
        return dob_as_date
    except ValueError:
        print("Invalid date. Please enter a valid date (e.g., 29-02-2000 for leap years).")
        return None

# Function to calculate age
def calculate_age(dob):
    today = datetime.date.today()
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    return age

# Function to add a new patient
def add_patient():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    
    while True:
        dob_input = input("Enter date of birth (dd-mm-yyyy): ")
        dob = validate_date_of_birth(dob_input)
        if dob:
            break

    hometown = input("Enter hometown: ")
    house_number = input("Enter house number: ")

    age = calculate_age(dob)
    patient_id = len(patients) + 1  # Auto-incremented ID

    patient = {
        "id": patient_id,
        "first_name": first_name,
        "last_name": last_name,
        "dob": dob.strftime("%d-%m-%Y"),
        "age": age,
        "hometown": hometown,
        "house_number": house_number
    }

    patients.append(patient)
    print(f"Patient {first_name} {last_name} added successfully with ID {patient_id}.")

# Function to get all patients
def get_all_patients():
    if not patients:
        print("No patients in the system.")
        return

    print("\nAll Patients:")
    for patient in patients:
        print(f"ID: {patient['id']}, Name: {patient['first_name']} {patient['last_name']}, "
              f"DOB: {patient['dob']}, Age: {patient['age']}, "
              f"Hometown: {patient['hometown']}, House Number: {patient['house_number']}")

# Function to search for a patient by ID
def search_patient_by_id():
    try:
        patient_id = int(input("Enter the patient ID: "))
    except ValueError:
        print("Invalid ID. Please enter a number.")
        return

    for patient in patients:
        if patient["id"] == patient_id:
            print("\nPatient Found:")
            print(f"ID: {patient['id']}, Name: {patient['first_name']} {patient['last_name']}, "
                  f"DOB: {patient['dob']}, Age: {patient['age']}, "
                  f"Hometown: {patient['hometown']}, House Number: {patient['house_number']}")
            return

    print("No patient found with that ID.")

# Function to update a patient by ID
def update_patient_by_id():
    try:
        patient_id = int(input("Enter the patient ID to update: "))
    except ValueError:
        print("Invalid ID. Please enter a number.")
        return

    for patient in patients:
        if patient["id"] == patient_id:
            print("\nEnter new details (leave blank to keep existing values):")
            patient["first_name"] = input(f"First Name [{patient['first_name']}]: ") or patient["first_name"]
            patient["last_name"] = input(f"Last Name [{patient['last_name']}]: ") or patient["last_name"]
            patient["hometown"] = input(f"Hometown [{patient['hometown']}]: ") or patient["hometown"]
            patient["house_number"] = input(f"House Number [{patient['house_number']}]: ") or patient["house_number"]

            while True:
                dob_input = input(f"Date of Birth [{patient['dob']}] (dd-mm-yyyy): ")
                if not dob_input:
                    break
                dob = validate_date_of_birth(dob_input)
                if dob:
                    patient["dob"] = dob.strftime("%d-%m-%Y")
                    patient["age"] = calculate_age(dob)
                    break

            print("Patient details updated successfully.")
            return

    print("No patient found with that ID.")

# Function to delete a patient by ID
def delete_patient_by_id():
    try:
        patient_id = int(input("Enter the patient ID to delete: "))
    except ValueError:
        print("Invalid ID. Please enter a number.")
        return

    for patient in patients:
        if patient["id"] == patient_id:
            patients.remove(patient)
            print(f"Patient with ID {patient_id} deleted successfully.")
            return

    print("No patient found with that ID.")

# Main function to display the menu and process user input
def main():
    while True:
        print("\nPatient Management System")
        print("1. Add New Patient")
        print("2. Get All Patients")
        print("3. Search Patient by ID")
        print("4. Update Patient by ID")
        print("5. Delete Patient by ID")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()
        if choice == "1":
            add_patient()
        elif choice == "2":
            get_all_patients()
        elif choice == "3":
            search_patient_by_id()
        elif choice == "4":
            update_patient_by_id()
        elif choice == "5":
            delete_patient_by_id()
        elif choice == "6":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
