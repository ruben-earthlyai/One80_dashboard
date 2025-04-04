def format_data(data):
    # Function to format data for display
    return str(data).strip()

def validate_input(input_data):
    # Function to validate user input
    if not input_data:
        raise ValueError("Input cannot be empty")
    return True

def log_error(error_message):
    # Function to log errors
    with open("error_log.txt", "a") as log_file:
        log_file.write(f"{error_message}\n")