a_1 = 2
Five_First_Terms = [a_1]
a_n = a_1

for i in range(0, 4):
	a_next = a_n / (a_n + 1)
	Five_First_Terms.append(a_next)
	a_n = a_next

print(Five_First_Terms) 
 # Bài này chỉ làm câu f