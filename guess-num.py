import random #載入模組
start = input('請決定隨機數字範圍開始值：')
end = input('請決定隨機數字範圍結束值：')
start = int(start)
end = int(end)
r = random.randint(start, end)
count = 0
while True:	
	num = input('請猜數字：')
	num = int(num) #型別轉換（casting)
	count += 1 #count =count + 1
	print('目前猜第', count,'次,')
	if num == r:
		print('終於猜對了！！！')
		break
	elif num > r:
		print('比答案大喲.')
	else:
		print('比答案小喲.')
	
	
