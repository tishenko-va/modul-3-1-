calls = 0
def count_calls():
    global calls
    calls += 1
    return calls

def string_info(string):
    count_calls()
    string_1 = [len(string), string.upper(), string.lower()]
    return string_1
def is_contains(string, list_to_search):
    count_calls()
    right = []
    for i in list_to_search:

        if string.lower() in i.lower():
            right = True
        else:
            right = False
    return right
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)


