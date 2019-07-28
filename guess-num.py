import random #載入模組
r = random.randint(1, 100)
count = 0
while True:	
	num = input('請猜數字：')
	num = int(num) #型別轉換（casting)
	count += 1 #count =count + 1
	print('目前猜第', count,'次')
	if num == r:
		print('終於猜對了！！！')
		break
	elif num > r:
		print('比答案大喲')
	else:
		print('比答案小喲')
	
	
