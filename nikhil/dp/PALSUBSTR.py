def is_pal(str1):
	a=str1[::]
	b=str1[::-1]
	return a==b and len(a)>1
my_str=[]
my_res=[]
def CountPS(str, n):
	count=0
	for i in range(len(str)):
		for j in range(i,len(str)):
			if is_pal(str[i:j+1]):
				my_str.append(str[i:j+1])
	for i in range(len(str)):
		for j in range(i,len(str)):
			for k in my_str:
				if str[i:j+1].find(k)!= -1:
					my_res.append(str[i:j+1])

	return len(set(my_res))

if __name__ == "__main__":

	str = input()
	n = len(str)
	print(CountPS(str, n))
