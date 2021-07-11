# COVID-19 Detection Web
Web to classify COVID-19 and normal patient in chest x-ray image using flask API and Keras CNN model.

## Documentation
Dataset from [Kaggle COVID-19 Radiography Database](https://www.kaggle.com/tawsifurrahman/covid19-radiography-database)

1. Create virtual environment
```command
python3 -m venv env
```
2. Activate virtual env
- Mac OS/Linux
```command
source env/bin/activate
```
- Windows
```command
env\Script\activate
```
3. Install Tensorflow, OpenCV, and Flask module
4. Place your saved Tensorflow model and put its directory path in covid_classification.py load_model function
5. Run Flask API
```command
python3 api.py
```
6. Open the localhost on web browser

## Screenshots
Home page
![home page](https://github.com/inayahsurya/covid-detection-web/blob/main/static/img/home.JPG)

Predict page
![predict page](https://github.com/inayahsurya/covid-detection-web/blob/main/static/img/predict.JPG)

Example
![example](https://github.com/inayahsurya/covid-detection-web/blob/main/static/img/normal%20clahe.JPG)
