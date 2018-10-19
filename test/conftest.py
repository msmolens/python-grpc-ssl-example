"""
Common fixtures for tests.
"""


import grpc
import mock
import pytest

import shopping_list_pb2

from shopping_list_service import ShoppingListService


@pytest.fixture
def service():
    """
    Fixture for shopping list service.
    """
    return ShoppingListService()


@pytest.fixture
def context():
    """
    Fixture for mock servicer context.
    """
    mock_context = mock.create_autospec(spec=grpc.ServicerContext)
    return mock_context


@pytest.fixture
def create_shopping_list(service, context):
    """
    Fixture for factory function to create a shopping list.
    """
    def _create_shopping_list(name, description=None):
        shopping_list = shopping_list_pb2.ShoppingList(
            name=name,
            description=description
        )
        request = shopping_list_pb2.CreateShoppingListRequest(
            shopping_list=shopping_list
        )
        response = service.CreateShoppingList(request, context)
        return response

    return _create_shopping_list
