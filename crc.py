def crc(data, div, code):
    data = data + code
    print(data)
    data = list(data)
    div = list(div)

    for i in range(len(data)-len(code)):
        if data[i] == '1':
            for j in range(len(div)):
                data[i+j] = str((int(data[i+j])+int(div[j])) % 2)
    return ''.join(data[-len(code):])


data = input("Enter The Data: ")
div = input("Enter the Divisor: ")
code = "0" * (len(div)-1)

code = crc(data, div, code)
print("Code: ", code)
print("Sender Sends Message : ", data + code)

data = input(
    "Enter Message received by Receiver(change the bit to show error): ")
code = data[-len(code):]
data = data[:-len(code)]
rem = crc(data, div, code)

if int(rem) == 0:
    print("No Error", rem)
else:
    print("ERROR FOUND", rem)
