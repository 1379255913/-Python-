# 对字符串加密成整数
import datetime
import random


def encrypt(srcStr, password='1938762450'):
    # 将字符串转换成字节数组
    data = bytearray(srcStr.encode('utf-8'))
    # 把每个字节转换成数字字符串
    strList = [str(byte) for byte in data]
    # 给每个数字字符串前面加一个长度位
    strList = [str(len(s)) + s for s in strList]
    # 进行数字替换
    for index0 in range(len(strList)):
        tempStr = ""
        for index in range(len(strList[index0])):
            tempStr += password[int(strList[index0][index])]
        strList[index0] = tempStr
    return "".join(strList)

# 把整数解密成字符串
def decrypt(srcStr, password='1938762450'):
    # 数字替换还原
    tempStr = ""
    for index in range(len(srcStr)):
        tempStr += str(password.find(srcStr[index]))
    # 去掉长度位，还原成字典
    index = 0
    strList = []
    while True:
        # 取长度位
        length = int(tempStr[index])
        # 取数字字符串
        s = tempStr[index + 1:index + 1 + length]
        # 加入到列表中
        strList.append(s)
        # 增加偏移量
        index += 1 + length
        # 退出条件
        if index >= len(tempStr):
            break
    data = bytearray(len(strList))
    for i in range(len(data)):
        data[i] = int(strList[i])
    return data.decode('utf-8')


def create_uuid():  # 生成唯一的图片的名称字符串，防止图片显示时的重名问题
    nowTime = datetime.datetime.now().strftime("%Y%m%d%H%M%S")  # 生成当前时间
    randomNum = random.randint(0, 100)  # 生成的随机整数n，其中0<=n<=100
    if randomNum <= 10:
        randomNum = str(0) + str(randomNum)
    uniqueNum = str(nowTime) + str(randomNum)
    return uniqueNum