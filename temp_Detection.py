import openPort

file = open("test.txt", "w+")
data = openPort.ser.read(size=12)
data = data.decode("utf-8")
data1= data[0:6]
data2 = data[6:13]
print(data1)
print(data2)

