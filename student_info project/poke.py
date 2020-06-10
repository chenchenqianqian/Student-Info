#斗地主模拟发牌
def get_poke():
    '''生成一副扑克'''
    kinds = ['\u2660','\u2663','\u2665','\u2666']
    number = ['A'] + list(map(str,range(2,11))) + list('JQK')
    L = ['JokerA','JokeB'] + [x + y for x in kinds for y in number]
    return L

import random
def poke_games():
    pk = get_poke()
    random.shuffle(pk)
    input("输入回车继续")
    print('第一个人的17张牌是：',pk[:17])
    input("输入回车继续")
    print('第二个人的17张牌是：',pk[17:34])
    input("输入回车继续")
    print('第三个人的17张牌是：',pk[34:51])
    input("输入回车继续")
    print('底牌是：',pk[51:])

poke_games()
