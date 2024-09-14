
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list = [*list1, *list2]  # 解包两个列表并合并
print(combined_list)  # 输出 [1, 2, 3, 4, 5, 6]

if __name__ == '__main__':
    print('需要执行一些解包的示例')