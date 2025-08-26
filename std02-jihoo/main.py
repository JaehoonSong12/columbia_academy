"""

Usage (in Terminal): 
    python main.py
"""


# # hard-coding (literal)
# print(4+5)
# print(4*5)
# print(4/5)
# print("-------------------------------------------------")






# smart-coding (variable)
# computers need a space to store data. (assignment operator, only for computers, =)
x = 4          # x is a memory space
y = 5
z = 2000

print(x+y) # math algebra
print(x*y) # math algebra
print(x/y) # math algebra

# boolean algebra
print(x !=y) 

print(x + y == z) 

print("Hi jihoo")


# logical oeprator
# AND
a = 4
b = 6
c = -1
print((a < b) and (c > b))
# OR
print((a < b) or (c > b))
# NOT
print(not (2 == 3))

print("-------------------------------------------------")



user_input1 = int(input("Enter a number1: "))
user_input2 = int(input("Enter a number2: "))

print(user_input1 + user_input2== 29)



# print(3+5 == 8) # boolean algebra
# is 3+5 equal to 8? True


# 3+5=8

# 1 + 1 = 3

## 3 + 5 -> 8





# print(type(125))

# print(type(3.14))


# print(type("String is here!"))
# print(type(ord('a')))


# print("Hello World")




### HW 
#1 










# [High-Level Language] Human-Language:             English / Korean / Spanish 
# [High-Level Language] Programming Language:       Python / Java / C++ / Kotlin / ...

# Python Lagnuage System << software, to interpret Python human language to Machine Language
# `python --version` verifies if python language system is installed on your machine.

# [Low-Level Language] Native Language (Machine):   Binary (11101010000010101010)


### Example
# main.py
#   print("Hello World")         <----- programming language (Python)
#
# python main.py (main.py -> main.exe)
# 
# main.exe
#   001011111101010101010        <----- native language (Binary)


### Data Type
# 1 bit (binary) in Memory (RAM, Random-Access-Memory) / Storage (HDD, Hard-Disk-Drive / SSD, Solid-State-Drive)
#   - switch on: 전기신호를 연결! (방 불 키기)    <- 1
#   - switch off: 전기신호를 차단! (방 불 끄기)   <- 0
#      - CPU (Central Processing Unit) 가 bit data 들을 읽고 이해하고 행동합니다.

"""
Native Language (how CPU reads data)
- 옛날 컴퓨터, 1 byte (8 bit) 씩 읽었다.
- 요즘 신식 컴퓨터, 32-byte / 64-byte 씩 읽는다.

Binary: 

11101101 10110101 01101101 10110100 10101011 01101010 10101011 01101000

Decimal:

237      181      109      180      171      106      171      104      !!!!!!!!!!!!!!!!!!!!!!!


사람의 언어:

í        µ        m	       ´        «        j        «	       h









< Case 1: Number Data - 단순한 숫자 해석 >
Calculator: https://www.rapidtables.com/convert/number/binary-to-decimal.html

Binary  - Decimal
0       - 0 
1       - 1
10      - 2
11      - 3
100     - 4
101     - 5
110     - 6
111     - 7
1000    - 8
1001    - 9
1010    - 10

{Natural Number, Whole Number, Integer Number} = int (정수 숫자)

{Rational Number, Real Number} = float (소숫점 숫자)
e.g. 0.0001, 1/3, 3.14

*Special topic, how float data is processed.
IEEE-754 Floating Point Converter: https://www.h-schmidt.net/FloatConverter/IEEE754.html




< Case 2: Character Data - 사람이 쓰는 문자로 해석>
ASCII code - American Standard Code for Information Interchange
ASCII reference: https://www.ascii-code.com/



사람의 언어:

j        i         h         o         o

Decimal:

106     105      104        111       111


Binary: 

01101010 01101001  01101000  01101111   01101111






"""


# 1 byte = 
# 1. 'a', 'b', 'c' <- "Character (char / bytes) Data", char == 1 byte
# 2. 최지후 <- "String (str) Data"