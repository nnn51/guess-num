# 產生一個隨機整數(1-100)
# 讓使用者重複輸入數字去猜
# 猜對 印出"終於猜對了
# 猜錯 印出"比答案大/小"

import random
min = input('請決定隨機數字範圍最小值:')
min = int(min)
max = input('請決定隨機數字範圍最大值:')
max = int(max)

r = random.randint(min, max)
count = 0  
	# 要寫再while的外面，若寫在裡面，代表每進入while一次，count就又變回0

while True:
	count += 1   # count = count + 1 的速寫法
	num = input('請猜數字:')
	num = int(num)
	if num == r:
		print('Bingo~! 答案是', r)
		print('經過', count, '次後，終於猜對了!')
		break
	else:
		if num > r:
			print('比答案大')
		else:
			print('比答案小')
	print('這是你猜的第', count, '次')				