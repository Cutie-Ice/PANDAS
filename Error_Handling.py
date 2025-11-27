"""
Python Error Handling Assignment - Complete Solution
Student Grade Processing System

This program demonstrates proper exception handling in Python
including try-except-finally, error recovery, and validation.
"""

# ============================================================================
# PART 1: Student Record Processor
# ============================================================================

def process_student_record(student):
    """
    Process a single student record with comprehensive error handling.
    
    Args:
        student (dict): Dictionary with 'name', 'score', and 'attendance'
    
    Returns:
        dict: Processed student data with final grade, or None if processing fails
    
    Error Handling Strategy:
    - KeyError: Missing required fields
    - ValueError: Invalid data conversion or out-of-range values
    - General Exception: Catch unexpected errors
    - Finally: Always execute cleanup code
    """
    try:
        # Step 1: Validate that all required fields are present
        # KeyError will be raised if any key is missing

        try:
            name = student['name']
            score_str = student['score']
            attendance_str = student['attendance']
        except KeyError as e:
            print(f"❌ Error: Missing required field {e}")
            return None
        
        # Step 2: Convert score to integer
        # ValueError occurs if score_str cannot be converted (e.g., "ninety")

        try:
            score = int(score_str)
        except ValueError:
            print(f"❌ Error: Invalid score '{score_str}' for {name}. Must be an integer.")
            return None
                
        # Step 3: Validate score is in valid range (0-100)
        # We RAISE a ValueError to signal validation failure

        if not (0 <= score <= 100):
            raise ValueError(f"Score {score} is out of range (0-100) for {name}")
        
        # Step 4: Convert attendance to float
        # Allows decimal values like 92.5

        try:
            attendance = float(attendance_str)
        except ValueError:
            print(f"❌ Error: Invalid attendance '{attendance_str}' for {name}. Must be numeric.")
            return None
        
        # Step 5: Validate attendance is in valid range (0-100)
        if not (0 <= attendance <= 100):
            raise ValueError(f"Attendance {attendance} is out of range (0-100) for {name}")
        
        # Step 6: Calculate final grade using weighted formula
        # 70% score + 30% attendance
        final_grade = score * 0.7 + attendance * 0.3
        
        # Step 7: Return processed data
        return {
            'name': name,
            'score': score,
            'attendance': attendance,
            'final_grade': round(final_grade, 2)
        }
    
    except ValueError as e:
        # Catch validation errors (raised by our range checks)
        print(f"❌ Validation Error: {e}")
        return None
    except Exception as e:
        # Catch any unexpected errors (defensive programming)
        print(f"❌ Unexpected error: {e}")
        return None
    finally:
        # ALWAYS executes, even if return or exception occurs
        # Useful for cleanup operations (closing files, connections, etc.)
        print("✓ Processing completed for record")


# ============================================================================
# PART 2: Batch Processing
# ============================================================================

def process_class_records(student_list):
    """
    Process multiple student records and track results.
    
    Args:
        student_list (list): List of student dictionaries
    
    Returns:
        dict: Summary with total, successful, failed counts and details
    
    Key Feature: Continues processing even when individual records fail
    This prevents one bad record from stopping the entire batch
    """
    # Initialize tracking variables
    successful_students = []
    errors = []
    successful_count = 0
    failed_count = 0
    
    print("\n" + "="*70)
    print("BATCH PROCESSING STARTED")
    print("="*70)
    
    # Process each student record
    for i, student in enumerate(student_list, 1):
        print(f"\n--- Processing Record {i} ---")
        
        # Try to get student name for error messages (might be missing)
        student_name = student.get('name', f'Record {i}')
        
        try:
            # Call our processor function
            result = process_student_record(student)
            
            if result:
                # Success! Add to successful list
                successful_students.append(result)
                successful_count += 1
                print(f"✅ SUCCESS: {result['name']} - Final Grade: {result['final_grade']}")
            else:
                # Processor returned None (error occurred)
                failed_count += 1
                errors.append(f"Failed to process {student_name}")
                print(f"⚠️  FAILED: {student_name}")
        
        except Exception as e:
            # Catch any unexpected errors from processor
            failed_count += 1
            error_msg = f"Unexpected error processing {student_name}: {str(e)}"
            errors.append(error_msg)
            print(f"❌ {error_msg}")
    
    # Create summary report
    summary = {
        'total_records': len(student_list),
        'successful_records': successful_count,
        'failed_records': failed_count,
        'successful_students': successful_students,
        'errors': errors
    }
    
    return summary


# ============================================================================
# PART 3: Safe Calculator
# ============================================================================

