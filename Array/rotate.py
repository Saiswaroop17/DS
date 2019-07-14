import math

li = [1,2,3,4,5,6,7,8]
n = len(li)
k= 2 #No of elements to rotate anti clockwise

#1 Can use a temp array to store first d elements and then shift the rest of elements left and finally append the temp array
#2 JUGGLING ALGORITHM
gcd = math.gcd(n, k)

for i in range(gcd):
	j = i
	t = li[j]

	while(1):
		d = (j+k)%n # Element of set i to be shifted left
		
		if d==i:
			break  #Cycle formed

		li[j] = li[d] # Shifting left
		j=d
	li[j] = t

print(li)
