
"""
Convert Arabic Number to Roman Number.
เขียนโปรแกรมรับค่าจาก user เพื่อแปลง input ของ user ที่เป็นตัวเลขอราบิก เป็นตัวเลขโรมัน
โดยที่ค่าที่รับต้องมีค่ามากกว่า 0 จนถึง 1000

*** อนุญาตให้ใช้แค่ตัวแปรพื้นฐาน, built-in methods ของตัวแปรและ function พื้นฐานของ Python เท่านั้น
ห้ามใช้ Library อื่น ๆ ที่ต้อง import ในการทำงาน(ยกเว้น ใช้เพื่อการ test การทำงานของฟังก์ชัน).

"""
def printRoman(number):
    num = [1, 4, 5, 9, 10, 40, 50, 90,
        100, 400, 500, 900, 1000]
    sym = ["I", "IV", "V", "IX", "X", "XL",
        "L", "XC", "C", "CD", "D", "CM", "M"]
    i = 12
      
    while number:
        div = number // num[i]
        number %= num[i]
  
        while div:
            print(sym[i], end = "")
            div -= 1
        i -= 1
  
# Driver code
if __name__ == "__main__":
    print('\n')
    test = input("Please input Value:")
    Value_Data = int(test)
    if Value_Data > 0 and Value_Data <= 1000:
        #print(Value_Data)
        print("Roman value is:", end = " ")
        printRoman(Value_Data)
    else:
        print('Input : Must be greater than 0 until 1000.')
