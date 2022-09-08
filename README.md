# Task-Time Predictor
The Task Time Predictor utilizes the user's data to create a model that predicts how much time a task will take.
The main goal is to feed a database that would contain a lot of data, diminishing the amount of data needed to create a functional model for individual users.

# How it works
By utilizing questionary data containing user profile, user experience and user expectation about individual tasks (aswell as information about the tasks themselves), a prediction model will be created to predict the time needed to complete other tasks.
The initial idea is to use a light-weight machine learning model (like XGBoost), since training time is a limitant to the user's experience. 

# What is the purpose of this project
I want to get better at storing large quantities of data into a database and better at accessing this data for machine learning training. Also, I've always wanted something like this in my life, since I have difficulty estimating the ammount of time I will use for a particular task. I think most of the things we do as humans could be predicted, given the dataset is good enough.