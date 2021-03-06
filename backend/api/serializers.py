from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(min_length=4)

    def create(self, validated_data):
        user = User.objects.create_user(username=validated_data['email'], email=validated_data['email'],
                                        password=validated_data['password'])
        user.staff = True
        user.admin = True
        return user

    class Meta:
        model = User
        fields = '__all__'
