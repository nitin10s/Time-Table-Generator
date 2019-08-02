# Python program for timetable generation using M Coloring
import os
import sys
import ascii
import time
from datetime import datetime, timedelta

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'

   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

#To keep the allotment within the range of no. of classrooms provided
count=[0]*30
# mylist=[['f1',maths],['f1',maths],['f1',maths],['f1',maths],['f1',maths]]


def datetime_range(start, end, delta):
    current = start
    while current < end:
        yield current
        current += delta
def fun(interval,breaks):
    new=[]
    dts1 = [dt.strftime('%H:%M') for dt in
           datetime_range(datetime(2016, 9, 1, 9), datetime(2016, 9, 1, 9+8),
           timedelta(minutes=interval+breaks))]
    return dts1

# To know the batch no. of the subject
def newfun(subj):
	cnt=0
	ans=[]
	for i in s_list:
		if subj in i:
			ans.append(cnt)
			cnt+=1
		else:
			cnt+=1
	return ans



class Graph():

    #Constructor
	def __init__(self, vertices):
		self.V = vertices
		self.graph = [[0 for column in range(vertices)]
							for row in range(vertices)]

	# A function to check if the current allotment
	# is safe for vertex v
	def isSafe(self, v, colour, c):
		for i in range(self.V):
			if (self.graph[v][i] == 1 and colour[i] == c) or count[c]>rooms-1: #if rooms are still available for the current slot or not
				return False
		return True

	# A recursive utility function to solve m
	# coloring problem
	def graphColourUtil(self, m, colour, v):
		if v == self.V:
			return True

		for c in range(1, m+1):

			if self.isSafe(v, colour, c) == True:
				colour[v] = c
				count[c]+=1 #
				if self.graphColourUtil(m, colour, v+1) == True:
					return True
				colour[v] = 0
				count[c]-=1


	def graphColouring(self, m):
		colour = [0] * self.V
		if self.graphColourUtil(m, colour, 0) == False:
			return False

		# Print the solution
		print "Following is the slot distribution--"
		print ""
		c=list(zip(colour,temp_list))
		final_d={} #Adjency list of common slot
		for i in range(len(colour)):
			try:
				final_d[c[i][0]].append(c[i][1])

			except:
				final_d[c[i][0]]=[c[i][1]]

		for a,b in final_d.items():
			temp=0
			print color.BOLD + "Time Slot : " + color.END ,arr[a-1] +  "-" + arr[a]
			print "----------------------"
			print "Batch        Subject        Room"
			print ""
			for j in b:
				bth=newfun(j) #Return list of batches where the subject was
				for newt in range(len(bth)):
					print "%-11d" %(bth[newt]+1),
					print "   " + "%-15s" %(j) + rooms_ar[temp] #j=subject
				temp+=1
			print ""
			print ""



d={}
set_subj=set()
s_list=[]


# print color.BOLD + "Problem Statement :" + color.END
# print "Making Schedule or Time Table: Suppose we want to make am exam schedule for a university."
# print "We have list different subjects and students enrolled in every subject."
# print "Many subjects would have common students (of same batch, some backlog students, etc)."
# print "How do we schedule the exam so that no two exams with a common student are scheduled at same time?"
# print "How many minimum time slots are needed to schedule all exams?"
# print "This problem can be represented as a graph where every vertex is a subject and an edge between two vertices mean there is a common student."
# print "So this is a graph coloring problem where minimum number of time slots is equal to the chromatic number of the graph."
# print ""
# print ""
print ""
print ""
print "By Ishjot Singh - 9917103256"
print "By Nitin Singhal - 9917103264"
print ""
print ""

time.sleep(2)
os.system('CLS')

print color.BOLD + "Constraints considered :" + color.END
print "1. Each subject is taught by one faculty."
print "2. Each batch can be taught only one subject in one time slot."
print "3. Only a particular number of rooms are available to take class."
print "4. Classes of different batches can be combined if needed."
print ""
print ""



print "Press Enter to Proceed..."
sys.stdin.read(1)


os.system('CLS')

print color.BOLD + "----------TimeTable Scheduling Program-------------" + color.END
print ""
rooms_ar=raw_input(color.UNDERLINE + "Enter the rooms available for allotment (separated by space)" +color.END + " - " ).split()
rooms=len(rooms_ar)
i = int(raw_input(color.UNDERLINE + "Enter the duration of each class (in mins)" +color.END + " - " ))
j = int(raw_input(color.UNDERLINE + "Enter the break time between classes (in mins)" +color.END + " - " ))
arr=fun(i,j)
# for i in range(0,len(arr)-1):
#     print arr[i],arr[i+1]


n=input(color.UNDERLINE + "Enter no. of batches" +color.END + " - " )
print ""
t=n
while t>0:

    x=map(str,raw_input("Enter subjects for batch" + color.RED +  " %i" %(n-t+1) + color.END + " - ").split())
    s_list.append(x)
    for i in x:
        set_subj.add(i)
    t=t-1
print ""


temp_list=list(set_subj)

len_sub=len(temp_list)

for i in range(len_sub):
    d[temp_list[i]]=i

# matrix=[[0 for column in range(len_sub)] for row in range(len_sub)]
# print matrix

g = Graph(len_sub)

for i in s_list:
    for j in i:
        for k in i:
            if j==k:
                continue
            else:
                g.graph[d[k]][d[j]]=1

m=30 #MAX_INT
os.system('CLS')
g.graphColouring(m)
