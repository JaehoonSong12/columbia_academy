print("Hello World")


arr_example = [12,17,19,21,22,20,40,80,72]

print(len(arr_example))

print(range(len(arr_example))) # range(0,9) ,,,,,            0 <= integers < 9


print(arr_example)
# print(arr_example[0])
# print(arr_example[9])


for i in range(len(arr_example)):
    print(f"your index: {i}, and your value: {arr_example[i]}, and your previous term is {arr_example[i-1]}")
















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
# 1 bit (binary)
#   - switch on: 전기신호를 연결! (방 불 키기) <- 1
#   - switch off: 전기신호를 차단! (방 불 끄기) <- 0
# 1 byte = 
# 1. 'a', 'b', 'c' <- "Character (char / bytes) Data", char == 1 byte
# 2. 최지후 <- "String (str) Data"