def convert_number(decimal):
 
    binary = bin(decimal)[2:]  
    
    octal = oct(decimal)[2:]  
    
    hexa = hex(decimal)[2:] 
    
    return binary, octal, hexa

def print_conversions(decimal):

    binary, octal, hexa = convert_number(decimal)
    print(f"\nnúmero decimal: {decimal}")
    print(f"binário: {binary}")
    print(f"octal: {octal}")
    print(f"hexadecimal: {hexa}")

numeros = [647, 543, 91]

for num in numeros:
    print_conversions(num) 

print("\n verificação (conversão de volta para decimal):")
for num in numeros:
    binary, octal, hexa = convert_number(num)
    print(f"\nNúmero original: {num}")
    print(f"Binário {binary} = {int(binary, 2)}")
    print(f"Octal {octal} = {int(octal, 8)}")
    print(f"Hexadecimal {hexa} = {int(hexa, 16)}")