# fruit = ["Apple","Pear","Peach"]
# for fruit in fruit:
#     print(fruit)
#     print(fruit + " pie")

# student_score = [1,2,3,4,5,6,7,8,9,10]
# # total_student_score = sum(student_score) #sum() 합을 알려줌
# # print(total_student_score)

# # sum = 0
# # for score in student_score:
# #     sum += score   sum()함수 반복문으로 표현
# # print(sum)

# # max(student_score) #max() 최대값을 구해줌
# # max = 0
# # for score in student_score:
# #     if score > max: max()함수 반복문으로 표현
# #         max = score
# # print(max)
# sum = 0
# for i in range(1,10, 3): #1<= n <101
#     print(i)

#--------------------------------------------
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
password_create = [letters,numbers,symbols]
nr_letters = int(input("몇개의 글자를 사용하시겠습니까?\n"))
nr_symbols = int(input("몇개의 특수기호를 사용하시겠습니까?\n"))
nr_numbers = int(input("몇개의 숫자를 사용하시겠습니까?\n"))
 
password = []
for i in range(0, nr_letters):
    password += random.choice(letters)    
for i in range(0, nr_numbers):
    password += random.choice(numbers)    
for i in range(0, nr_symbols):
    password += random.choice(symbols)    
random.shuffle(password) #List 요소 무작위 섞음
password1 = ""
for i in password:
    password1 += i
print(password1)