# from rest_framework import serializers
# from user.models import User
# from django.urls import reverse

# class UserHyperlinkedSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'url', 'username', 'email', 'is_staff', 'postname']
#         extra_kwargs = {
#             'url': {'view_name': 'post:postmodel-detail'},
#         }

# print(reverse('post_api:postmodel-detail'))