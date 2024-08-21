import requests

response = requests.get('http://google.com')
print(response)

# Commands to create virtual env using pipenv
# pipenv install requests
# pipenv shell
# exit


# To publish a package
# pip3 install twine
# python3 setup.py sdist bdist_wheel
# twine upload dist/*
