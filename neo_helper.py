your_name = input("管理员，请验证您的代号:")
print(f"您好{your_name}!我是Neo，您的助手。请告知我今天需要进行的事项，我会为您安排。")
to_do_list = input("您写在这里，我会记住。>>>")
print(f"好的{your_name}!您的今日日程是:【{to_do_list}】。请确认无误！")
infirmation = input("是否无误？请输入是或否:")
if infirmation == "是":
    print(f"已知悉！Neo现在为您安排。")
elif infirmation == "否":
    print(f"抱歉{your_name}，Neo搞错了。")
    new_to_do_list = input("辛苦您再次重复，Neo会牢牢记住！>>>")
    print(f"好的{your_name}!您的今日日程是:【{new_to_do_list}】。请确认无误！")
else:
    print(f"抱歉{your_name}!只能输入 是 或 否。")
    