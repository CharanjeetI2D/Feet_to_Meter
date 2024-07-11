def inches_to_meters(feet, inches):
    total_inches = feet * 12 + inches
    meters = total_inches * 0.0254
    return meters


if __name__ == "__main__":
    feet_inch = input("Please enter feet and inches: ")
    split_feet_inch = feet_inch.split(" ")
    feet = int(split_feet_inch[0])
    inch = int(split_feet_inch[1])
    meters = inches_to_meters(feet=feet, inches=inch)
    print(meters)
