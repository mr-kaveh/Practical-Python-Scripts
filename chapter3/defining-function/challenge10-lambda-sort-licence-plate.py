# List of license plates
license_plates = [
    "ABC 123",
    "XYZ 789",
    "DEF 456",
    "JKL 987",
    "MNO 654",
]

# Sort license plates by the numeric part (e.g., 123, 789) in ascending order using a lambda function
sorted_plates_by_numeric_part = sorted(license_plates, key=lambda plate: int(plate.split(' ')[1]))
print("License plates sorted by numeric part (ascending):")
for plate in sorted_plates_by_numeric_part:
    print(plate)

# Sort license plates by the alphabetic part (e.g., ABC, XYZ) in descending order using a lambda function
sorted_plates_by_alphabetic_part = sorted(license_plates, key=lambda plate: plate.split(' ')[0], reverse=True)
print("\nLicense plates sorted by alphabetic part (descending):")
for plate in sorted_plates_by_alphabetic_part:
    print(plate)
