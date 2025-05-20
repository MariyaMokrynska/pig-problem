import re


def pig_latin(sentence):
    words = sentence.split()
    result = []
    for word in words:
        new_word = ''
        # if word[0] != 'a' and word[0] != 'e' and word[0] != 'i' and word[0] != 'o' and word[0] != 'u':
        if re.match('[^aeiou]', word[0]):
            new_word = word[1:]
            new_word += word[0]
            new_word += 'ay'
        else:
            new_word = word
        result.append(new_word)
    return " ".join(result)


# Test cases
assert pig_latin("something") == "omethingsay"
assert pig_latin("awesome") == "awesome"
assert pig_latin(
    "latin is a hard language") == "atinlay is a ardhay anguagelay"
assert pig_latin("y") == "yay"
assert pig_latin("e") == "e"

print("All tests passed!")
print("Discuss time and space complexity if there's time remaining")
