import requests

def registration(account_details):
    registration_endpoint = 'http://127.0.0.1:8000/auth/users/'
    response = requests.post(registration_endpoint, account_details)
    print(response)


def login(login_credentials):
    login_endpoint = 'http://127.0.0.1:8000/auth/token/login/'
    response = requests.post(login_endpoint, login_credentials)
    status_code = response.status_code
    print(f"Status code: {status_code}")
    
    if status_code == 200:
        auth_token = response.json()['auth_token']
        print("Auth token: ", auth_token)
        return auth_token
    

def client(auth_token, endpoint):
    token_h = f"Token {auth_token}"
    headers = {'Authorization': token_h}
    response = requests.get(endpoint, headers=headers)
    status_code = response.status_code
    print(f"Status code: {status_code}")
    
    if status_code == 200:
        response_data = response.json()
        return response_data
    
if __name__ == '__main__':
    account_details = {'username': 'neo-user', 'email': 'neo-user@email.com', 'password': 'strong-password', 're-password': 'strong-password'}
    registration(account_details)
    # login_credentials = {'username': 'admin', 'password': 'admin'}
    # auth_token = login(login_credentials)
    
    # data_endpoint = 'http://127.0.0.1:8000/api/profiles/'
    # client_data = client(auth_token, data_endpoint)
    # print(client_data)