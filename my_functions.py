

# custom-functions/my_functions.py


# TODO: define temperature conversion function here

def function (c):
    return (1.8 * c) + 32

c = 0
f= function (c)

# print (c)
# print (f)

# TODO: define gradebook function here

if __name__ == "__main__":

    print("--------------------")
    print("CUSTOM FUNCTIONS EXERCISE...")

    print("--------------------")
    c = 0
    print("THE CELSIUS TEMP IS:", c, "DEGREES")
    # f = celsius_to_fahrenheit(c)
    print("THE FAHRENHEIT EQUIVALENT IS:", f, "DEGREES")

    score = 87.5
    print("--------------------")
    print("THE NUMERIC SCORE IS:", score)

#    def grade = numeric_to_letter_grade(score):
def determineGrade(score):
    if (score < 60):
        return "F"
    elif (score > 70):
        return "A"
print ("Grade", score)
#     grade = numeric_to_letter_grade(score):

# function overtScoreToGrade(grade)
#     if  score > 93:
#          rade ='A'  
#     elif  score < 93:
#             grade 'B' 
#     elif  score < 70:
#             grade 'C'    
#     else : grade 'D'    
#     print("THE LETTER-GRADE EQUIVALENT IS:", grade)