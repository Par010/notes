from django.contrib.auth import get_user_model
from rest_framework.serializers import (
    CharField,
    EmailField,
    ModelSerializer,
    ValidationError,
)

User = get_user_model()

class UserRegisterSerializer(ModelSerializer):
    email = EmailField(label = 'Email')
    email2 = EmailField(label = 'Confirm email')
    password = CharField(style={'input-type' : 'password'}, label='Password')
    password2 = CharField(style={'input-type' : 'password'}, label='Confirm Password')
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'email2'
            'password',
            'password2',
        ]
        extra_kwargs = {
            'password' : {'write_only' : True},
            'password2' : {'write_only' : True},
        }

        def validate(self, data):
            email = data['email']
            qs = User.objects.filter(email=email)
            if qs.exists():
                raise ValidationError("This email already exists, try again with a new email.")
            return data

        def validate_email(self, value):
            data = self.get_initial()
            email1 = data.get("email")
            email2 = value
            if email1 != email2:
                raise ValidationError("Emails must match")
            return value

        def validate_email2(self, value):
            data = self.get_initial()
            email2 = data.get("email2")
            email1 = value
            if email1 != email2:
                raise ValidationError("Emails must match")
            return value

        def validate_password(self, value):
            data = self.get_initial()
            password1 = data.get("password")
            password2 = value
            if password1 != password2:
                raise ValidationError("Passwords must match.")
            return value

        def validate_password2(self, value):
            data = self.get_initial()
            password2 = data.get("password")
            password1 = value
            if password1 != password2:
                raise ValidationError("Passwords must match.")
            return value

        def create(self, validated_data):
            username = validated_data["username"]
            email = validated_data["email"]
            password = validated_data["password"]
            user_obj = User(
                username = username,
                email = email,
            )
            user_obj.set_password(password)
            user_obj.save()
            return validated_data
