str_manip = input("Enter a sentence or word: ")
length = len(str_manip)
print(length)

reverse_letters = (str_manip[:-4:-1])
print(reverse_letters)

five_letter_word = "{}{}".format (str_manip[0:3], str_manip[-2:])
print(five_letter_word)

new_string = str_manip.replace('k', '@')
print(new_string)
# The word used was'hickorydickorydock'