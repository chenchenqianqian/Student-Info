#写一个函数input_student()得到学生的姓名，年龄，年龄
# 输入一些学生信息；按照年龄从大到小排列，并输出
# 按照成绩从高到低排序后，并输出
#第一步，读取学生信息，形成字典后存入列表L中
from student import Student

def input_student():
    L = []
    while True:
        name = input('请输入学生姓名：')
        if not name:
            break
        age = int(input('请输入学生年龄：'))
        score = int(input('请输入学生成绩：'))
        d =Student(name,age,score)
        # d['name']=name
        # d['age']=age
        # d['score']=score
        L.append(d)
    return L

def output_student(L):
    print('+'+'-'*12+'+'+'-'*6+'+'+'-'*7+'+')
    print('|'+str('name').center(12)+'|'+str('age').center(6)+'|'+str('score').center(7)+'|')
    print('+'+'-'*12+'+'+'-'*6+'+'+'-'*7+'+')
    for d in L:
        n, a, s = d.get_infos()
        t = (n.center(12),
            str (a).center(6),
            str (s).center(7))
        line = '|%s|%s|%s|'% t
        print(line)
    print('+'+'-'*12+'+'+'-'*6+'+'+'-'*7+'+')

#此函数用来打印菜单
# def show_menu():
#     print('+------------+------+----------------------+')
#     print('|  1) 添加学生信息                         |')
#     print('|  2) 查看所有学生信息                     |')
#     print('|  3) 修改学生的成绩                       |')
#     print('|  4) 删除学生信息                         |')
#     print('|  5) 按成绩从高到低打印学生信息           |')
#     print('|  6) 按成绩从低到高打印学生信息           |')
#     print('|  7) 按年龄从高到低打印学生信息           |')
#     print('|  8) 按年龄从低到高打印学生信息           |')
#     print('|  q) 退出                                 |')
#     print('+------------+------+----------------------+')




#此函数修改学生的信息
def modify_student_info(lst):
    name = input('请输入要修改学生的姓名：')
    for d in lst:
        if d.is_name(name):
            score = int(input('请输入新成绩：'))
            d.set_score(score)
            print('修改',name,'的成绩为',score)
            return
    else:
        print('没有找到名为：',name,'的学生信息')

#此函数删除学生信息
def delete_student_info(lst):
    name = input('请输入要删除学生的姓名：')
    for i in range(len(lst)):
        if lst[i].is_name(name):
            del lst[i]
            print('已成功删除：', name)
            return
    else:
        print('没有找到名为：',name,'的学生信息')



#此函数年龄降序排列
def age_desc(lst):
    L = sorted(lst,
                key= lambda d: d.get_age(),
                reverse = True)
    output_student(L)

#此函数年龄升序排列
def age_asc(lst):
    L = sorted(lst,
               key= lambda d: d.get_age())
    output_student(L)

#此函数年龄降序排列
def score_desc(lst):
    L = sorted(lst,
              key= lambda d: d.get_score(), 
              reverse = True)
    output_student(L)

#此案函数年龄升序排列
def score_asc(lst):
    L = sorted(lst,
              key= lambda d: d.get_score())
    output_student(L)

def save_to_file(docs, filename='si.txt'):
    try:
        f = open(filename,'w')
        for stu in docs:
            stu.write_to_file(f)
        f.close()
        print('保存文件成功')
    except OSError:
        print('保存失败')

def read_from_file(filename='si.txt'):
    L = []
    try:
        f = open(filename)
        for line in f:
            s = line.rstrip() # 去掉右侧‘\n’
            lst = s.split(',')
            name,age,score = lst
            age = int(age)
            score = int(score)
            L.append(Student(name,age,score))
        f.close()
    except OSError:
        print('文件打开失败')
    return L

#定义主函数，用来获取键盘操作，实现选择功能
# def main():
#     docs = [] # 此列表用来存储所有学生的信息的字典
#     while True:
#         show_menu()
#         s = input('请选择：')
#         if s == '1':
#             docs += input_student()
#         elif s == '2':
#             output_student(docs)
#         elif s == '3':
#             modify_student_info(docs)
#         elif s == '4':
#             delete_student_info(docs)
#         elif s == '5':
#             score_desc(docs)
#         elif s == '6':
#             score_asc(docs)
#         elif s == '7':
#             age_desc(docs)
#         elif s == '8':
#             age_asc(docs)
#         elif s == 'q':
#             return  #结束此函数执行，直接退出

# main()
