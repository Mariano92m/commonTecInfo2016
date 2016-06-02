def tipo(k):
	sum=0
	for x in range (1,k-1):
		if (k%x==0):
			sum=sum+x
	if sum==k:
		return ("perfecto")
	elif sum < k:
		return ("deficiente")
	else:
		return ("abundante")
