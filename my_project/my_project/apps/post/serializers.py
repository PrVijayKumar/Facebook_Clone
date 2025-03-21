from rest_framework import serializers
from .models import PostModel
from django.utils import timezone
from user.serializers import UserSerializer

def post_starts_with_p(value):
    if value[0].lower() != 'p':
        raise serializers.ValidationError("Post must start with P")
    return value

class PostSerializer(serializers.ModelSerializer):
    # post_user = UserSerializer()
    def start_with_p(value):
        if value[0].lower() != 'p':
            raise serializers.ValidationError("Post title must start with p")
    # post_title = serializers.CharField(max_length=100, validators=[start_with_p])
    
    post_user_id = serializers.IntegerField()
    class Meta:
        model = PostModel
        fields = ['id', 'post_title', 'post_description', 'post_date', 'post_user_id']

    def validate_post_user_id(self, value):
        if value > 3:
            raise serializers.ValidationError('User must have id less than 3')
        return value
    
    def validate(self, data):
        pt = data.get('post_title')
        pd = data.get('post_description')

        if pt.lower() == 'india' and pd.lower() == 'illegal post':
            raise serializers.ValidationError('illegal post not allowed')
        return data

        
# class PostSerializer(serializers.Serializer):
#     post_title = serializers.CharField(max_length=100, validators=[post_starts_with_p])
#     post_description = serializers.CharField(max_length=100)
#     post_date = serializers.DateTimeField(default=timezone.now)
#     post_user_id = serializers.IntegerField()

#     def create(self, validated_data):
#         return PostModel.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.post_title = validated_data.get('post_title', instance.post_title)
#         instance.post_description = validated_data.get('post_description', instance.post_description)
#         instance.save()
#         return instance
    
#     def validate_post_user_id(self, value):
#         breakpoint()
#         if value > 3:
#             raise serializers.ValidationError('Not Allowed')
#         return value
    
#     def validate(self, data):
#         breakpoint()
#         pt = data.get('post_title')
#         pd = data.get('post_description')

#         if pt.lower() == 'india' and pd.lower() == 'illegal post':
#             raise serializers.ValidationError("Illegal Post Not allowed")
#         return data


class CreatePostSerializer(serializers.Serializer):
    post_title = serializers.CharField(max_length=100)
    post_description = serializers.CharField(max_length=100)
    post_date = serializers.DateTimeField(default=timezone.now)
    post_user_id = serializers.IntegerField(default=1)

    def create(self, valid_data):
        return PostModel.objects.create(**valid_data)