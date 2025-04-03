from requests import get, post, delete

print(post('http://127.0.0.1:8080/api/v2/users', json={'name': 'Sonya', 'position': 'junior programmer',
                                                       'surname': 'Wolf', 'age': 17, 'address': 'module_3',
                                                       'speciality': 'computer sciences',
                                                       'hashed_password': 'wolf', 'email': 'wolf@mars.org'}).json())

print(get('http://127.0.0.1:8080/api/v2/users').json())
