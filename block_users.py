from TwitterAPI import TwitterAPI, TwitterRequestError, TwitterConnectionError

SCREEN_NAME = ''

try:
    api = TwitterAPI('<REDACTED>', '<REDACTED>', '<REDACTED>', '<REDACTED>', api_version='2')
    r = api.request(f'users/by/username/:{SCREEN_NAME}')

    userID = r.json()['data']['id']
    blockedUsers = list(set(user['screen_name'] for user in api.request(f'users/:{userID}/blocking', {'include_entities': 'false', 'skip_status':'true'})))

    if SCREEN_NAME in blockedUsers:
        print("User already blocked.")
    else:
        r = api.request('users/:<REDACTED>/blocking', params={'target_user_id': userID}, method_override='POST')
        for item in r:
            print(item)

except TwitterRequestError as e:
    print(e.status_code)
    for msg in iter(e):
    	print(msg)

except TwitterConnectionError as e:
	print(e)

except Exception as e:
	print(e)
