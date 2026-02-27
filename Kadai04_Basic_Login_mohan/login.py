USERS = [
    {'id':'a', 'password':'aaa'},
    {'id':'b', 'password':'bbb'},
    {'id':'c', 'password':'ccc'},
    ]

class Login:
    def auth(self, id, password):
        for user in USERS:
            if user['id'] == id:
                if user['password'] == password:
                    return True
                break   # IDは一意のため、passwordが異なれば以後のループは不要。

        return False
