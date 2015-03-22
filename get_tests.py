__author__ = 'u366472'
import requests
import json
import os.path
import time

user = ''
password = ''

'''
# Proxy Connection #
http_proxy = 'http://u366472:Winter.2014@westproxy.wellsfargo.com:80'
proxyDict = {
    "http": "http://u366472:Winter.2014@westproxy.wellsfargo.com:80",
    "https": "https://u366472:Winter.2014@westproxy.wellsfargo.com:80"}
'''

def load_tests(token):
    # use token to get list of tests and write to file.
    test_dump = json.loads(get_tests(token))
    write_file('test_info.txt', test_dump)
    test_dict = {}
    for i in test_dump['Monitors']:
        test_dict[i['Monitor']['tname']] = i['Monitor']['monitorID']
    write_file('test_monid.txt', test_dict)
    return test_dict


def get_token(user, password):
    req_headers = {
        "Accept": "application/json",
        "Host": "datafeed-int1.compuwareapm.com",
        "Accept-Encoding": "gzip, deflate",
        "User-Agent": "Jakarta Commons-HttpClient/3.1"
    }
    end_point = 'https://datafeedeap1-api.compuwareapm.com/publicapi/rest/v1.0/login?'
    user_pass = 'user=' + user + '&password=' + password
    r = requests.request('get', end_point+user_pass, proxies=proxyDict, headers=req_headers)
    write_file('token.txt', r.text)
    return r.text


def get_tests(token):
        req_header = {
            "Authentication": "bearer " + str(token)
        }
        end_point = 'https://datafeedeap1-api.compuwareapm.com/publicapi/rest/v1.0/tests?'
        status = 'active'
        r = requests.request('get', end_point+'status='+status, proxies=proxyDict, headers=req_header)
        return r.text


def write_file(file_name, data2write):
    f = open(file_name, 'w')
    if type(data2write) == str:
        f.write(data2write)
    elif type(data2write) == dict:
        f.write(json.dumps(data2write, indent=1))
    f.close()
