from rest_framework import serializers
from datetime import date
from . import models
from rest_framework import status
from rest_framework.response import Response


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserDetail
        dateOfBirth = serializers.DateField()
        fields = ('user_name', 'dateOfBirth')

    def validate(self, dateOfBirth):
        if dateOfBirth['dateOfBirth'] >= date.today():
            raise serializers.ValidationError("YYYY-MM-DD must be date before today date!")
        return dateOfBirth
