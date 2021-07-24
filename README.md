# music-recommender-rest-api
A music recommendation REST API which makes a machine learning algorithm work with the Django REST Framework 

![alt text](https://github.com/ReaperZ0v/music-recommender-rest-api/blob/main/model/graphviz.png)

## How it works
The REST API has a simple operational flow which goes like so :
1. > User signs up at the ```/sign-up``` endpoint 
2. > User logs in using Django REST Framework's basic authentication via the ```/login``` endpoint
3. > After successful authentication user can then navigate to the ```/recommend``` endpoint 

## Deeper Intuition 
The code I have designed is connected directly to a packaged machine learning model, a user signs up by providing data such as gender, age, name etc. Once a sign up is successful then the user can login to use the ```/recommend``` endpoint to get recommendations on music that best fits the user's age/gender. Music Albums are stored in an SQLite database and are picked then displayed to user at the ```/recommend``` endpoint. Now the question is what's the process look like in simple steps? :

1. > User signs up and provides info like gender, age, name, etc..
2. > Once user logs in and navigates to ```/recommend``` endpoint, the back end will send that authenticated user's age & gender to the packaged ML model for evaluation / to get a prediction on what genre of music would be best for the user's age/gender type.
3. > once a genre is predicted by ML model the result is sent to a queryset for filtering thus returning music from the database the REST API is connected to which has the genre that was predicted in the first place.

## Setup
1. > run the command ```pip3 install -r requirements.txt``` to install required libraries 
2. > setup migrations by running command ```python3 manage.py makemigrations accounts``` and ```python3 manage.py makemigrations api```
3. > finally apply migrations by running command ```python3 manage.py migrate```
4. > create a super user for accessing ```/admin``` by running command ```python3 manage.py createsuperuser```
5. > after that just fill the database with some albums of different genres from the admin panel
6. > and you are **Done!** 
