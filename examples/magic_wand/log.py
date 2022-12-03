# ctrl c  停止
import serial
import re

ser = serial.Serial('COM6', 115200, timeout=6) # 串口  波特率

outFile = open(r'./output_negative_1.txt', 'w', encoding='utf-8')   # 本地目录 没有自动创建
ser.write("testing".encode())
try:
    while 1:

        line = ser.readline()   # 读取 
        line = line.decode('utf-8','ignore')
        st = str(line).replace("\r\n","")  # 列表转换字符串
        outFile.write(st+"\n")


except KeyboardInterrupt:
    ser.close()
    outFile.close()

