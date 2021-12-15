from flask import Flask
from flask import request

from flask_api.controllers.customer_controller import customer

app = Flask(__name__)

cache = {}
USE_CACHE = False


@app.route('/flask/customer/<int:customer_id>', methods=['GET', 'DELETE', 'PUT'])
@app.route('/flask/customer', methods=['POST'])
def customer_resource(customer_id=None):
    return customer(request, customer_id, USE_CACHE)


if __name__ == '__main__':
    app.run(port=8001)
