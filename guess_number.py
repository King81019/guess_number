import random
max = input('請決定數字上限：')
min = input('請決定數字下限：')
max = int(max)
min = int(min)
r = random.randint(min, max)
n = 0
while r > 0:
    n += 1  #n = n + 1
    guess = input('請猜數字：')
    guess = int(guess)
    print('這是你猜的第', n, '次')
    if guess == r:
        print('猜對了！')
        break
    elif guess < r and guess > min:
        print('太小了喔！')
    elif guess > r and guess < max:
        print('太大了喔！')
    else:
        print('數字範圍錯誤！請輸入', min, '~', max, '之間的整數')
    

