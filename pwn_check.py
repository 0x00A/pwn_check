import requests
from time import sleep

def pwnd(email):

    results = {'breaches': 0, 'pastes': 0}
    hibp_url = "https://haveibeenpwned.com/api/%s"
    headers = \
    {"API-Version": "2",
    "User-Agent": "Python pwn check"}
    breach_type = \
    {"breaches": "breachedaccount/%s",
    "pastes": "pasteaccount/%s"}
    statement = \
    ["Currently checking ",
    " has been involved in the following data breach(es)",
    " has not been found in any ",
    "Failed due to status code ",]

    print (statement[0] + email)
    for b_type, b_type_url in breach_type.items():
        req = requests.get(hibp_url % b_type_url % email, headers=headers)
        s_code = req.status_code
        if req.ok and s_code == 200:
            res = (len(req.json())); print ("!!! " + email + statement[1] + " !!!")
            for x in range(res):
                print("+++ " + req.json()[x]['Title'] + " +++")
            if b_type == "breaches":
                results['breaches'] = res
            elif b_type == "pastes":
                results['pastes'] = res
        elif s_code == 404:
            print(email + statement[2] + b_type)
        else:
            print(statement[3] + s_code)
    sleep(2); print

    return results