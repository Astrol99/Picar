from flask import Flask

api = Flask(__name__)

@api.route('/profile')
def my_profile():
    response_body = {
        "name": "David",
        "about": "I like men"
    }

    return response_body

