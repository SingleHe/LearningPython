import random  # 随机数的标准库，随着Python环境安装好的库
strs = "ABCD"
who = random.choice(strs)  # 从strs随机取单个字符串

# print("当前随机的字母为：{who}")
# count = 0
# if who == inp:
#     print("这都能猜对，运气真好！")
# else:
#     inp2 = input("您还有两次机会，请再试一次：")
#     if inp2 == who:
#         print("恭喜你，在第二次猜对了！")
#     else:
#         inp3 = input("您还有最后一次机会，请再试一次：")
#         if inp3 == who:
#             print("终于答对了！")
#         else:
#             print("您没有机会了！")
count = 0
total = 3
while True:
    inp = input("请输入ABCD四个字母中的一个，猜系统给的正确答案是啥：")
    if inp == who:
        print("系统随机的值为：%s" % who)
        print("这你都能猜对，你太厉害了！")
        break
    else:
        count += 1
        if count >= 3:

            print("很遗憾，您还是猜错了，且您已经用完三次机会了，请充值！")
            break
        else:
            print("很遗憾，您猜错了！您还有{}次机会".format(total-count))
