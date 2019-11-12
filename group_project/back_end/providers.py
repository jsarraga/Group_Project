from orm import ORM



class Provider(ORM):
    tablename = 'accounts'
    fields = ['username', 'password_hash', 'balance', 'api_key']

    def __init__(self, **kwargs):
        self.pk = kwargs.get('pk')
        self.username = kwargs.get('username')
        self.password_hash = kwargs.get('password_hash')
        self.balance = kwargs.get('balance')
        self.pk = kwargs.get('pk')
        self.api_key = kwargs.get('api_key')
    
    @classmethod
    def api_authenticate(cls, api_key):
        account = Account.one_from_where_clause("WHERE api_key=?", 
                                                    (api_key,))
        if account is None:
            return None
        return account

    @classmethod
    def login(cls, username, password):
        return Provider.one_from_where_clause("WHERE username=? AND password_hash=?", 
                                                (username, hash_password(password)))

    def set_password(self, password):
        self.password_hash = hash_password(password)

