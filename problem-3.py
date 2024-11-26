# Function using the map function

def celsius_to_fahrenheit(celsius):
    return list(map(lambda c: (c * 9/5) + 32, celsius))

temperatures_c = [0, 20, 30, 40]
temperatures_f = celsius_to_fahrenheit(temperatures_c)
print(temperatures_f)
