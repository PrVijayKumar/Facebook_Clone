from rest_framework import serializers
from .models import User

def starts_with_s(value):
    if value[0].lower() != 's':
        breakpoint()
        raise serializers.ValidationError("Username should start with S")
    return value

class UserSerializer(serializers.ModelSerializer):
    
    def start_with_r(value):
        if value[0].lower() != 'r':
            raise serializers.ValidationError("Must start with r")
        return value
    
    # username = serializers.CharField(max_length=100, validators=[start_with_r])
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_staff']

    def validate_is_staff(self, value):
        if value:
            raise serializers.ValidationError('Cannot be a staff')
        return value
    
    def validate(self, data):
        username = data.get('username')
        email = data.get('email')

        if username.lower() == 'sonia' and email.lower() != 'congress@gmail.com':
            raise serializers.ValidationError("Cannot be other than congress")
        return data
    

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
