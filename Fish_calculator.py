# Function to calculate the weight of the fish
def calculate_weight(length, girth):
    weight = (girth * girth * length) / 800
    return round(weight, 2)

# Function to guess the class of the fish based on its weight
def guess_class(weight):
    if weight == 0:
        return "No Fish"
    elif weight <= 41:
        return "Small Fish"
    elif weight <= 99:
        return "Medium Fish"
    elif weight <= 174:
        return "Big Fish"
    else:
        return "Giant Fish"

# Lists to store fish names and their weights
fish_list = []
weight_list = []

#For Loop to get inputs for two fish
for i in range(2):
    # Tell user to enter fish name, length, and girth
    fish_name = input(f"Enter the name of Fish {i+1}: ")
    length = float(input(f"Enter the length (in inches) of Fish {fish_name}: "))
    girth = float(input(f"Enter the girth (in inches) of Fish {fish_name}: "))

    # Calculate weight and determine class
    weight = calculate_weight(length, girth)
    fish_class = guess_class(weight)

    # Store the fish name and its weight
    fish_list.append(fish_name)
    weight_list.append(weight)

    # Display the result
    print(f"\nFish: {fish_name}")
    print(f"Weight: {weight} pounds")
    print(f"Class: {fish_class}\n")

# While loop to display the fish classes
index = 0
while index < len(fish_list):
    print(f"Fish: {fish_list[index]}")
    print(f"Weight: {weight_list[index]} pounds")
    print(f"Class: {guess_class(weight_list[index])}\n")
    index += 1

# Output the final lists answer
print("Final Fish List:", fish_list)
print("Final Weight List:", weight_list)
