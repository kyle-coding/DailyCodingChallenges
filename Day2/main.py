# This program serves as a solution-finder for the difficult challenges found on pythonchallenge.com
# where I left off: http://www.pythonchallenge.com/pc/def/equality.html
# I think this is the solution for challenge 3: http://www.pythonchallenge.com/pc/def/linkedlist.html
import re
import urllib.request
import urllib.parse
import pickle


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
    for i in range(1, len(input_string3) - 7):
        if input_string3[i:i + 3].isupper():
            lower_string = input_string3[i:i + 3]
            middle_char = input_string3[i + 3]
            upper_string = input_string3[i + 4:i + 7]
            final_char = input_string3[i + 8]
            first_char = input_string3[i - 1]
            print(lower_string, upper_string, middle_char, final_char)
            if lower_string.isupper() \
                    and upper_string.isupper() \
                    and middle_char.islower() \
                    and final_char.islower() \
                    and first_char.islower():
                answer = answer + middle_char
    print("answer: ", answer)


def challenge3_attempt2(str_input):
    pattern = '[a-z][A-Z][A-Z][A-Z][a-z][A-Z][A-Z][A-Z][a-z]'
    answer = re.findall(pattern, str_input, re.MULTILINE)

    answer_string = ""

    for row in answer:
        answer_string = answer_string + row[4]
    print(answer_string)


def challenge4():
    # Solution: http://www.pythonchallenge.com/pc/def/peak.html
    base_url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php'
    values = {'nothing': '25357'}
    data = urllib.parse.urlencode(values)

    for i in range(1, 400):
        # we will iterate throught the urls, finding the next number and re-encoding our url
        response = urllib.request.urlopen(base_url + '?' + data)
        html = str(response.read())

        m = re.search('nothing is \d{3,10}', html)
        m2 = re.search('\d{3,10}', m.group())
        next_number = m2.group()
        print(i, next_number)
        values['nothing'] = next_number
        data = urllib.parse.urlencode(values)


def challenge5():
    # Solution: http://www.pythonchallenge.com/pc/def/channel.html
    # This challenge seems to require the use of "pickle" serialization

    page_data = urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/banner.p')

    decoded = pickle.load(page_data)
    # print(decoded)
    # It looks like a list of tuples which describe '#' characters that form something

    for i in range(0, len(decoded)):
        string = ''
        for row in range(0, len(decoded[i])):
            # iterate through the row, creating the string from each tuple of characters
            character, length = decoded[i][row]
            string = string + character * length
        print(string)


if __name__ == '__main__':
    # with open('challenge3.txt', 'r') as file:
    # string = file.read()

    challenge5()
