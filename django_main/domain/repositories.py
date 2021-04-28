# from channels.db import database_sync_to_async

from django_main.domain.models import Customer


class CustomerRepo:
    async def get_customer(**kwargs):
        customer = await __get_customer(**kwargs)
        return customer[0]


    async def get_last_customer():
        customer = await __get_customer(is_last=True)
        return customer


    async def create_customer(**kwargs):
        x = await __create_customer(**kwargs)
        customer = await __get_customer(is_last=True)
        return customer


    async def update_customer(customer_id, **kwargs):
        x = await __update_customer(customer_id, **kwargs)
        customer = await __get_customer(customer_id=customer_id)
        return customer


    @database_sync_to_async
    def __get_customer(is_last=False, **kwargs):
        if is_last:
            return Customer.objects.last()

        return Customer.objects.filter(**kwargs).all()


    @database_sync_to_async
    def __create_customer(**kwargs):
        Customer.objects.create(**kwargs)


    @database_sync_to_async
    def __update_customer(customer_id, **kwargs):
        Customer.objects.filter(id=customer_id).update(**kwargs)


    @database_sync_to_async
    def delete_customer(customer_id):
        Customer.objects.delete(id=customer_id)
