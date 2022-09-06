driv = input("是否有開過車?: ")
if driv != "是" and "否":
	print("我糙你大爺的")
age = input("年齡: ")
if driv == "是":
	if int(age) < 18:
		print("不行犯法")
	else:
		print("飆起來")
elif driv =="否":
	if int(age) < 18:
		print("乖孩子")
	else:
		print("去考照孩子")
