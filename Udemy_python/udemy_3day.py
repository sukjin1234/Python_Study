# Example = "kakaka"
# Example = Ex.count("k")
# print(Example) -> 3
# 변수.count() ()안에 있는 문자나 숫자 변수 안에 얼마나 있는지 알려줌
# 변수.lower() 변수에 들어있는 문자열을 모두 소문자로 바꿈 


print('''
                           ______
        |\_______________ (_____\\______________
HH======#H###############H#######################
        ' ~""""""""""""""`##(_))#H\"""""Y########
                          ))    \#H\       `"Y###
                          //     }#H)''')
print(''' ___________ ____________  
|           )._______.-'
`----------'    ''')
print('''  |`-._/\_.-`|
  |    ||    |
  |___o()o___|
  |__((<>))__|
  \   o\/o   /
   \   ||   /
    \  ||  /
     '.||.'
       ``''')

print("좀비들이 다가오고 있습니다.\n당신 앞에는 세 개의 무기가 있습니다.")
first_answer = input("총, 칼, 방패 중에 하나를 고르세요. :")
if first_answer == "총":
    print("\n총으로 좀비들을 죽이고 간신히 도망쳤습니다.")
    print("앞에 사람이 보인다.")
    second_answer = input("총으로 쏜다 y or n :")
    if second_answer == "y":
        print("\n다행이도 그 사람은 좀비였습니다.")
        print("앞에 차가 두 대 보인다.")
        print("왼쪽 차를 탈지 오른쪽 차를 탈지 고르세요")
        third_answer = input("left or right : ")
        if third_answer == "left":
            print("\n고르신 차는 고장난 차였습니다.")
            print("좀비들에게 둘러쌓여 죽었습니다.")
            print("game over")
        else:
            print("\n고르신 차는 정상인 자동차였습니다.")
            print("차를 타고 좀비가 전염된 도시를 탈출하였습니다.")
            print("winner")
    else:
        print("\n사람처럼 보이는 좀비였습니다.")
        print("game over")
else:
    print("\n고르신 무기로는 많은 좀비들을 상대할 수 없습니다.")
    print("좀비에게 물려 사망")
    print("game over")