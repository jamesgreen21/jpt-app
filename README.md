# JPT App

A website app for Joseph Paris, Personal Training, in which users can read about Joe, get useful hints and tips, register as a user and book PT sessions

#### Project Details @CodeInstitute
The temporary superuser username and password is "admin" and "Test123!" to test the admin features.

The app gives the user access to the home page where the user can read all the benefits available on the app with advertising throughout to catch the user’s attention and increase traffic

Authentication is used to control user access throughout the site. In this first release, the users will be able to sign up for free to gain access to the content, but the plan in a future release will be to include membership payments with this feature.

Once a user has an account they can view their profile, update their details and change their picture.

The user can view the Blog posts that can be updated by the Admin user, with ability to add, edit and delete blog posts. The user can also post questions to the app. This can be answered by the Admin user, who can choose to star the message so that it appears on the Blog page. 

The user can also user the Search app functionality built in to find a question already answered on the Blog app. This feature ignores the starred messages set by the Admin and instead searches all messages.

Finally, the user can access the PT & Products app, which allows the user to purchase “session tokens”, a way of storing PT sessions that you can then book through the app (coming soon). The user can buy any number of these tokens and is rewarded for buying more tokens by a lower £/session rate. Once a token is purchased it appears next to you username in the navbar and on the Profile page. The profile page links back to the Products app

The user can also purchase products available such as gym equipment, sportswear, etc. All the products are completely editable in the Admin Edit Mode.

##### Coming Soon
The Book app will be built next to allow users to book PT sessions using the session tokens, because let’s face it, what’s the point of them otherwise! The user will be shown a calendar with the ability to request a session time. The admin will be able to approve or reject the requests and will also be able to set working times and block out periods where unavailable.

## Frameworks & APIs
- [Django](https://www.djangoproject.com/) - Application
- [Bootstrap](https://getbootstrap.com/) - Core styling framework
- [jQuery](https://cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.min.js) - Core JS framework
- [AWS S3](https://aws.amazon.com/s3/) - Static & Media Storage
- [Stripe](https://stripe.com/gb) - Making payments
- [Heroku Postgres](https://dashboard.heroku.com/) - Database
- [Django Forms Bootstrap](https://pypi.org/project/django-forms-bootstrap//) - Form handling

## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install jpt-app within a virtual environment (assumed "venv"):

```bash
source venv/bin/activate
pip install requirements.txt
```


## Deployment
In order to deploy on Heroku, ensure all installation requirements are in-place, create a  GitHub repo and a Heroku app. Connect the Heorku app to the GitHub repo and set to automatically deploy. 

Within Heroku-Resources, create a Heroku Postgres DB. In Settings, Config Vars, set the following:

```
AWS_ACCESS_KEY_ID = "AWS S3 access id"
AWS_SECRET_ACCESS_KEY = "AWS S3 secret key"
EMAIL_ADDRESS = "The email address to send emails from"
EMAIL_PASSWORD = "The password of the email account used"
STRIPE_PUBLISHABLE = "See Stripe set-up for this information ( link above )"
STRIPE_SECRET = "See Stripe set-up for this information ( link above )"
DATABASE_URL = "The Postgres DB created in Heroku"
SECRET_KEY = "A desire secret key"
```
## Compatibility
The following browsers have been tested for compatibility with this app:

- Google Chrome
- Firefox

## Testing

### UnitTesting
Unit testing has been set up in the health_blog App to demonstrate testing and Travis CI API

### In App Testing
- General navigation and clicking on all links
- All django messages display successfully
- Main App
    - Navbar – All links are correct and highlight appropriately according to the active page
    - Home screen – all links are correctly set up
    - Book App (coming soon) page set up, links correct
- Health Blog App
    - Admin Edit mode behaves correct with user login
    - All links correct
    - Add/Edit/Delte Blog Page (Admin Edit Mode) opens correct and able to submit. All input checks have been successful
    - Go to Q&A Page (Admin Edit Mode) opens correct and able to submit. All input checks have been successful
    - FAQ post question form functions correctly
    - Starred messages (editable from the Admin Edit Mode) are displaying correct
- Product App
    - Admin Edit mode behaves correct with user login
    - All links correct
    - Add/Edit/Delte Product Page (Admin Edit Mode) opens correct and able to submit. All input checks have been successful
    - Go to Q&A Page (Admin Edit Mode) opens correct and able to submit. All input checks have been successful
    - Go to Checkout ‘safe’ message displays
- Cart & Checkout Apps
    - All links correct
    - Cart navbar count functioning
    - Checkout form submits successfully using appropriate random user information, including the following inputs:
        - Credit card number – 4242424242424242
        - Security code (CVV) – 111
        - Month – 12
        - Year – 2020
    - Checkout – testing the session_tokens are updated to the user Profile
- Accounts App
    - Login and Logout functionality tested successfully
    - Register form submits correctly, prevents users using the same email and weak password entries
    - Profile page Loads all detail correctly. The form submits correctly
    - Change password page loads successfully, and form submits correctly
    - Login forgotten password page submits correctly

### Bugs

- Bug found with authentication between app and gmail account “SMTPAuthenticationError”, which happens intermittently and is a common problem according to Stack Overflow

## Acknowledgments
A big thank you to the following:
- Digital Fusion for Navbar scroll-up display - http://teamdf.com/jquery-plugins/license/
- Meal prepping content - https://www.thelantern.com/2018/01/the-dos-and-donts-of-meal-prepping/
- Meal Images - https://selecthealth.org/blog/2019/03/6-ideas-to-make-meal-prep-easier

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
There are currently no licensing on this application


[![Build Status](https://travis-ci.com/jamesgreen21/jpt-app.svg?branch=master)](https://travis-ci.com/jamesgreen21/jpt-app)