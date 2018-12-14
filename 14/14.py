puzzle_input = 554401
puzzle_digits = [int(digit) for digit in str(puzzle_input)]

recipes = [3, 7]
first_elf = 0
second_elf = 1

# for part 1 only:
# while len(recipes) <= (puzzle_input + 10):
# for both parts:
while recipes[-len(puzzle_digits):] != puzzle_digits and recipes[-len(puzzle_digits) - 1:-1] != puzzle_digits:
    sum_recipes = recipes[first_elf] + recipes[second_elf]
    recipes.extend(divmod(sum_recipes, 10) if sum_recipes >= 10 else [sum_recipes])
    first_elf = (first_elf + 1 + recipes[first_elf]) % len(recipes)
    second_elf = (second_elf + 1 + recipes[second_elf]) % len(recipes)

print("part 1: " + ''.join(str(c) for c in recipes[puzzle_input:puzzle_input + 10]))

recipes_string = ''.join(str(c) for c in recipes)
puzzle_string = str(puzzle_input)
print(f'part 2: {recipes_string.index(puzzle_string)}')
