# Deploying Machine Learning Models with Django
Tools used: Machine Learning with Python (Sklearn, pandas, numpy), Django(REST, POST), SQLite <br>

The purpose of this project was to build a Machine Learning model that predicts income level based on census data, and then to deploy that model to a Django server. In this project I utlized the Random Forest and Extra Trees algorithms for machine learning predictions, and built a django server that had interactivity using REST API. SQLite was the database of choice. Finally, I ran an A/B test to see which algorithm (random forest vs extra trees) yielded better results. <br>

The code for the machine learning training can be found [here](https://nbviewer.jupyter.org/github/pratsingh/ML_Django_Project/blob/main/research/ML.ipynb).

<br>
First image in the Django REST Framework view.
<img src="rest_view.png" alt="REST view in Django" width="550px"/>
Second image is the Predict feature.
 <img src="./images/predict.png" alt="predict" width="550px"/>
 Third image shows the A/B test algorithms list.
 <img src="./images/AB_test_list.png" alt="ABlist" width="450px"/>
 Fourth image shows result of the A/B test.
 <img src="./images/AB_finished.png" alt="ABlist" width="550px"/>
