mini=1
maxm=100

import random
ans=random.randint(mini,maxm)
win=True
while win:
    x=int(input())
    if x==ans:
        print("win")
        win=False
    elif x<ans:10
        mini=x
        print("請輸入"+str(mini)+"~"+str(maxm)+"之間")
        continue
    elif x>ans:
        maxm=x
        print("請輸入"+str(mini)+"~"+str(maxm)+"之間")
        continue
    elif x<=mini or x>=maxm:
        print("輸入錯誤，請輸入"+str(mini)+"~"+str(maxm)+"之間")
