def get_details(name,gender,roll):
	return  'Name:' + str(name) + '\nGender:' + str(gender) + '\nRoll: ' + str(roll)

def get_grade(marks):
	if marks >100 or marks <0:
    		return "Marks ", str(marks) , " is invalid"
	elif marks >= 70:
		return "Grade is A"
	elif marks >= 60:
	    return "Grade is B"
	elif marks >=40 :
	      return "Grade is C"
	else :
	    return "You have Failed"

