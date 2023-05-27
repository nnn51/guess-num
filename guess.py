# 產生一個隨機整數(1-100)
# 讓使用者重複輸入數字去猜
# 猜對 印出"終於猜對了
# 猜錯 印出"比答案大/小"

import random
r = random.randint(1, 100)

while True:
	num = input('請輸入數字:')
	num = int(num)
	if num == r:
		print('Bingo~! 答案是', r)
		break
	else:
		if num > r:
			print('比答案大')
		else:
			print('比答案小')		