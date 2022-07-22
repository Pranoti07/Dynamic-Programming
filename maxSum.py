#Dynamic programming approach to find maximum contiguous sum of subarray 
import random                     
from datetime import datetime
class Dynamic:
  def maxSumSubArray(self,a,size):
    max_sum=0                     #maximum sum initialized to zero
    max_end=0                     #max sum ends intialized to zero
    for x in range(0,size): 
      max_end=max_end+a[x]        #adding elements to find max sum
      if (max_end<0):
        max_end=0
      elif (max_sum < max_end):     #max sum gets updated to highest value so far
        max_sum=max_end
    return max_sum                  #returns maximum sum

  def run(self):
    while True:
      N=0     
      user_input=input("Enter number of elements(N) or type Quit to end:")                        #taking input from user
      if (user_input=='Quit'):        #if user wants to quit
        print("Terminating")
        return 
      try:
        N=int(user_input)               #user input assigned to N(number of elements)
      except:
        print("Invalid Input")          #when there is exception
        continue
      
      random_array=[random.randint(-20,20)for i in range(N)]    #generating random array as input using random function
      if (N<=20):
        print(random_array)       #if array is small then print elements of array
      print()
      print("\tTrying random input array of length N:",str(N)) #printing 
      start_time=datetime.now()    
      print("\tMaximum contiguous sum:", self.maxSumSubArray(random_array,N))           #function call
      end_time=datetime.now()
      time_taken=(end_time-start_time).microseconds   #to compute run time
      print("\tRuntime Performance",(N,time_taken))
      print()
obj=Dynamic()                 #creating object of class
obj.run()                     #function call



