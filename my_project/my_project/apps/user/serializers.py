from rest_framework import serializers
# from .models import User
from django.contrib.auth.models import User
from post.serializers import PostSerializer
import re

class UserSerializer(serializers.ModelSerializer):
    posts = PostSerializer(many=True, read_only=True, source='postname')
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_staff', 'first_name', 'last_name', 'posts', 'password']
        write_only_fields = ['is_staff', 'first_name', 'last_name']
        extra_kwargs = {
            'is_staff': {'write_only': True},
            'first_name': {'write_only': True},
            'last_name': {'write_only': True},
            'password': {'write_only': True},
        }

# accounts/serializers.py


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # breakpoint()
        if (validated_data['email'] != '') and (bool(re.search("^[a-zA-Z0-9_.±]+@[a-zA-Z0-9-]+.[a-zA-Z0-9-.]+$", validated_data['email']))):
            if ('first_name' in validated_data and 'last_name' in validated_data):
                user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'], first_name=validated_data['first_name'], last_name=validated_data['last_name'])
            else:
                user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
        else:
            raise serializers.ValidationError({"email": "Enter a valid email address"})
        return user




# def starts_with_s(value):
#     if value[0].lower() != 's':
#         breakpoint()
#         raise serializers.ValidationError("Username should start with S")
#     return value

# class UserSerializer(serializers.ModelSerializer):
    
#     def start_with_r(value):
#         if value[0].lower() != 'r':
#             raise serializers.ValidationError("Must start with r")
#         return value
    
#     # username = serializers.CharField(max_length=100, validators=[start_with_r])
    
#     postname = serializers.SlugRelatedField(many=True, read_only=True, slug_field='post_title')
#     # postname = serializers.HyperlinkedIdentityField(view_name='post-list')
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'email', 'is_staff', 'postname']

#     def validate_is_staff(self, value):
#         if value:
#             raise serializers.ValidationError('Cannot be a staff')
#         return value
    
#     def validate(self, data):
#         username = data.get('username')
#         email = data.get('email')

#         if username.lower() == 'sonia' and email.lower() != 'congress@gmail.com':
#             raise serializers.ValidationError("Cannot be other than congress")
#         return data
    

# class UserSerializer(serializers.Serializer):
#     username = serializers.CharField(max_length=100, validators=[starts_with_s])
#     email = serializers.EmailField()
#     is_staff = serializers.BooleanField()

#     def create(self, validated_data):
#         return User.objects.create(**validated_data)
    

#     def update(self, instance, validated_data):
#         print(instance.username)
#         instance.username = validated_data.get('username', instance.username)
#         print(instance.username)
#         instance.email = validated_data.get('email', instance.email)
#         instance.is_staff = validated_data.get('is_staff', instance.is_staff)
#         instance.save()
#         return instance
    
#     def validate_is_staff(self, value):
#         if value:
#             raise serializers.ValidationError('Cannot be a staff.')
#         return value
    
#     def validate(self, data):
#         un = data.get('username')
#         email = data.get('email')

#         if un.lower() == 'sonia' and email.lower() != 'congress@gmail.com':
#             raise serializers.ValidationError("only congress@gmail allowed")
#         return data


class CreateUserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    is_staff = serializers.BooleanField()

    def create(self, valid_data):
        return User.objects.create(**valid_data)
