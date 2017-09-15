# Python: Getting Started

A barebones Django app, which can easily be deployed to Heroku.


## Deploying to Heroku

```sh
$ heroku create
$ git push heroku master

$ heroku run python manage.py migrate
$ heroku run python manage.py shell
on shell do this  
> import ReadCSV.py
> exit()

$ heroku open
```
"# Restaurants" 
