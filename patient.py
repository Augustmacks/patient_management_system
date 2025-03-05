import re
from datetime import datetime

class Patient:
    patient_counter = 1  # Auto-incrementing ID

    def __init__(self, first_name, last_name, date_of_birth, hometown, house_number, phone_number):
        self.id = Patient.patient_counter
        Patient.patient_counter += 1
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.age = self.calculate_age()
        self.hometown = hometown
        self.house_number = house_number
        self.phone_number = phone_number

    def calculate_age(self):
        birth_date = datetime.strptime(self.date_of_birth, "%d-%m-%Y")
        today = datetime.today()
        return today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

    def to_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "date_of_birth": self.date_of_birth,
            "age": self.age,
            "hometown": self.hometown,
            "house_number": self.house_number,
            "phone_number": self.phone_number
        }

    @staticmethod
    def validate_date_of_birth(date_str):
        pattern = r"\d{2}-\d{2}-\d{4}"
        return bool(re.match(pattern, date_str))

    @staticmethod
    def validate_phone_number(phone_str):
        pattern = r"\d{3}-\d{3}-\d{4}"
        return bool(re.match(pattern, phone_str))
