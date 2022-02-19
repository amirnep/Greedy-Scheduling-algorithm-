class schedule(object):
    def __init__(self):
        self.arr = []
        self.r = 0
        self.ans = []
        self.job = []
        
    def input_numbers(self): #To input times ans profits of jobs.
        n = int(input("How many job do you want to add: "))

        for i in range(1,n+1):
            array = []
            t = int(input("Enter job {} time: ".format(i)))
            p = int(input("Enter profit of job {}: ".format(i)))
            array.append(i)
            array.append(t)
            array.append(p)
            self.arr.append(array)
            print()

        self.r = max(self.arr,key = lambda lst: lst[1])[1] #Maximum time of jobs

    def schedulejobs(self):
        schedule.input_numbers(self)

        n = len(self.arr)

        self.arr = sorted(self.arr,key = lambda lst: lst[2]) #Sort jobs by profits

        self.arr = self.arr[::-1] #Reverse jobs by profits --> Max to Min
    
        self.ans = [''] * self.r

        self.job = [''] * self.r #Array for jobs

        for i in range(n): #Schedule algorithm
            for j in range((self.arr[i][1] - 1), -1, -1):
                if self.ans[j] == '': 
                    self.ans[j] = 'T'
                    self.job[j] = self.arr[i][0]
                    break

        return self.job

    def profit(self): #To print All profits
        sum_ = 0

        for i in range(self.r):
            a = self.arr[self.job[i]-1]
            b = a[2]
            sum_ += b

        return sum_

    def time(self): #To print All Time
        sum_ = 0

        for i in range(self.r):
            a = self.arr[self.job[i]-1]
            b = a[1]
            sum_ += b

        return sum_
