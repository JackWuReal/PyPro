"""
学生信息
姓名 name
年龄 age
性别 sex
用字典来存储的单个学生
用列表来存储多个学生信息
"""

list = []
# show_info 函数展示学生信息


def show_info():
    code = input("please input the number you want\n1.添加学生\n2.删除学生\n3.修改学生信息"
                 "\n4.查询单个学生信息\n5.查询所有学生信息\n6.退出系统")
    return int(code)

def add_stu():
    name = input('请输入学生名字')
    for info in list:
        if info['name'] == name:
            print('已有该学生,请勿重复添加')
            return   # 结束该函数
    age = input('请输入学生年龄')
    sex = input('请输入学生性别')
    dirct = {'name': name, 'age': int(age), 'sex': sex}
    list.append(dirct)


def modify_stu(name):
    dict_name = find_stu_by_name(name)
    if dict_name != False:
        new_age = input("请输入新的年龄")
        dict_name.__setitem__('age', new_age)



def find_stu_by_name(name):
    for i in list:
        if i['name'] == name:
            print(f'{name}的信息如下')
            return i
    print(f'未找到姓名{name}的学生')
    return False


def display_all_stu():
    print(list)


def delete_stu_by_name(name):
    for i in list:
        if i['name'] == name:
            list.remove(i)
            print(f'删除{name}用户成功')
            return i
    print(f'未找到{name}的学生')

def run():
    while True:
        code = show_info()
        if code == 1:
            add_stu()
        print("\n按回车键继续操作\n")
        if code == 4:
            name = input("请输入你想要查找的学生名字")
            print(find_stu_by_name(name))
        if code == 3:
            name = input("请输入你想要修改的学生名字")
            modify_stu(name)
        if code == 5:
            display_all_stu()
        if code == 2:
            name = input("请输入想要删除的学生name")
            delete_stu_by_name(name)
        if code == 6:
            print("已退出该系统")
            break


if __name__ == '__main__':
    run()
