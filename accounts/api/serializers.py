from django.contrib.auth import get_user_model
from django.db.models import Q
from rest_framework.serializers import (
    CharField,
    EmailField,
    ModelSerializer,
    ValidationError,
)

# from accounts.models import User

User = get_user_model()

class UserRegisterSerializer(ModelSerializer):
    email = EmailField(label = 'Email')
    email2 = EmailField(label = 'Confirm Email', write_only=True) #to confirm email
    password = CharField(style={'input-type' : 'password'}, label='Password', write_only=True, min_length=8)
    password2 = CharField(style={'input-type' : 'password'}, label='Confirm Password', write_only=True, min_length=8) #to confirm password
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'email2',
            'password',
            'password2',
        ]

    def validate(self, data):  # check if given email already exists
        email = data['email']
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise ValidationError("This email already exists, try again with a new email.")
        return data

    def validate_email(self, value):
        data = self.get_initial()
        email1 = data.get("email2")
        email2 = value
        if email1 != email2:
            raise ValidationError("Emails must match")
        return value

    def validate_email2(self, value):
        data = self.get_initial()
        email1 = data.get("email")
        email2 = value
        if email1 != email2:
            raise ValidationError("Emails must match")
        return value

    def validate_password(self, value):  #check if password matches confirm password
        data = self.get_initial()
        password1 = data.get("password2")
        password2 = value
        if password1 != password2:
            raise ValidationError("Passwords must match.")
        return value

    def validate_password2(self, value): #check if confirm password matches password
        data = self.get_initial()
        password1 = data.get("password")
        password2 = value
        if password1 != password2:
            raise ValidationError("Passwords must match.")
        return value

    def create(self, validated_data):
        username = validated_data["username"]
        email = validated_data["email"]
        password = validated_data["password"]
        user_obj = User(         #create user constructor with username and email
            username = username,
            email = email,
        )
        user_obj.set_password(password)  #set password
        user_obj.save()
        return validated_data

class UserLoginSerializer(ModelSerializer):
    username = CharField(required=False, allow_blank=True)  #not required field
    email = CharField(required=False, allow_blank=True, label="Email") #not required field
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password'
        ]
        extra_kwargs = {
            'password' : {'write_only' : True }
        }

    def validate(self, data):
        user_obj = None
        username = data.get("username", None)
        email = data.get("email", None)
        password = data["password"]
        if not email and not username:  #if email and username not provided
            raise ValidationError("Please provide email or password")
        user = User.objects.filter(    #searching the particular username or email
            Q(username=username) |
            Q(email=email)
        )
        user = user.exclude(email__isnull=True).exclude(email__iexact='')  #excluding users with no email
        if user.exists() and user.count() == 1:
            user_obj = user.first()     #if user exists set to user_obj
        else:
            raise ValidationError("username/email does not exist.")

        if user_obj:
            if not user_obj.check_password(password):  #check if password provide is correct
                raise ValidationError("Incorrect Password. Try again")

        return data
