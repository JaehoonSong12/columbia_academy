######################  CODE SEGMENT
class Student: # <- class
    # field
    def __init__(self, studentName, studentAge):
        self.studentName = studentName
        self.studentAge = studentAge
    
    def getStudentName(self):
        return self.studentName
    
    def setStudentName(self, studentName):
        self.studentName = studentName
    
    def __repr__(self):
        return f"[name:{self.studentName},age:{self.studentAge}]"

class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __repr__(self):
        return f"{self.real} + i {self.imaginary}"
    
    def __add__(self, other):
        if isinstance(other, ComplexNumber): 
            return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)
        else: 
            raise TypeError("Unsupported operand type(s) for +")
    
    def __mul__(self, other):
        if isinstance(other, ComplexNumber): 
            return ComplexNumber(self.real * other.real - self.imaginary * other.imaginary, self.real * other.imaginary + other.real * self.imaginary)
        else: 
            raise TypeError("Unsupported operand type(s) for +")

def main():
    std = Student("Jihoo", 14)
    name = std.getStudentName()
    print(std)

    
    number = ComplexNumber(3, 4) * ComplexNumber(-1, 8)
    print(number)

#######################
# Student (self.studentName, self.studentAge) <- object (0x00000244FCD57D40)
# 
# 
# ---- heap --------
# 
# 
# ---- stack --------
# 
# __init__(self, studentName, studentAge)
# main()
# python main.py
########################



if (__name__ == "__main__"):
    main()