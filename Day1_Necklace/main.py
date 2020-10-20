# This code is a solution to the problem posed in the r/dailyprogrammer subreddit on Feb 9, 2012
# Link: https://www.reddit.com/r/dailyprogrammer/comments/ffxabb/20200309_challenge_383_easy_necklace_matching/
# The problem description is available in the README.txt file in the repo

def solve(string1, string2):
    ret = False
    for i in range(len(string1)):
        # Modify the first string (move the first letter to the end) and compare
        string1 = string1[1:] + string1[0]
        if string1 == string2:
            ret = True
            break
    return ret


if __name__ == '__main__':

    input_string1, input_string2 = input("Input the two strings:").split()
    solution = solve(input_string1, input_string2)
    print(solution)
