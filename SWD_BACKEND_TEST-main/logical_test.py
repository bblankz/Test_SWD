
"""
Convert Number to Thai Text.
เขียนโปรแกรมรับค่าจาก user เพื่อแปลง input ของ user ที่เป็นตัวเลข เป็นตัวหนังสือภาษาไทย
โดยที่ค่าที่รับต้องมีค่ามากกว่าหรือเท่ากับ 0 และน้อยกว่า 10 ล้าน

*** อนุญาตให้ใช้แค่ตัวแปรพื้นฐาน, built-in methods ของตัวแปรและ function พื้นฐานของ Python เท่านั้น
ห้ามใช้ Library อื่น ๆ ที่ต้อง import ในการทำงาน(ยกเว้น ใช้เพื่อการ test การทำงานของฟังก์ชัน).

"""
thai_number = ("ศูนย์", "หนึ่ง", "สอง", "สาม", "สี่", "ห้า", "หก", "เจ็ด", "แปด", "เก้า")
unit = ("", "สิบ", "ร้อย", "พัน", "หมื่น", "แสน", "ล้าน")

def unit_process(val):
    length = len(val) > 1
    result = ''

    for index, current in enumerate(map(int, val)):
        if current:
            if index:
                result = unit[index] + result

            if length and current == 1 and index == 0:
                result += 'เอ็ด'
            elif index == 1 and current == 2:
                result = 'ยี่' + result
            elif index != 1 or current != 1:
                result = thai_number[current] + result

    return result

def thai_num2text(number):
    if number != 0:
        # print('In Function if')
        # print(number)
        s_number = str(number)[::-1]
        n_list = [s_number[i:i + 6].rstrip("0") for i in range(0, len(s_number), 6)]
        result = unit_process(n_list.pop(0))
        for i in n_list:
            result = unit_process(i) + 'ล้าน' + result
        return result
    else:
        # print('In Function else')
        # print(number)
        result = thai_number[0]
        return result

if __name__ == '__main__':
    print('\n')
    test = input("Please input Value:")
    Value_Data = int(test)
    #print(Value_Data)
    if Value_Data >= 0 and Value_Data < 10000000:
        #print(Value_Data)
        for test in range(1):
            #print(Value_Data)
            #print('\n')
            print(thai_num2text(Value_Data))
    else:
        print('Input : Must be greater than or equal to 0 and equal to 10 million.')