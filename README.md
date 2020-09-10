# POLL CREATOR
![](res/chart.png)
https://pollcreator.herokuapp.com/


Create short surveys with people and generate a unique link for same - Poll Creator helps you tp find the answers easily. You can create a account as well for maintaining the record of old polls.
Polls can be deleted only by the user. 
> Note: In case you are not a user, you can not delete a poll  

The webapp also allows user to add image to each choice and each poll question.

# Run the code:
```
python manage.py runserver
```

# Deployment - Heroku:

```
heroku login
cd poll_anywhere
git init
git add .
git commit -m "$message"
heroku create $websitename
```
Add environment variables:
```
heroku config:set EMAIL='email@email.com'
heroku config:set PASSWORD='$password'
heroku config:set SECRET_KEY='$djangosecretkey[path=poll_anywhere/settings.py]'
heroku config:set DEBUG_VALUE='True/False'
heroku config:set EMAIL='email@email.com'
```
Use postgresql heroku-addon:
```
heroku addons:create heroku-postgresql:hobby-dev
```

Migrate changes:
```
heroku run python manage.py makemigrations
heroku run python manage.py migrate
```
Create Super-user:
```
heroku run python manage.py createsuperuser
```
Run Heroku-cli:
```
heroku run bash
```


# Tech Stack:
* Django
* JavaScript
* Bootstrap
* HTML

