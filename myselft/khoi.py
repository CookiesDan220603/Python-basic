def sumarry (arr,n,a):
	tong =0
	j=0
	k=0
	count =0
	for i in range (1,n+1):
		count =0
		for j in range (0,a):
			if int(arr[j])>0:
				if i%int(arr[j])==0:
					count+=1
		if count >0:
			tong +=i
	return tong
n =int(input("Nhập n : "))
arr=[]
a = int (input())
for i in range (0,a):
	arr.append(input())
arr.sort()
print (arr)

print (sumarry(arr,n,a))
