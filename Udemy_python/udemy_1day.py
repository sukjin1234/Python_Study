#print함수와 input함수를 배움

print(len(input())) #len() : () 안에 있는 값의 길이를 알려줌

two_digit_number = input() #32를 입력
first_digit_number = two_digit_number[0]
second_digit_number = two_digit_number[1]
print(first_digit_number) #입력 받은 string 값을 배열을 통해
print(second_digit_number) #나누어 저장할 수 있음
#input() 으로 저장한 변수는 type이 string임
a = ""
a += a #문자열에 문자 덧셈가능 이때 +는 덧셈이 아니라 연결연산자