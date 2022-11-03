name=input("Please type your name to get started  ")
print( name,"Welcome ,It's a quiz game consisting of 25 questions all you need to do is give out it's longest form :) ")
playing=input("Do you want to play? Type YES to continue and NO to quit :) ")
if playing.lower() !="yes":
    quit()
print("okay!Lets play")
score=0

#QUESTION ONE
answer=input("GNU ")
if (answer.lower()=="GNU'S not UNIX".lower()):
    print("correct!")
    score=score + 1
else:
    print("Incorrect!") 

#QUESTION TWO
answer=input("CPU ")
if (answer.lower()== "Central Processing Unit".lower()):
    print("correct!")
    score=score+1
else:
    print('Incorrect!')

#QUESTION THREE
answer=input("FAANG ")
if (answer.lower()=="Facebook Amazon Apple Netflix Google".lower()):
    print("correct!")
    score=score+ 1
else:
    print("Incorrect!")       

#QUESTION FOUR
answer=input("OOP ")
if (answer.lower()=="Object Oriented Programming".lower()):
    print("correct!")
    score=score+ 1
else:
    print("Incorrect!")     

#QUESTION FIVE
answer=input("MAANG ")
if (answer.lower() == "Meta Amazon Apple Netflix Google".lower()):
    print("correct!")
    score=score+1
else:
    print('Incorrect!')

#QUESTION SIX
answer=input("DES ")
if (answer.lower()=="Data Encryption Standard".lower()):
    print("correct!")
    score=score+ 1
else:
    print("Incorrect!")       

#QUESTION SEVEN
answer=input("NUMPY ")
if (answer.lower()=="Numerical Python".lower()):
    print("correct!")
    score=score+ 1
else:
    print("Incorrect!")       

#QUESTION EIGHT
answer=input("URL ")
if (answer.lower()=="Uniform Resource Locator".lower()):
    print("correct!")
    score=score+ 1
else:
    print("Incorrect!")  
               

#QUESTION NINE
answer=input("SQL ")
if (answer.lower()=="Structured Query Language".lower()):
    print("correct!")
    score=score+ 1
else:
    print("Incorrect!")           

#QUESTION TEN
answer=input("SMTP ")
if (answer.lower() == "Simple Mail Transfer Protocol".lower()):
    print("correct!")
    score=score+1
else:
    print('Incorrect!')

#QUESTION ELEVEN
answer=input("HTTP ")
if (answer.lower()=="HyperText Transfer Protocol".lower()):
    print("correct!")
    score=score+ 1
else:
    print("Incorrect!")       

#QUESTION TWELVE
answer=input("ESMTP ")
if (answer.lower()=="Extended Simple Mail Transfer protocol".lower()):
    print("correct!")
    score=score+ 1
else:
    print("Incorrect!")    

#QUESTION THIERTEEN
answer=input("TCP ")
if (answer.lower() == "Transmission control Protocol".lower()):
    print("correct!")
    score=score+1
else:
    print('Incorrect!')

#QUESTION FOURTEEN
answer=input("IP  ")
if (answer.lower()=="Internet Protocol".lower()):
    print("correct!")
    score=score+ 1
else:
    print("Incorrect!")       

#QUESTION FIFTEEN
answer=input("DDOS  ")
if (answer.lower() =="Distributed Denial of Service ".lower()):
    print("correct!")
    score=score+1
else:
    print('Incorrect!')

#QUESTION SIXTEEN
answer=input("AES ")
if (answer.lower()=="Advanced Encryption Standard".lower()):
    print("correct!")
    score=score+ 1
else:
    print("Incorrect!")       


#QUESTION SEVENTEEN
answer=input("FIFO ")
if (answer.lower ()=="First In First Out".lower()):
    print("correct!")
    score=score+1
else:
    print('Incorrect!')

#QUESTION EIGHTEEN
answer=input("OSI ")
if (answer.lower()=="Open Source Initiative".lower()):
    print("correct!")
    score=score+ 1
else:
    print("Incorrect!")       

# QUESTION NINETEEN 
answer=input("SSL ")
if (answer.lower() == "Secure Socket Layer".lower()):
    print("correct!")
    score=score+1
else:
    print('Incorrect!')

#QUESTION TWENTY
answer=input("Scipy")
if (answer.lower()=="Scientific Python".lower()):
    print("correct!")
    score=score+ 1
else:
    print("Incorrect!")       



               
print("you got " +str(score) + " questions corrrect! out of 20 questions")   
print( name," Thank you for playing :) , This is your percentage " +str(((score)/20)*100) + "%.")  