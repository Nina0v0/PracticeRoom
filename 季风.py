#开篇
name = input("管理员，请验证您的代号:")
print(f"验证通过。欢迎来到季风,",name,",这里是无人知晓的地下诗社。\n我是Neo,您的助手。\n今天只想四处转转吗？还是查看您的新邮件？Neo能帮您做什么？")#引导语
#以下为初始化成就变量（布尔值）
is_poem_read = False#四处转转-是否听Neo读过诗
is_letter_read = False#查看邮箱-是否已浏览过未读信件
is_reply_sent = False#查看邮箱-是否已回复信件
#下面是主程序
Running = True#此处为主循环设定变量Running，是为了便利“无论何时输入0都能退出程序”功能的实现，起到保险，否则仅靠break，不方便既退出当前所在的子循环，又退出决定程序是否运行的主循环。
while Running:
    choice = input("Neo一次只能完成一次量子跃迁。所以您只能选择:1或者2,四处转转,或者查看您的邮筒。\n如您想要离开,请输入0,返回进程不受时限,随时都可以。\n请输入数字编码，Neo会为您执行:")
    #以下为检测是否存在错误输入
    if choice.isdigit():#判断用户输入是否为纯数字
        choice = int(choice)#如果是数字，转换为整数
        #以下为判断剧情选择   
        if choice == 0:
            print(f"好的{name},Neo将在这里静候您的下一次访问。祝您愉快。\n\n…夜幕下,季风仍在低语…")
            Running = False#给主循环发出信号，停止整个程序
            break#保险，退出子循环
        elif choice == 1:
            print(f"好的{name},Neo陪伴您四处转转。\n你踏入季风的夜晚……\n沿着红砖小径向前走。一个转弯，然后是一个上坡。\n煤油灯的微光下，你看到一个戴粉红色亚麻头巾的身影坐在台阶上。")
            pink_headband = "流浪诗人"
            poems_written = 316
            print(f"{name},您遇见了{pink_headband}。他的背包里有{poems_written}首诗。")
            is_poem_read = False#使用布尔值跟踪成就变量
            #下面是是否要读诗的选择，考虑到可能有误输入，需要重新输入，所以不仅使用if控制，而是使用循环。
            while True:
                pink_poem = input("您想听一首吗？Neo乐意为您效劳。您只需要回答是或否。")
                pink_poem.strip()#去除回答里的空格
                if pink_poem == "0":
                    print(f"好的{name},Neo将在这里静候您的下一次访问。祝您愉快。\n\n…夜幕下,季风仍在低语…")
                    Running = False#告诉主循环退出程序
                    break#同时退出子循环，保险
                elif pink_poem == "是":
                    is_poem_read = True#记录成就
                    print(f"【Neo清了清嗓子。】\n⌈我走过他走过的地方。\n向着晚风我伸出手,\n想象这只手穿过时间\n替他整理沾上泥土的帽子。⌋\n啊,是首情诗,{name}。\n让我们继续。")
                elif pink_poem == "否":
                    print(f"好的{name},将军赶路,不追小兔。\n你踏入季风的夜晚……\n登上石条垒砌而成的台阶。穿过狭窄的小巷，道路变得宽敞。\n让我们继续。")
                else:
                    print(f"您输入的编码无效,管理员{name}。事实证明就算是天才也会犯错误,您认为呢？")
                break#退出是否读诗循环
        elif choice == 2:
            print(f"好的{name},Neo帮您查看邮筒，请稍等。")
            unread_letters = 1
            latest_sender = "未知发件人"
            print(f"{name},您有{unread_letters}封未读邮件。\n最新的邮件来自:{latest_sender}。")
            is_letter_read = False#布尔值跟踪成就变量
            while True:
                new_letter = input("您想阅读它吗？Neo乐意为您效劳。您只需要回答是或否。").strip()#去除空格
                #检测是否读信
                if new_letter == "0":#是否读信
                    print(f"好的{name},Neo将在这里静候您的下一次访问。祝您愉快。\n\n…夜幕下,季风仍在低语…")
                    Running = False
                    break
                elif new_letter == "是":#是否读信
                    is_letter_read = True#记录成就
                    print(f"好的{name}。这里是{latest_sender}的邮件内容:\n⌈月色撕开夜的前襟。黑暗在流血。⌋\n看来是封加密信件,{name}。")
                    write_back = input(f"您想回信吗？{name}。Neo乐意为您效劳。您只需要回答是或否。")
                    is_reply_sent = False#跟踪成就变量
                    #检测是否回信
                    if write_back == "0":#是否回信
                        print(f"好的{name},Neo将在这里静候您的下一次访问。祝您愉快。\n\n…夜幕下,季风仍在低语…")
                        Running = False
                    elif write_back == "是":#是否回信
                        back_letter = input(f"好的{name},请输入您想要回信的内容。")
                        print(f"叮咚！Neo已帮您将回信发出。\n让我们继续。")
                    elif write_back == "否":#是否回信
                        print(f"好的{name},已读不回有时也是明智的选择,Neo相信您的判断。\n让我们继续。")
                    else:#是否回信
                        print(f"您输入的编码无效,管理员{name}。事实证明就算是天才也会犯错误,您认为呢？")
                        continue#这里的continue针对的是如果用户在此选择支内输入除是、否、0以外的其它内容，则重复询问一次。如没有这个continue，则会回到主循环并重新询问。
                elif new_letter == "否":#是否读信
                    print(f"好的{name},Neo已为您将邮件妥当收好，留待您方便时再读。\n让我们继续。")
                else:#是否读信
                    print(f"您输入的编码无效,管理员{name}。事实证明就算是天才也会犯错误,您认为呢？")
                    continue#重新询问是否读信
                break#退出是否读信循环
        else:#这里是针对主循环选0、1、2以外其它数字的反馈
                print(f"您输入的编码无效,管理员{name}。事实证明就算是天才也会犯错误,您认为呢？\n季风仍然沉睡在夜色之中。")
                continue#跳过本次循环的剩余部分，直接进入下一次循环，即再次询问
    else:#这里是针对主循环输入非数字的反馈
        print(f"您输入的编码无效,管理员{name}。事实证明就算是天才也会犯错误,您认为呢？\n季风仍然沉睡在夜色之中。")
        continue#跳过本次循环的剩余部分，直接进入下一次循环，即再次询问
