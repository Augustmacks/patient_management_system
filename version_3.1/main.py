from patient_management import PatientManagementSystem

if __name__ == "__main__":
    storage_type = input("Select Storage Type (CSV/JSON): ").strip().upper()
    while storage_type not in ["CSV", "JSON"]:
        storage_type = input("Invalid! Select Storage Type (CSV/JSON): ").strip().upper()

    while True:
        print("\n1. Add New Patient\n2. Get All Patients\n3. Search Patient by ID\n4. Delete Patient by ID\n5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            PatientManagementSystem.add_patient(storage_type)
        elif choice == "2":
            PatientManagementSystem.get_all_patients(storage_type)
        elif choice == "3":
            patient_id = int(input("Enter Patient ID: "))
            PatientManagementSystem.search_patient_by_id(patient_id, storage_type)
        elif choice == "4":
            patient_id = int(input("Enter Patient ID: "))
            PatientManagementSystem.delete_patient_by_id(patient_id, storage_type)
        elif choice == "5":
            print("Exiting system...")
            break
        else:
            print("Invalid choice, please try again.")
