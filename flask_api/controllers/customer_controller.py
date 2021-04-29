from flask import jsonify

from django_main.domain.repositories import CustomerRepo

cache = {}
repo = CustomerRepo()


def customer(request, customer_id: int,  use_cache: bool):
    if request.method == 'GET':
        if use_cache:
            if customer_id in cache:
                return jsonify(**cache.get(customer_id))

        customer_data = repo.get_customer(id=customer_id)
        cache[customer_id] = customer_data.to_dict()
        return jsonify(**customer_data.to_dict())

    if request.method == 'POST':
        request_body = request.get_json(force=True)  # must use force=True if content-type: application/json wasn't supplied
        customer_data = repo.create_customer(**request_body)
        return jsonify(**customer_data.to_dict())
