#My calculator calculates how far one can run using three inputs 
SPEED = int(input("What is your average speed (in MPH) during the run? "))
#Speed will need to be in Miles per hour
RUNTIME = int(input("How long (in MINTUES) will your ENTIRE run (including break time) be? "))
#Runtime is the amount of time you plan to run, including the amount of time you would need for break
BREAKTIME = int(input("How long will your break be? "))
#Breaktime is the amount of time you will be standing still in your planned run, regaining energy
Final_Distance = ((RUNTIME - BREAKTIME)/60)*SPEED

print (F"Your computed running distance is {Final_Distance} miles!")

