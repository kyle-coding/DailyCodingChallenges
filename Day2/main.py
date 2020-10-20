# This program serves as a solution-finder for the difficult challenges found on pythonchallenge.com
# where I left off: http://www.pythonchallenge.com/pc/def/equality.html

def challenge1(input_string):
    # solves the puzzle by iterating through the string and shifting the letters by 2
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    new_string = ""

    for i in range(len(input_string)):
        if input_string[i] != ' ' \
                and input_string[i] != '.' \
                and input_string[i] != "'" \
                and input_string[i] != '(' \
                and input_string[i] != ')':
            old_index = alphabet.index(input_string[i])
            new_index = old_index + 2
            if new_index > 25:
                new_index = new_index - 26
            new_string = new_string + alphabet[new_index]
        else:
            new_string = new_string + input_string[i]
    return new_string


def challenge2(input_string2):
    # find the unique characters in the string
    # find the occurances of each one
    # if they are rare (there is only one occurance), then output the letters

    character_set = set(input_string2)
    character_list = list(character_set)
    for i in range(len(character_list)):
        counter = input_string2.count(character_list[i])
        # print("Character: ", character_list[i], " Occurances: ", counter)
        if counter == 1:
            print(character_list[i])
    # the output gives us "iteqlayu", which can also spell "equality"


def challenge3(input_string3):
    answer = ''
    for i in range(4, len(input_string3)-4):
        if input_string3[i].islower():
            lower_string = input_string3[i-3:i]
            upper_string = input_string3[i+1:i+4]
            lower_limit = input_string3[i-4]
            upper_limit = input_string3[i+4]
            print(lower_string, upper_string, lower_limit, upper_limit)
            if lower_string.isupper() and upper_string.isupper() and lower_limit.islower() and upper_limit.islower():
                answer = answer + input_string3[i]
    print(answer)


if __name__ == '__main__':

    with open('testfile.txt', 'r') as file:
        string = file.read()

    challenge3(string)
