# PageLoad
Python3 and Django version higher than 2 should be installed first
Then run the web-app using python manage.py runserver
It will first redirect to home-page (http://127.0.0.1:8000/)
Then to access login-page (http://127.0.0.1:8000/login/)
To access the page where all the logs for home-page are stored, goto (http://127.0.0.1:8000/pageload/)
If you access the home-page without logging in, it shows as empty user
But if you first login and then goto home page, it shows as that user
It records all the requests for home in a JSON file
