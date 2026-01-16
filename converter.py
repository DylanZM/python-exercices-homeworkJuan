# Convert Celsius to Fahrenheit
cel = float(input("Enter temperature in Celsius: "))
fahrenheit = (cel * 9/5) + 32
print(f"{cel}°C is equal to {fahrenheit}°F")

# Convert Fahrenheit to Celsius
fah = float(input("Enter temperature in Fahrenheit: "))
celsius = (fah - 32) * 5/9
print(f"{fah}°F is equal to {celsius}°C")