def search(patients, dis):
    return [patient["Name"] for patient in patients if patient["Disease"].lower() == disease.lower()]

patients = [
    {"Name": "Alice", "Age": 30, "Disease": "Flu"},
    {"Name": "Bob", "Age": 45, "Disease": "Diabetes"},
    {"Name": "Charlie", "Age": 35, "Disease": "Flu"}
]

disease = "Flu"

result = search(patients, disease)

print(f"Patients with {disease}: {result}")
