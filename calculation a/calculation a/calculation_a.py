import sys
sys.stdout = open('calculation.txt','a')
def start():

  while True:

    print("종료하려면 e, 재시작 하시려면 c를 입력해주세요.")

    get_ = input("계산식을 입력해주세요>>>")

    if get_ == 'c':
        continue

    elif get_ == 'e':
        break


    if '+' in get_:
        get_num1, get_num2 = get_.split("+")
        get_math = '+'
            
    elif '-' in get_:
        get_num1, get_num2 = get_.split('-')
        get_math = '-'
        
    elif '*' in get_:
        get_num1, get_num2 = get_.split("*")
        get_math = '*'
        
    elif '/' in get_:
        get_num1, get_num2 = get_.split("/")
        get_math = '/'
        
    else:
        print("잘못된 입력입니다. 올바른 연산자를 입력해주세요.")
        continue


    

    get_num1 = get_num1.strip()
    get_num2 = get_num2.strip()
    
    if not get_num1.isdigit() or not get_num2.isdigit():
        print("잘못된 입력입니다. 숫자를 입력해주세요.")
        continue

   

    if get_math == '+':
     print ("결과값은 ", int(get_num1) + int(get_num2), "입니다.\n")

    elif get_math == '-':
         print ("결과값은 ", int(get_num1) - int(get_num2), "입니다.\n")

    elif get_math == '*':
      print ("결과값은 ", int(get_num1) * int(get_num2), "입니다.\n")

    elif get_math == '/':
        print ("결과값은 ", int(get_num1) / int(get_num2), "입니다.\n")


print ("시작")
start()
print ("끝")      
