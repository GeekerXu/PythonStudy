import random
import time
secret = random.randint(1,9)
print('-------------------------Geeker Xu------------------------')
temp = input('不妨猜一下Geeker Xu现在心里想的是哪个(1-9)数字，有3次机会：')


while str.isdigit(temp) == 0:
    temp = input('请输入(1-9)数字，这次不算，重新输入：')

    
guess = int(temp)
i = 3
if guess == secret:
    print('我操，你是Geeker Xu心里的蛔虫吗？！')
    print('哼，猜中了也没有奖励！')
else:
    if guess > secret:
        print('哥，大了~大了！！！')
    else:
        print('嗨，小啦~小啦！！！')
    while guess != secret and i>1:
        i=i-1
        print('还有',i ,'次机会') 
        temp = input('哎呀，输错了，请重新输入吧：')
        while str.isdigit(temp) == 0:
            temp = input('请输入(1-9)数字，这次不算，重新输入：')
        guess = int(temp)
        if guess == secret:
            print('我操，你是Geeker Xu心里的蛔虫吗？！')
            print('哼，猜中了也没有奖励！')
        else:
            if guess > secret:
                print('哥，大了~大了！！！')
            else:
                print('嗨，小啦~小啦！！！')
print('游戏结算，不玩啦，哈哈！！正确答案是',secret)
print('5秒后退出游戏！！！')
time.sleep(5)
	
