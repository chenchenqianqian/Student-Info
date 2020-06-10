
#此函数将输入的学生信息存入si.txt
from student_info import input_student

def write_to_text(lst,filename="si.txt"):
    '''将lst列表中的内容保存到si.txt'''
    try:
        f = open(filename,'a',encoding='utf-8')
        for name,age,score in lst:
            f.write(name)
            f.write('|')
            f.write(age)
            f.write('|')
            f.write(score)
            f.write('\n')
        f.close()
    except OSError:
        print("文件打开失败！")

