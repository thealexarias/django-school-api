from django.core.exceptions import ValidationError
import re

def validate_name_format(name:str) -> ValidationError:
    error_message = 'Name must be in the format "First Middle Initial. Last"'
    pattern = r'^[A-Z][a-z]+ [A-Z]\. [A-Z][a-z]+$'
    good_name = re.match(pattern, name)
    if good_name:
        return name
    else:
        raise ValidationError(error_message, params={'name' : name})
    
    

    
def validate_school_email(student_email:str) -> ValidationError:
    error_message = 'Invalid school email format. Please use an email ending with "@school.com".'
    pattern = r'^[A-Za-z0-9._%+-]+@school\.com$'
    good_stu_email = re.match(pattern, student_email)
    if good_stu_email:
        return student_email
    else:
        raise ValidationError(error_message, params={'student_email' : student_email})


def validate_combination_format(combo:str) -> ValidationError:
    error_message = 'Combination must be in the format "12-12-12"'
    pattern = r'^\d{2}-\d{2}-\d{2}$'
    good_combo = re.match(pattern, combo)
    if good_combo:
        return combo
    else:
        raise ValidationError(error_message, params={'locker_combonation' : combo})