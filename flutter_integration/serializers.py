from rest_framework import serializers, fields
from rest_framework.response import Response

class ModelSerializer(serializers.Serializer):
    class Meta:
        Pregnancies = serializers.IntegerField(required=True)
        Glucose = serializers.IntegerField(required=True)
        BloodPressure = serializers.IntegerField(required=True)
        SkinThickness = serializers.IntegerField(required=True)
        Insulin = serializers.IntegerField(required=True)
        BMI = serializers.FloatField(required=True)
        DiabetesPedigreeFunction = serializers.FloatField(required=True)
        Age = serializers.IntegerField(required=True)
