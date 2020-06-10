from menu import show_menu
from student_info import *
from student import Student

#定义主函数，用来获取键盘操作，实现选择功能
def main():
    docs = [] # 此列表用来存储所有学生的信息的字典
    while True:
        show_menu()
        s = input('请选择：')
        if s == '1':
            docs += input_student()
        elif s == '2':
            output_student(docs)
        elif s == '3':
            modify_student_info(docs)
        elif s == '4':
            delete_student_info(docs)
        elif s == '5':
            score_desc(docs)
        elif s == '6':
            score_asc(docs)
        elif s == '7':
            age_desc(docs)
        elif s == '8':
            age_asc(docs)
        elif s == '9':
            save_to_file(docs)
        elif s == '10':
            docs = read_from_file()
        elif s == 'q':
            return  #结束此函数执行，直接退出

main()
