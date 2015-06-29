# flask-blog
Simple Blog app using Flask and StormPath API for authentication

## How to test the app:

- Clone using `cd && git clone https://github.com/manojpandey/flask-blog.git`

- `cd flaskr`

- `virtualenv venv`

- `source venv/bin/activate`

- `pip install -r requirements.txt`

- You'll need a stormpath account to get the API key.

	- Register/Login at `https://api.stormpath.com`

	- Create API key

		- This will download an API key on your system

		- `mv ~/Downloads/apiKey-blahblah ~/flaskr/apiKey.properties`

	- Create a new Stormpath application from Applications page: https://api.stormpath.com/v#!applications. Create a new application named `flaskr`, with the default options selected.

	- Visit the Accounts page: https://api.stormpath.com/ui/accounts/create and create a new user account in: `flaskr Directory`. Remember the credentials. You can fill in any random emailID and password for testing the app.


- `python flaskr.py`

- Open `localhost:5000`

- Login with the credentials

- Create posts !

- Enjoy

## Test app on Heroku:

- Login Email: testuser1@flaskr.com

- Password: TestUser1

- Don't spam.
