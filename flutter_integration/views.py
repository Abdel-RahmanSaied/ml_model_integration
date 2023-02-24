from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from .serializers import ModelSerializer
import pickle
import numpy as np
# Create your views here.

class ModelViewSet(viewsets.ModelViewSet):
    serializer_class = ModelSerializer
    http_method_names = ['post']
    def create(self, request, *args, **kwargs):
        Pregnancies = int(request.data['Pregnancies'])
        Glucose = int(request.data['Glucose'])
        BloodPressure = int(request.data['BloodPressure'])
        SkinThickness = int(request.data['SkinThickness'])
        Insulin = int(request.data['Insulin'])
        BMI = float(request.data['BMI'])
        DiabetesPedigreeFunction = float(request.data['DiabetesPedigreeFunction'])
        Age = int(request.data['Age'])

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            input_data = np.array(
                [[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

            with open('ml model/diabetes_model.pkl', 'rb') as file:
                model = pickle.load(file)
            map = {0: 'No Diabetes', 1: 'Diabetes'}
            prediction = model.predict(input_data)
            prediction = map[prediction[0]]
            return Response({"detail":prediction}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
