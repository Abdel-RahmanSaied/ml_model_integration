
# ML Model Integration in django restframework APIs

This project demonstrates how to integrate a machine learning model with a Django API. The project uses the following tools:

- Django: a Python web framework that allows you to create web applications.
- Django REST Framework: a toolkit for building APIs in Django.
- NumPy: a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays.
- pandas: a fast, powerful, flexible, and easy-to-use open-source data analysis and manipulation tool.
- pickle: a Python module used to serialize and deserialize objects.

## Get Started : 
1- Clone the repository:
```cmd  
git clone https://github.com/Abdel-RahmanSaied/ml_model_integration.git
```

2 - Create a virtual environment:
``` python
python -m venv env
```
3- Activate the virtual environment:
```
source env/bin/activate
```
4- Install the requirements:
```
pip install -r requirements.txt
```
5- Run the migrations:
```
python manage.py migrate
python manage.py makemigrations
```
6- Create a superuser:
```
python manage.py createsuperuser
```
7- Run the server:
```
python manage.py runserver
```
8- Open your browser and go to http://localhost:8000/. You should see the Django REST Framework's default API root.

# API endpoints
The project has the following API endpoints:

/model/: This endpoint takes in a POST request with data in JSON format and returns a prediction from the machine learning model. The expected input data is a dictionary with the following keys: 

- Pregnancies
- Glucose
- BloodPressure
- SkinThickness
- Insulin
- BMI
- DiabetesPedigreeFunction
- Age


Contributing
If you'd like to contribute to this project, feel free to create a pull request.


## Demo

you can use this end point to try !

https://mlintegration.pythonanywhere.com/model/

note : 
- this lind will expired after 3 month 
## Authors

- [@Abdel-Rahman Saied](https://github.com/Abdel-RahmanSaied)

