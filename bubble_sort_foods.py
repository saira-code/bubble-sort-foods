# Bubble Sort program
# This program sorts my favorite foods by the length of their names.

foods = ["Biriyani", "Mandi", "Sadhya", "Ice cream", "French Fries"]

# Bubble sort algorithm to sort the foods list by length
for i in range(len(foods)):
    for j in range(0, len(foods) - i - 1):
        # If the current food's name is longer than the next, swap them
        if len(foods[j]) > len(foods[j + 1]):
            foods[j], foods[j + 1] = foods[j + 1], foods[j]

print("Sorted foods by length:", foods)
