def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5 )+32

def fahrenheit_a_celsius(fahrenheit):
    return(fahrenheit -32)*5/9

if __name__=="__main__":
 celsius = 25
 fahrenheit = celsius_a_fahrenheit(celsius)
 print(f"{celsius}grados celsius equivalen a {fahrenheit}grados fahrenheit")

 fahrenheit = 25
 celsius = fahrenheit_a_celsius(fahrenheit)
 print(f"{fahrenheit}grados fahrenheit equivalen a {celsius}grados celsius")