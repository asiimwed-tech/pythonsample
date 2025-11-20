from A import detect_number_type
from B import convert_to_binary


# ---- Main Program ----
user_input = input("Enter an integer or hex value (e.g., 42 or 0x2A): ")

value, number_type = detect_number_type(user_input)

if number_type == "invalid":
    print("Invalid input! Please enter a valid integer or hexadecimal number.")
else:
    print(f"Detected as: {number_type}")
    print(f"Integer value: {value}")

    binary_value = convert_to_binary(value)
    print(f"Binary representation: {binary_value}")
