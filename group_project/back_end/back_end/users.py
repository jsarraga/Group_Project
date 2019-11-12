from orm import ORM
import random, string
from user_files import User_files
import util

ORM.dbpath = 'medical.db'

class User(ORM):
    tablename = 'users'
    fields = ['username', 'first_name', 'last_name', 'password_hash', 
            'email', 'security_question', 'token', 
            'api_key', 'provider_pk' ]

    def __init__(self, **kwargs):
        self.pk = kwargs.get('pk')
        self.username = kwargs.get('username')
        self.first_name = kwargs.get('first_name')
        self.last_name = kwargs.get('last_name')
        self.password_hash = kwargs.get('password_hash')
        self.email = kwargs.get('email')
        self.security_question = kwargs.get('security_question')
        self.token = kwargs.get('token')
        self.api_key = kwargs.get('api_key')
        self.provider_pk = kwargs.get('provider_pk')
    
    @classmethod
    def api_authenticate(cls, api_key):
        user = User.one_from_where_clause("WHERE api_key=?", 
                                                    (api_key,))
        if user is None:
            return None
        return user

    @classmethod
    def login(cls, username, password):
        return User.one_from_where_clause("WHERE username=? AND password_hash=?", 
                                                (username, hash_password(password)))

    def set_password(self, password):
        self.password_hash = hash_password(password)

    def get_all_user_files(self):
        return User_files.all_from_where_clause('WHERE user_pk=?',(self.pk,))
    
    def get_one_user_file(self, user_files_pk):
        return User_files.one_from_where_clause('WHERE pk=?', (user_files_pk,))

    def add_file(self, blood_type, allergies, medications, user_pk):
        user_file = User_files(blood_type=blood_type, alleriges=allergies, 
                                medications=medications, user_pk=self.pk)
        user_file.save()
        self.save()

    def remove_file(self, user_files_pk):
        user_file = User_files.one_from_where_clause('WHERE pk=?', (user_files_pk,))
        user_file.delete()
        user_file.save()
        

