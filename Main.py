#Algorithm Design: Dr. Pira
#Chapter3 Project by Amir Nematpour - 981830281
#Shahid Madani University

import Class as c

if __name__ == '__main__': #Run program.
    s = c.schedule()
    print("The jobs with high profits: ",s.schedulejobs()) #Jobs
    print()
    print("All profit is: ",s.profit()) #Profit
    print()
    print("The Time to do that jobs is: ",s.time()) #Time
    print()

quit = input("Press Enter to Exit Program.")
