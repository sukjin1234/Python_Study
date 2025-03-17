import random

# randome_integer = random.randint(1, 10)
# print(randome_integer)  1 <= n <= 10 사이의 무작위 정수를 생성함

# random_number_0_to_1 = random.random()
# print(random_number_0_to_1)  0.0 <= n < 1.0 사이의 무작위 실수를 생성함

# random_float = random.uniform(1,10)
# print(random_float)   1.0 <= n <= 10 사이의 무작위 실수를 생성함
# count1 = 0
# count2 = 0
# for i in range(100):
#     dd = random.randint(1,2)
#     if dd == 1:
#         print("Heads")
#         count1 += 1
#     else:
#         print("Tails")
#         count2 += 1
        
# print(count1, count2 )

# state_of_korea = ["순천","서울","인천"]
# state_of_korea.append("부산") #append()는 List 끝에 단일 항목을 추가함
# state_of_korea.extend(["여수","광주"]) #extend()는 List 끝에 여러 항목을 추가함
# print(random.choice(state_of_korea)) #random.choice() 리스트 안에 내용을 무작위로 추출함
# #len() ()안에 있는 데이터의 길이를 알려줌
# print(len("안녕하세요"))
# state_of_japan = ["도쿄", "오사카"]
# state_state = [state_of_korea, state_of_japan]
# print(state_state) #중첩 리스트
computer_choice = random.randint(0,2)
your_choice = int(input("주먹 0, 보 1, 가위 2 "))
print(your_choice, computer_choice)
if (computer_choice == your_choice):
    print("비겼습니다")
elif(computer_choice == 0 and your_choice == 2) or (computer_choice == 1 and your_choice == 0) or (computer_choice == 2 and your_choice == 1):
    print("졌습니다")
else:
    print("이겼습니다") 