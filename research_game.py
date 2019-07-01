import random
import math

data = [['見','貝'],['土','士'],['眠','眼']]
level = 1
col=5#横
row=4#縦

def start_message():
    print('違う漢字の番号を入力してください') 

def section_message():
    print('レベル:'+str(level))#レベル１

datas = ''
def view_question():
    choice_data = random.randint(0,2)#0~2 どの文字にするか
    mistake_number = random.randint(0, (col * row) - 1 )#0~19   5*4
    print('mistake_number'+str(mistake_number)) #0

    data_in= data[choice_data]#data[0~2]
    print (data_in)#['見','貝']
    print('/| A B C D E')
    print('ーーーーー')
    i = 0
    j = 0
    while i < row:#0123
        datas = str(i+1)+'|'#1回目:1|   2回目:2| 3回目:3| 4回目:4|
        while j < col:#01234                                         
            if i*col+j == mistake_number:#012345678910111213141516171819
                datas+= data_in[1]#貝    #0回目:0=0*3+0  1回目:1=0*3+1 2回目:2=0*3+2  3回目:3=0*3+3  4回目:4=0*3+4 
                                         #0回目:5=1*3+0  1回目:6=1*3+1 2回目:7=1*3+2  3回目:8=1*3+3  4回目:9=1*3+4 
                                         #0回目:10=2*3+0  1回目:11=2*3+1 2回目:12=2*3+2 3回目:13=2*3+3 4回目:14=2*3+4
                                         #0回目:15=3*3+0 1回目:16=3*3+1 2回目:17=3*3+2 3回目:18=3*3+3 4回目:19=3*3+4

            else:
                datas += data_in[0]#見  
                                        
            j+=1
        print(datas)
        
        j=0#j初期化
        i+=1
    return mistake_number
def change_input_number(input_str): #例えば　C2
    str_data = {'A':0, 'B':1, 'C':2 }
    input_str_split = list(input_str)#['C','2']
    print (input_str_split)
    col_number = str_data[input_str_split[0]]# 2←col_number=str_data[C]     input_str_split[0]='C'で
    print (col_number)#2
    row_number = int(input_str_split[1])- 1   #１←row_number = int(2)- 1  行の１２３４を−１引く事で０１２３となる
    print(row_number)#１
    input_number = row_number*5+col_number    #7⇦input_number=1*5+2
    return input_number#7⇦C2が　　にchange!!!

def is_correct_number(input_number,mistake_number): #7,0
    if input_number == mistake_number:
        return True
    else:

        return False

def view_result(is_correct,mistake_number): #False  0
    if is_correct: 
        print('正解です！')
    else :
        # print(type(mistake_number))

        print('不正解です'+change_string(mistake_number)) #0

def change_string(number):
    number_data = ['A','B','C','D', 'E']
    col_number = number % 5 #    2⇦col_number=mistake_number7%5 もとに戻す　　0%5=0 1%5=1 2%5=2 3%5=3 4%5=4  ％の剰余0123
                                                                           #5%5=0 6%5=1 7%                        0123
                                                                                                               #  0123
                                                                                                               #  0123
    row_number = math.floor(number/5)+1#  2⇦row_number2=(7/5)+1             0/5=0 1/5=0 2/5=0 3/5=0 4/5=0     割る0000
                                                                        #   5%5=1 6/5=1 7/5=1 8/5=1 9/5=1         1111
                                                                                                            #     2222
                                                                                                            #     3333

    string=number_data[col_number]+str(row_number)  #C2
    return string


def play():
    section_message()
    mistake_number = view_question()#０←mistake_number 
    choice = input('例：A1→')#C2
    print('デバッグ：入力した文字 = '+str(choice))#C2
    input_number=change_input_number(choice)#    ５←input_number
    print('デバッグ：input_number = '+str(input_number))
    is_correct = is_correct_number(input_number,mistake_number)#False  ⇦5,0
    view_result(is_correct,mistake_number)  #False  0
    


start_message()
play()

