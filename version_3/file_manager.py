import json
import csv

class FileManager:
    @staticmethod
    def read_file(storage_type):
        if storage_type == "CSV":
            try:
                with open("patients.csv", mode="r") as file:
                    return list(csv.DictReader(file))
            except FileNotFoundError:
                return []
        elif storage_type == "JSON":
            try:
                with open("patients.json", "r") as file:
                    return json.load(file)
            except (FileNotFoundError, json.JSONDecodeError):
                return []

    @staticmethod
    def write_file(storage_type, data):
        if storage_type == "CSV":
            with open("patients.csv", mode="w", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=data[0].keys())
                writer.writeheader()
                writer.writerows(data)
        elif storage_type == "JSON":
            with open("patients.json", "w") as file:
                json.dump(data, file, indent=4)