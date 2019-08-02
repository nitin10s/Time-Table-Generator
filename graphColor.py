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
