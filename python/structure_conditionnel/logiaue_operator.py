# AND operator - both conditions must be True
x = 10
y = 20
if x > 5 and y > 15:
    print("Both conditions are True")

# OR operator - at least one condition must be True
age = 25
has_license = False
if age >= 18 or has_license:
    print("Can drive")

# NOT operator - inverts the boolean value
is_raining = True
if not is_raining:
    print("Go outside")
else:
    print("Stay inside")

# Complex combinations
temperature = 30
humidity = 60
if (temperature > 25 and humidity < 70) or temperature > 35:
    print("Hot conditions")