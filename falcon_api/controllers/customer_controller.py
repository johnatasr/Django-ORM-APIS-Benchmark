import falcon as falcon
from django_main.domain.repositories import CustomerRepo

cache = {}
USE_CACHE = False
repo = CustomerRepo()


class CustomerController:
    @staticmethod
    def __return_error(resp, e):
        resp.status = falcon.HTTP_500
        resp.media = {"error": str(e)}

    def on_get(self, req, resp, customer_id=None):
        resp.status = falcon.HTTP_200

        if USE_CACHE:
            if customer_id in cache:
                resp.media = cache.get(customer_id)
                return

        customer = repo.get_customer(id=customer_id)
        cache[customer_id] = customer.to_dict()
        resp.media = customer.to_dict()

    def on_delete(self, req, resp, customer_id=None):
        try:
            repo.delete_customer(customer_id)
            resp.media = {"success": True}
        except Exception as e:
            self.__return_error(resp, e)

    def on_put(self, req, resp, customer_id=None):
        resp.status = falcon.HTTP_200
        try:
            customer_data_to_update = req.media
            customer = repo.update_customer(customer_id, **customer_data_to_update)
            resp.media = customer.to_dict()
        except Exception as e:
            self.__return_error(resp, e)

    def on_post(self, req, resp):
        resp.status = falcon.HTTP_200
        try:
            customer_data = req.media
            customer = repo.create_customer(**customer_data)
            resp.media = customer.to_dict()
        except Exception as e:
            self.__return_error(resp, e)
