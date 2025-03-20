gender = input("Enter biological gender (male/female): ")
hemoglobin_value = float(input("Enter your hemoglobin value: "))

#Normal hemoglobin level
if gender == "female":
    normal_range = (117, 155)
elif gender == "male":
    normal_range = (134, 167)
else:
    print("Invalid gender entered.")
    exit()


# Check if the hemoglobin is low, normal, or high
if hemoglobin_value < normal_range[0]:
    print("Your hemoglobin value is low.")
elif normal_range[0] <= hemoglobin_value <= normal_range[1]:
    print("Your hemoglobin value is normal.")
else:
    print("Your hemoglobin value is high.")
