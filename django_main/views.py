# Create your views here.
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.status import HTTP_200_OK, HTTP_500_INTERNAL_SERVER_ERROR
from rest_framework.response import Response
from django_main.domain.repositories import CustomerRepo


# Register your viewsets here.
class CustomerViewSet(viewsets.GenericViewSet):
    """
    API made using Django Rest Framework
    """

    http_method_names = ["get", "post"]
    repo = CustomerRepo()

    @action(methods=["POST"], detail=False, url_path="drf/get")
    def get_customers(self, request):
        """
           Endpoint to search a list of users by coordinates
           :param request:
           :return: dict
        """
        try:
            search_results = self.repo.get_customer()
            return Response(search_results, status=HTTP_200_OK)
        except Exception as error:
            return Response(error, status=HTTP_500_INTERNAL_SERVER_ERROR)