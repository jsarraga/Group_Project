from orm import ORM



class Provider(ORM):
    tablename = 'providers'
    fields = ['hospital', 'doctor_name', 'department', 'username',
                'email', 'password_hash', 'token', 'api_key']

    def __init__(self, **kwargs):
        self.pk = kwargs.get('pk')
        self.hospital = kwargs.get('hospital')
        self.doctor_name = kwargs.get('doctor_name')
        self.department = kwargs.get('department')
        self.username = kwargs.get('username')
        self.email = kwargs.get('email')
        self.password_hash = kwargs.get('password_hash')
        self.token = kwargs.get('token')
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

     # TODO
    def get_patient( self, first_name, last_name,):
        pass

    # TODO
    def get_patient_file(self, token):
        pass