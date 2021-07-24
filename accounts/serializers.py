from rest_framework import serializers
from django.core.exceptions import ValidationError
from . import models 


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Account
        fields = ("email", "first_name", "last_name", "gender", "age", "password")
        extra_kwargs = {
            "password": {
                "write_only": True
            }
        }

    def save_validations(self, email):
        if "gmail.com" in email.split('@'):
            return True

        elif "outlook.com" in email.split("@"):
            return True 

        elif "icloud.com" in email.split("@"):
            return True 

        else:
            return False

    def create(self, validated_data):
        if self.save_validations(validated_data["email"]) == True:
            account = models.Account.objects.create(
                email=validated_data["email"],
                first_name=validated_data["first_name"],
                last_name=validated_data["last_name"],
                gender=validated_data["gender"],
                age=validated_data["age"]
            )

            account.set_password(validated_data["password"])
            account.save()

            return account 

        else:
            raise ValidationError("Invalid E-Mail Address provided...")