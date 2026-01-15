from rest_framework import serializers
from account.models import User
from django.contrib.auth import authenticate
from account.utils.tokens import get_tokens_for_user,token_generator
from django.utils.encoding import smart_str,force_bytes,DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from account.utils.email import Email


class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(
        write_only=True,
        style={"input_type": "password"}
    )
    class Meta:
        model = User
        fields = ['email', 'name', 'password', 'password2', 'tc']
        extra_kwargs={
            'password':{'write_only':True}
        }
    
    def validate(self, attrs):
        password =attrs.get('password')
        password2= attrs.get('password2')
        if password != password2:
            raise serializers.ValidationError("Password & Confirm password doesn't match")
        return attrs
    
    def create(self, validated_data):
        validated_data.pop('password2')

        return User.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            tc=validated_data['tc'],
            password=validated_data['password']
        )
        
class UserLoginSerializer(serializers.Serializer):
    email= serializers.EmailField(max_length=255)
    password = serializers.CharField(
        write_only=True,
        style={'input_type': 'password'}
    )
    class Meta:
        model = User
        fields = ['email','password']
        
    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        user = authenticate(email=email, password=password)

        if not user:
            raise serializers.ValidationError("Invalid email or password")
        
        attrs['user'] = user
        attrs['token'] = get_tokens_for_user(user)
        return attrs
    
    
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields= ['id', 'name', 'email']
        
        
class UserChangePasswordSerializer(serializers.Serializer):
    
    old_password = serializers.CharField(max_length=255,
        write_only=True,
        style={'input_type': 'password'}
    )
    new_password = serializers.CharField(max_length=255,
        write_only=True,
        style={'input_type': 'password'}
    )
    new_password2 = serializers.CharField(
        max_length=255,
        write_only=True,
        style={'input_type': 'password'}
    )
    def validate(self, attrs):
        user = self.context.get('user')
        if not user.check_password(attrs.get('old_password')):
            raise serializers.ValidationError("Old password is incorrect")  
        if attrs['new_password'] != attrs['new_password2']:
            raise serializers.ValidationError("Passwords do not match")
      
        return attrs
    
    def save(self, **kwargs):
        user = self.context.get('user')
        user.set_password(self.validated_data.get('new_password'))
        user.save()
        return user
    
    
class SendPasswordResetEmailSerilaizer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)
    
    def validate(self, attrs):
        email = attrs.get('email')
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            uid = urlsafe_base64_encode(force_bytes(user.id)) 
            token = token_generator.make_token(user)
            link = f"http://localhost:3000/reset-password/{uid}/{token}/"

            # Send Email.
            body = f'Click Following Link to Reset Your Password\n {link}'
            data={
                'subject':'Reset your Password',
                'body':body,
                'to_email':user.email
            }
            Email.send_email(data)
            return attrs
        else:
            raise ValueError('No User found with this Email ')
        

class UserPasswordResetSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=255,
        write_only=True,
        style={'input_type': 'password'}
    )
    password2 = serializers.CharField(
        max_length=255,
        write_only=True,
        style={'input_type': 'password'}
    )
    class Meta:
        fields = ['password', 'password2']
    
    def validate(self, attrs):
        try:
            password =attrs.get('password')
            password2= attrs.get('password2')
            uid = self.context.get('uid')
            token = self.context.get('token')
            if password != password2:
                raise serializers.ValidationError("Password & Confirm password doesn't match")
            user_id = smart_str(urlsafe_base64_decode(uid))
            user = User.objects.get(id =user_id)
            if not token_generator.check_token(user,token):
                raise serializers.ValidationError("Token is invalid or expired")
            user.set_password(password)
            user.save()
        
            return attrs
        except DjangoUnicodeDecodeError :
            token_generator.check_token(user, token)
            raise serializers.ValidationError("Token is invalid or expired")