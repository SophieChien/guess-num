import random #載入模組
r = random.randint(1, 100)
while True:
	num = input('請猜數字：')
	num = int(num) #型別轉換（casting)
	if num == r:
		print('終於猜對了！！！')
		break
	elif num > r:
		print('比答案大喲')
	else:
		print('比答案小喲')
