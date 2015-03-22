__author__ = 'u366472'
import get_tests
import os.path
import time
import json

# Gomez Authentication
username = ''
password = ''


def main():
    if not os.path.isfile('token.txt'):
        token = get_tests.get_token(username, password)
        print('no token! New Token requested ' + str(token))
    elif (time.time()-os.path.getmtime('token.txt')) > 7140:
        token = get_tests.get_token(username, password)
        print('Token old, new token requested ' + str(token))
    else:
        f = open('token.txt')
        token = f.read()
        f.close()

    print('token is good for another ' +
          str(120 - round(((time.time() - os.path.getmtime('token.txt'))/60), 0)) +
          ' minutes')

    if os.path.exists('test_monid.txt'):
        refresh = input('Would you like to refresh the test list? Y/N: \n').lower()
        if refresh == 'y':
            test_dict = get_tests.load_tests(token)
        elif refresh == 'n':
            f = open('test_monid.txt')
            test_dict = json.loads(f.read())
        else:
            print('Choose Y or N')
            time.sleep(1)
            main()
    else:
        test_dict = get_tests.load_tests(token)

    # for x, key in enumerate(sorted(test_dict)):
        # print(x, key, test_dict[key])
    numtest_dict = {}
    for x, key in enumerate(test_dict):
        numtest_dict[x] = [key, test_dict[key]]
        # print(x, key, test_dict[key])
    for i in numtest_dict:
        print(i, numtest_dict[i])
    print(numtest_dict[12][1])
if __name__ == main():
    main()

