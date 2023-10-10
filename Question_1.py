
cont = 'y'



print ("Letter Grade Converter")

while (cont == 'y'):
    grade = int(input("\nEnter numerical grade:\t"))
    
    if (grade >= 88):
        print ("Letter grade: A")
        
        cont = input("\nContinue? (y/n) ")
        
    elif (grade <= 87 and grade >= 80):
        print ("Letter grade: B")
        
        cont = input("\nContinue? (y/n) ")
    
    elif (grade <= 79 and grade >= 67):
        print ("Letter grade: C")
        
        cont = input("\nContinue? (y/n) ")
    
    elif (grade <= 66 and grade >= 60):
        print ("Letter grade: D")
        
        cont = input("\nContinue? (y/n) ")
        
    elif (grade < 60 and grade >= 0):
        print ("Letter grade: F")
        
        cont = input("\nContinue? (y/n) ")
    
    else:
        grade = ("ERROR")


print ("\nBye!")