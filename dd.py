def guest_list(guests):
	for three in guests:
		for guest in three:
			print(guests)

		  #print("{} is {} years old and works as {}".format(guests))
guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])

"""
Output should match:
Ken is 30 years old and works as Chef
Pat is 35 years old and works as Lawyer
Amanda is 25 years old and works as Engineer
"""