def calculate_class_average(grades):
    """
    Calculate average of grades with comprehensive error handling.
    
    Args:
        grades (list): List of numeric grades
    
    Returns:
        float: Average grade, or None if error occurs
    
    Demonstrates try-except-else-finally structure:
    - try: Attempt the calculation
    - except: Handle specific errors
    - else: Runs ONLY if no exception occurred
    - finally: ALWAYS runs
    """
    try:
        # Attempt to calculate average
        # This can raise ZeroDivisionError if grades is empty
        # or TypeError if grades contains non-numeric values
        total = sum(grades)
        average = total / len(grades)
        
    except ZeroDivisionError:
        # Empty list means len(grades) = 0
        print("❌ Error: Cannot calculate average of empty grade list")
        return None
    
    except TypeError as e:
        # Occurs if grades contains non-numeric values
        print(f"❌ Error: Invalid data type in grades list. All values must be numeric.")
        print(f"   Details: {e}")
        return None
    
    else:
        # This ONLY runs if NO exception occurred
        # Perfect for success messages
        print("✅ Calculation successful")
        return round(average, 2)
    
    finally:
        # ALWAYS executes, whether success or failure
        print("✓ Average calculation completed")


# ============================================================================
# BONUS: Grade with Division (10 extra points)
# ============================================================================

def grade_with_division(total_score, num_assignments):
    """
    Calculate average score per assignment with advanced error handling.
    
    Args:
        total_score (float): Total score across all assignments
        num_assignments (int): Number of assignments
    
    Returns:
        float: Average score per assignment
    
    Demonstrates:
    - Custom error raising with 'raise'
    - Multiple except blocks
    - Nested try-except blocks
    """
    try:
        # Outer try block: Input validation
        
        # Custom validation: Check for negative scores
        if total_score < 0:
            # Use 'raise' to create our own error
            raise ValueError("Total score cannot be negative")
        
        # Inner try block: Division operation
        try:
            average = total_score / num_assignments
            return round(average, 2)
        
        except ZeroDivisionError:
            # Division by zero (nested exception handling)
            print("❌ Error: Number of assignments cannot be zero")
            return None
        
        except TypeError:
            # Non-numeric values
            print("❌ Error: Both arguments must be numeric")
            return None
    
    except ValueError as e:
        # Catch our custom validation error
        print(f"❌ Validation Error: {e}")
        return None


# ============================================================================
# TEST CASES & DEMONSTRATION
# ============================================================================

def main():
    """
    Main function to demonstrate all components with test cases.
    """
    
    # Test data with various error scenarios
    test_students = [
        {'name': 'Alice Johnson', 'score': '85', 'attendance': '90'},      # Valid
        {'name': 'Bob Smith', 'score': 'ninety', 'attendance': '88'},      # Invalid score
        {'name': 'Carol White', 'score': '150', 'attendance': '95'},       # Score out of range
        {'score': '75', 'attendance': '80'},                                # Missing name
        {'name': 'Dave Brown', 'score': '78', 'attendance': '92.5'},       # Valid with decimal
        {'name': 'Eve Davis', 'score': '92', 'attendance': '-10'}          # Invalid attendance
    ]
    
    print("\n" + "="*70)
    print("STUDENT GRADE PROCESSING SYSTEM - DEMONSTRATION")
    print("="*70)
    
    # ========== PART 1 & 2: Process all records ==========
    summary = process_class_records(test_students)
    
    # Display summary
    print("\n" + "="*70)
    print("PROCESSING SUMMARY")
    print("="*70)
    print(f"Total Records: {summary['total_records']}")
    print(f"✅ Successful: {summary['successful_records']}")
    print(f"❌ Failed: {summary['failed_records']}")
    print(f"Success Rate: {(summary['successful_records']/summary['total_records']*100):.1f}%")
    
    if summary['successful_students']:
        print("\n--- Successful Students ---")
        for student in summary['successful_students']:
            print(f"  • {student['name']}: Score={student['score']}, "
                  f"Attendance={student['attendance']}, Final Grade={student['final_grade']}")
    
    if summary['errors']:
        print("\n--- Errors Encountered ---")
        for error in summary['errors']:
            print(f"  • {error}")
    
    # ========== PART 3: Calculate class average ==========
    print("\n" + "="*70)
    print("CLASS AVERAGE CALCULATION")
    print("="*70)
    
    # Extract final grades from successful students
    final_grades = [s['final_grade'] for s in summary['successful_students']]
    
    print(f"\nFinal grades: {final_grades}")
    average = calculate_class_average(final_grades)
    if average is not None:
        print(f"  Class Average: {average}")
    
    # Test error cases
    print("\n--- Testing Edge Cases ---")
    print("\n1. Empty list:")
    calculate_class_average([])
    
    print("\n2. Invalid data types:")
    calculate_class_average([85, 'ninety', 92])
    
    # ========== BONUS: Grade with Division ==========
    print("\n" + "="*70)
    print("BONUS: GRADE WITH DIVISION")
    print("="*70)
    
    print("\n1. Valid calculation:")
    result = grade_with_division(450, 5)
    if result:
        print(f"   Average per assignment: {result}")
    
    print("\n2. Division by zero:")
    grade_with_division(450, 0)
    
    print("\n3. Negative score:")
    grade_with_division(-100, 5)
    
    print("\n4. Invalid type:")
    grade_with_division(450, 5)
    
    print("\n" + "="*70)
    print("DEMONSTRATION COMPLETE")
    print("="*70)


# Run the demonstration
if __name__ == "__main__":
    main()