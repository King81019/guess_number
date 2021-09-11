import random
r = random.randint(1, 100)
n = 0
while r > 0:
    n += 1  #n = n + 1
    guess = input('請輸入數字1~100整數：')
    guess = int(guess)
    print('這是你猜的第', n, '次')
    if guess == r:
        print('猜對了！')
        break
    elif guess < r and guess > 0:
        print('太小了喔！')
    elif guess > r and guess < 100:
        print('太大了喔！')
    else:
        print('數字範圍錯誤！')
    

