from django.test import TestCase
from .models import CustomUser
import pytest

   

def tests ():

    #models.py
    # Tests creating a user with valid email, username, password, and rol. 
    def test_create_user_valid(self):
        user = CustomUser.objects.create_user(
            email='test@example.com',
            username='testuser',
            password='testpassword',
            rol='testrol'
        )
        assert user.email == 'test@example.com'
        assert user.username == 'testuser'
        assert user.rol == 'testrol'

    # Tests updating a user's email, username, password, and rol. 
    def test_update_user(self):
        user = CustomUser.objects.create_user(
            email='test@example.com',
            username='testuser',
            password='testpassword',
            rol='testrol'
        )
        user.email = 'newemail@example.com'
        user.username = 'newusername'
        user.password = 'newpassword'
        user.rol = 'newrol'
        user.save()
        updated_user = CustomUser.objects.get(email='newemail@example.com')
        assert updated_user.username == 'newusername'
        assert updated_user.password == 'newpassword'
        assert updated_user.rol == 'newrol'

    # Tests creating a user with an email that already exists in the database. 
    def test_create_user_email_exists(self, mocker):
        mocker.patch('django.contrib.auth.models.UserManager._create_user', return_value=None)
        with pytest.raises(ValueError):
            CustomUser.objects.create_user(
                email='test@example.com',
                username='testuser',
                password='testpassword',
                rol='testrol'
            )

    # Tests creating a user with an invalid email format. 
    def test_create_user_invalid_email_format(self):
        with pytest.raises(ValueError):
            CustomUser.objects.create_user(
                email='invalidemail',
                username='testuser',
                password='testpassword',
                rol='testrol'
            )

    # Tests creating a user with a rol that exceeds the maximum length. 
    def test_create_user_rol_exceeds_max_length(self):
        with pytest.raises(ValueError):
            CustomUser.objects.create_user(
                email='test@example.com',
                username='testuser',
                password='testpassword',
                rol='a' * 51
            )

    # Tests creating a user without a rol. 
    def test_create_user_without_rol(self):
        user = CustomUser.objects.create_user(
            email='test@example.com',
            username='testuser',
            password='testpassword'
        )
        assert user.email == 'test@example.com'
        assert user.username == 'testuser'
        assert user.rol is None


    #views.py


    # Tests creating a user with valid email, username, password, and rol. 
    def test_create_user_valid(self):
        user = CustomUser.objects.create_user(email='test@example.com', username='testuser', password='testpassword', rol='testrol')
        assert user.email == 'test@example.com'
        assert user.username == 'testuser'
        assert user.check_password('testpassword')
        assert user.rol == 'testrol'

    # Tests authenticating a user with valid email and password. 
    def test_authenticate_user_valid(self):
        user = CustomUser.objects.create_user(email='test@example.com', username='testuser', password='testpassword', rol='testrol')
        authenticated_user = CustomUser.objects.authenticate(email='test@example.com', password='testpassword')
        assert authenticated_user == user

    # Tests creating a user with an email that already exists in the database. 
    def test_create_user_email_exists(self, mocker):
        mocker.patch('django.contrib.auth.models.UserManager._create_user', return_value=None)
        with pytest.raises(ValueError):
            CustomUser.objects.create_user(email='test@example.com', username='testuser', password='testpassword', rol='testrol')

    # Tests creating a user with an invalid email format. 
    def test_create_user_invalid_email_format(self):
        with pytest.raises(ValueError):
            CustomUser.objects.create_user(email='invalidemail', username='testuser', password='testpassword', rol='testrol')

    # Tests creating a user with a blank email, password, and username field. 
    def test_create_user_blank_fields(self):
        with pytest.raises(ValueError):
            CustomUser.objects.create_user(email='', username='', password='', rol='')

    # Tests creating a user with a rol that exceeds the maximum length. 
    def test_create_user_rol_max_length(self):
        with pytest.raises(ValueError):
            CustomUser.objects.create_user(email='test@example.com', username='testuser', password='testpassword', rol='a'*51)