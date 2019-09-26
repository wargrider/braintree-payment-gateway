# Braintree Payment Gateway

## Prerequisites:

You will need the following programmes properly installed on your computer.

* [Python](https://www.python.org/) 3.5+
* Virtual Environment

To install virtual environment on your system use:

```bash
pip install virtualenv

or

pip3 install virtualenv #if using linux(for python 3 and above)
```
```
# Creating a Braintree sandbox account
- Open https://www.braintreepayments.com/sandbox in your browser
- You will see a form, Fill in the details to create a new sandbox account.
- You will receive an email from Braintree with a link to complete your account setup.Follow the link and complete your account setup.
- Once you are done, login at https://sandbox.braintreegateway.com/login . Your merchant ID and private/public keys will be displayed 
- Add these keys to your settings.py file.

```

## Installation and Running :

```bash
git clone https://github.com/ongraphpythondev/Braintreepayment.git

cd Braintreepayment 

virtualenv venv 
      or 
virtualenv venv -p python3 #if using linux(for python 3 and above)

venv\Scripts\activate # for windows
      or
source venv/bin/activate # for linux

# install required packages for the project to run

pip install -r requirements.txt

python manage.py runserver
```
