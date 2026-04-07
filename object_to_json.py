import json
# AI used here to finish
class User:
    username = 'user'
    email = 'something@mail.com'

def create_new_user(data):
    if isinstance(data, str):
        try:
            data = json.loads(data)
        except json.JSONDecodeError:
            return User()
    user = User()
    if isinstance(data, dict):
        user.username = data.get('username', User.username)
        user.email = data.get('email', User.email)
    return user

def user_to_json(user):
    user_dict = {}
    if hasattr(user, 'username') and user.username != User.username:
        user_dict['username'] = user.username
    if hasattr(user, 'email') and user.email != User.email:
        user_dict['email'] = user.email
    
    return json.dumps(user_dict)
