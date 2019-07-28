while True:
	import random
	r = random.randint(1, 5)
	num = input('請猜數字：')
	num = int(num). #型別轉換（casting)
	if num == r:
		print('終於猜對了！！！')
		break
	elif num > r:
		print('比答案大喲,答案是', r)
	else:
		print('比答案小喲,答案是', r)
