#此练习用类来描述一个学生的信息，要求该类的对象用于存储学生信息：姓名，年龄和成绩
#将这个写对象存于列表中，可以任意增添和删除学生信息
# 打印出学生的个数；打印出所有学生的平均成绩
class Student:
    count = 0

    def __init__(self, n, a, s=0):
        self.__name = n
        self.__age = a
        self.__score = s
        Student.count += 1 #让对象个数加1
    
   
    def __del__(self):
        Student.count -= 1 #对象销毁时count减去1
    
    def get_age(self):
        return self.__age

    def get_score(self):
        return self.__score
    
    def get_infos(self):
        return (self.__name, self.__age, self.__score)
    
    def is__name(self,n):
        '''判断n是否和self的名字先沟通'''
        return self.__name == n
    
    def set_score(self,score):
        '''此方法用于指定设置成绩时的规则'''
        if 0 <= score <=100:
            self.__score = score
            return
        raise ValueError('不合法的成绩信息'+str(score))
   
    def write_to_file(self,file):
        file.write(self.__name)        
        file.write(',')
        file.write(str(self.__age))
        file.write(',')
        file.write(str(self.__score))
        file.write('\n')        
    
    @classmethod
    def getTotalCount(cls):
        '''此方法用来得到学生对象的个数'''
        return cls.count

def test():
    L1 = []
    L1.append(Student('小张',20,100))
    L1.append(Student('小李',18,97))
    L1.append(Student('小王',19,98))
    print('此时学生对象的个数是：',
            Student.getTotalCount()) # 3
    
    L2 = []
    L2.append(Student('小赵',18,99))
    print(Student.getTotalCount()) # 4
    #删除一个学生
    L1.pop(1)
    print('此时学生个数为：', 
            Student.getTotalCount()) # 3
    
    all_student = L1 + L2
    scores = 0 # 用此变量记录所有学生的成绩总和
    for s in all_student:
        scores += s.get_score() # 累加所有学生的成绩
    
    print('平均成绩是：', scores/len(all_student)) # 99

if __name__=='__main__':
    test()




