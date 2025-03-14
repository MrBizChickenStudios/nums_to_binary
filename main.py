def binary_converter(number):
    bit = [128,64,32,16,8,4,2,1]
    output = []
    for b in bit:
        if b > number:
            output.append(0)
        if number >= b:
            number -= b
            output.append(1)

    return output

for i in range(0, 256):

    print(binary_converter(i))
