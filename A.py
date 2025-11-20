def detect_number_type(user_input):
    """
    Detects whether the input is decimal or hexadecimal.
    Returns the integer value and the detected type as a string.
    """
    # Check for hex (with or without 0x prefix)
    try:
        if user_input.lower().startswith("0x"):
            value = int(user_input, 16)
            return value, "hexadecimal"
        else:
            # Try hex without prefix
            value = int(user_input, 16)
            # If it converts, assume hex only if letters A-F are present
            if any(c in "abcdefABCDEF" for c in user_input):
                return value, "hexadecimal"
    except ValueError:
        pass

    # Otherwise treat as decimal
    try:
        value = int(user_input)
        return value, "decimal"
    except ValueError:
        return None, "invalid"