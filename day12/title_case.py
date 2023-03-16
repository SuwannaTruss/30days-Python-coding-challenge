'''
16-Mar-2023
Instruction:
https://www.codewars.com/kata/5202ef17a402dd033c000009
'''

def main():
    test_input = [
        ['a clash of KINGS', 'a an the of'],
        ['THE WIND IN THE WILLOWS', 'The In'],
        ['the quick brown fox', '']
    ]
    for i in range(len(test_input)):
        print(f'main text: {test_input[i][0]}, minor text: {test_input[i][1]}')
        print(f'result: {title_case(test_input[i][0], test_input[i][1])}')

def title_case(title, minor_words=''):
    list = title.lower().split(" ")
    minor_list = minor_words.lower().split(" ")
    for index, word in enumerate(list):
        if index > 0:
            list[index] = word.title() if word not in minor_list else word
        else:
            list[index] = word.title()
    return ' '.join(list)

if __name__ == "__main__":
    main() 