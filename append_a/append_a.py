#######################################
# Name: Charith Kumarasinghe
# Discode id: CHKUMARASINGH#1583
# Practice assignment 2
#######################################



# - Create an array variable named `animals`
#   with the following content:
#   `["koal", "pand", "zebr", "anacond", "bo", "chinchill", "cobr",
#     "gorill", "hyen", "hydr", "iguan", "impal", "pum", "tarantul", "piranh"]`
#
# - Add an `"a"` at the end of all elements (use a loop!)
# - Print the 'fixed' array to the console:
#   [koala, panda, zebra, anaconda, boa, ..., puma, tarantula, piranha]


####### Solution #######


# Initiating the array(list) with given values.
animals = ["koal", "pand", "zebr", "anacond", "bo", "chinchill", "cobr", 
           "gorill", "hyen", "hydr", "iguan", "impal", "pum", "tarantul", "piranh"]

# # Iterating "animal" list. 
# for array_index in range(len(animals)):
#     # Appending "a" to each element as ex:animals[0]= "kola" + "a".
#     animals[array_index] += "a"

# # Print updated array.
# print(animals)

# Iterating "animal" list.
new_animals = []
for animal in animals:
    # Appending "a" to each element as ex:animals[0]= "kola" + "a".
    new_animal = animal + "a"
    new_animals.append(new_animal)
    print(animal)

# Print updated array.
# print(animals)




