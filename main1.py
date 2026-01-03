#write a proggram to chheck whether a student can take the exam or not. students will be allowed only in two conditions. if they have a medical cause(sick) "Y" for yes and "N" not sick. if yes then they will be allowed to take the exam. if NO chheck the attendence if the attendence is less than 75 tey will not be allowed to take the text. if greater then allowed to take test
medical_cause=input("Enter 'Y' if you have a medical cause else write 'N' for no medical cause: ")
attendence=int(input("Enter your attence percentage: "))
if medical_cause=="Y":
    print("You are allowed to take the exam")
elif medical_cause=="N":
    if attendence>=75:
        print("You are allowed to give the exam")
    else:
        print("You are not allowed to give the exam because your attendence is short.")
else:
    print("Invalid input type Y for yes and N for no.")