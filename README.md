# COVID-19 Detection Web
Web to classify COVID-19 in chest x-ray image using flask API Tensorflow Keras CNN model.

## Documentation
Dataset from [Kaggle COVID-19 Radiography Database](https://www.kaggle.com/tawsifurrahman/covid19-radiography-database)

1. Create virtual environment
```command
python3 -m venv env
```
2. Install Tensorflow, OpenCV, and Flask module
3. Place your saved Tensorflow model and put its directory in covid_classification.py load_model function
4. Run Flask API
```command
python3 api.py
```
5. Open the localhost on web browser

## Screenshots
Home page
![home page](https://github.com/inayahsurya/covid-detection-web/blob/main/static/img/home.JPG)

Predict page
![predict page](https://github.com/inayahsurya/covid-detection-web/blob/main/static/img/predict.JPG)

Example
![example](https://github.com/inayahsurya/covid-detection-web/blob/main/static/img/normal%20clahe.JPG)
