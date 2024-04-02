def calculate_cgpa(grades):
    total_points = 0
    total_credit_units = 0
    
    for grade, credit_unit in grades:
        # Convert grade to points
        if grade == 'A':
            points = 5
        elif grade == 'B':
            points = 4
        elif grade == 'C':
            points = 3
        elif grade == 'D':
            points = 2
        elif grade == 'E':
            points = 1
        else:
            points = 0
        
        # Calculate total points and total credit units
        total_points += points * credit_unit
        total_credit_units += credit_unit
    
    # Calculate CGPA
    cgpa = total_points / total_credit_units
    return cgpa

# Example usage:
grades = [('A', 4), ('B', 3), ('C', 3)]  # Format: (Grade, Credit Units)
result = calculate_cgpa(grades)
print("CGPA:", result)
