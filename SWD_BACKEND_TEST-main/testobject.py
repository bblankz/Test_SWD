#Python List
# HiLight Ctrl+/
# Data = [3,5,7,9,10]
# print(type(Data))
# print(sum(Data))
# print(sum(Data)/len(Data))


#Create Dict Data (Type : Str , Int , List )
#Key Name (Str) , ID(Str) , Score(Int) , Test(List)

# print(StuDict) # All Data Dict
# print(type(StuDict))
#
# print(StuDict['Name']) # Data of Specify Key
# print(type(StuDict['Name']))
#
# print(StuDict['Test'])
# print(type(StuDict['Test']))
#
# #Update Value of Specify Key
# StuDict['Score'] = 10
# print(StuDict)

# for Item in StuDict: # return Item is KeyName
# print(Item,StuDict[Item])
#
# for Item in StuDict.values(): #returm Item is Value
# print(Item)

# for KeyName , ItemValue in StuDict.items():
# print(KeyName,ItemValue)
#
# StuDict = {
# "Name":"Nut",
# "ID":"600001",
# "Score":8 ,
# "Test":[7,4,3,5]
# }
# if "name" in StuDict:
# print(StuDict['name'])
#
# if "Score" in StuDict:
# print(StuDict['Score'])

# WhatKey = input('What info do you want to know ?')
# if WhatKey in StuDict :
# print(WhatKey,':',StuDict[WhatKey])
# else :
# print('This key is not Exists!!!')

# Add New Key & Value
# StuDict["email"] = "limceprapan@gmail.com"
# print(StuDict)



# print(StuDict01)
# print(type(StuDict01))

# StuName = input('name :')
# StuDict01['name'] = StuName
# StuDict01 = {}
# StuDict01['name']= input('student name :')
# StuDict01['no'] = int(input('student no:'))
# StuDict01['email']= input('email address :')
# StuDict01['score1'] = int(input('score 1:'))
# StuDict01['score2'] = int(input('score 2:'))
# StuDict01['sum'] = StuDict01['score1'] + StuDict01['score2']
# print(StuDict01)
#
# Stu6003 = {
# "01" : StuDict01,
# "02" : StuDict01,
# }
# print(Stu6003)
#
# Stu6003 = {'01': {'name': 'Wachira', 'no': 8, 'email': 'limceprapan@gmail.com', 'score1': 4, 'score2': 7, 'sum': 11},
# '02': {'name': 'Wachira', 'no': 8, 'email': 'limceprapan@gmail.com', 'score1': 4, 'score2': 7, 'sum': 11}
# }
#

# {'6001': {'name': 'Wachira', 'score1': 4, 'score2': 5, 'score3': 7, 'sum': 16}, '6002': {'name': 'Teera', 'score1': 5, 'score2': 6, 'score3': 7, 'sum': 18}, '6003': {'name': 'Phuti', 'score1': 5, 'score2': 5, 'score3': 5, 'sum': 15}}

#V1
# Stu6003 = {}
# for StuInfo in range(1,4):
#     StuInfo = {}
#     StuID = input('Student ID:')
#     StuInfo['name'] = input('student name :')
#     StuInfo['score1'] = int(input('score 1:'))
#     StuInfo['score2'] = int(input('score 2:'))
#     StuInfo['score3'] = int(input('score 2:'))
#     StuInfo['sum'] = StuInfo['score1'] + StuInfo['score2'] + StuInfo['score3']

#     Stu6003[StuID] = StuInfo
# print(Stu6003)

#V2
# {'6001': {'name': 'Wachira', 'score': [3, 6, 7], 'sum': 16}, '6002': {'name': 'Teera', 'score': [6, 7, 8], 'sum': 21}, '6003': {'name': 'Phuntida', 'score': [8, 5, 4], 'sum': 17}}
# {'6001': {'name': 'Wachira', 'score': [3, 6, 7], 'sum': 16}, '6002': {'name': 'Teera', 'score': [6, 7, 8], 'sum': 21}, '6003': {'name': 'Phuntida', 'score': [8, 5, 4], 'sum': 17}}


# Stu6003 = {}
# for Stu in range(1,4):
# StuInfo = {}
# StuID = input('Student ID:')
# StuInfo['name'] = input('student name :')
#
# StuScoreList = []
# for i in range(1,4):
# Score = int(input('score:'))
# StuScoreList.append(Score)
#
# StuInfo['score'] = StuScoreList
# StuInfo['sum'] = sum(StuScoreList)
#
# if not StuID in Stu6003 :
# Stu6003[StuID] = StuInfo
# else :
# print('This Student id is Exits!!!')
#
# print(Stu6003)


# Stu6003 = {'6001': {'name': 'Wachira', 'score': [3, 6, 7], 'sum': 16}, '6002': {'name': 'Teera', 'score': [6, 7, 8], 'sum': 21}, '6003': {'name': 'Phuntida', 'score': [8, 5, 4], 'sum': 17}}
# print(Stu6003)
# print(type(Stu6003))

# print(Stu6003['6001'])
# print(Stu6003['6001']['name'])


# import math

# def BintoDec(StrBin):
#    DecVal = 0
#    for i in range(0, len(StrBin)):
#        NumVal = int(StrBin[i])
#        PowVal = math.pow(2, len(StrBin) - 1 - i)
#        DecVal += (PowVal * NumVal)
#    return(int(DecVal))

# StrBin =input("Please input 8 Bit :")
# print(BintoDec(StrBin))