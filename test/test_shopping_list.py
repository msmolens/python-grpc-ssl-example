"""
Tests for ShoppingListService shopping list methods.
"""

import grpc
import pytest

import shopping_list_pb2


@pytest.fixture
def update_shopping_list(service, context):
    """
    Fixture for factory function to update a shopping list.
    """
    def _update_shopping_list(shopping_list):
        request = shopping_list_pb2.UpdateShoppingListRequest(
            shopping_list=shopping_list
        )
        response = service.UpdateShoppingList(request, context)
        return response

    return _update_shopping_list


@pytest.fixture
def delete_shopping_list(service, context):
    """
    Fixture for factory function to delete a shopping list.
    """
    def _delete_shopping_list(shopping_list_id):
        request = shopping_list_pb2.DeleteShoppingListRequest(
            shopping_list_id=shopping_list_id
        )
        response = service.DeleteShoppingList(request, context)
        return response

    return _delete_shopping_list


@pytest.fixture
def list_shopping_lists(service, context):
    """
    Fixture for factory function to list the shopping lists.
    """
    def _list_shopping_lists(filter=None):
        request = shopping_list_pb2.ListShoppingListsRequest(
            filter=filter
        )
        response = service.ListShoppingLists(request, context)
        return response

    return _list_shopping_lists


@pytest.fixture
def list_shopping_lists_stream(service, context):
    """
    Fixture for factory function to list the shopping lists, returning results
    as a stream.
    """
    def _list_shopping_lists_stream(filter=None):
        request = shopping_list_pb2.ListShoppingListsStreamRequest(
            filter=filter
        )
        response = service.ListShoppingListsStream(request, context)
        return response

    return _list_shopping_lists_stream


def test_create_shopping_lists(create_shopping_list):
    response1 = create_shopping_list('Groceries', 'Ingredients for dinner')

    assert len(response1.id) > 0
    assert response1.name == 'Groceries'
    assert response1.description == 'Ingredients for dinner'

    response2 = create_shopping_list('Pet supplies')

    assert len(response2.id) > 0
    assert response2.id != response1.id
    assert response2.name == 'Pet supplies'
    assert not response2.description


def test_create_shopping_list_with_empty_name(context, create_shopping_list):
    create_shopping_list('')

    context.set_code.assert_called_once_with(grpc.StatusCode.INVALID_ARGUMENT)
    context.set_details.assert_called_once_with('Name cannot be empty')


def test_update_shopping_list(create_shopping_list, update_shopping_list):
    shopping_list = create_shopping_list('Groceries', 'Ingredients for dinner')
    shopping_list.name = 'Snack Food'
    shopping_list = update_shopping_list(shopping_list)
    assert shopping_list.name == 'Snack Food'


def test_update_shopping_list_to_empty_name(context, create_shopping_list, update_shopping_list):
    shopping_list = create_shopping_list('Groceries', 'Ingredients for dinner')
    shopping_list.name = ''
    update_shopping_list(shopping_list)

    context.set_code.assert_called_once_with(grpc.StatusCode.INVALID_ARGUMENT)
    context.set_details.assert_called_once_with('Name cannot be empty')


def test_update_invalid_shopping_list(context, create_shopping_list, update_shopping_list):
    shopping_list = create_shopping_list('Groceries', 'Ingredients for dinner')
    shopping_list.id = 'invalid id'
    shopping_list = update_shopping_list(shopping_list)

    context.set_code.assert_called_once_with(grpc.StatusCode.NOT_FOUND)
    context.set_details.assert_called_once_with('Not found')


def test_delete_shopping_list(create_shopping_list, delete_shopping_list):
    shopping_list = create_shopping_list('Groceries')
    response = delete_shopping_list(shopping_list.id)
    assert response.shopping_list.id == shopping_list.id


def test_delete_invalid_shopping_list(context, create_shopping_list, delete_shopping_list):
    create_shopping_list('Groceries')
    delete_shopping_list('invalid id')

    context.set_code.assert_called_once_with(grpc.StatusCode.NOT_FOUND)
    context.set_details.assert_called_once_with('Not found')


def test_list_shopping_lists(create_shopping_list, list_shopping_lists):
    response = list_shopping_lists()
    assert not response.shopping_lists

    create_shopping_list('List 1')
    create_shopping_list('List 2')

    response = list_shopping_lists()
    assert len(response.shopping_lists) == 2

    assert response.shopping_lists[0].name == 'List 1'
    assert response.shopping_lists[1].name == 'List 2'


def test_list_shopping_lists_filter(create_shopping_list, list_shopping_lists):
    create_shopping_list('List 1')
    create_shopping_list('List 2')

    response = list_shopping_lists(filter='List')
    assert len(response.shopping_lists) == 2

    response = list_shopping_lists(filter='List 1')
    assert len(response.shopping_lists) == 1
    assert response.shopping_lists[0].name == 'List 1'

    response = list_shopping_lists(filter='2')
    assert len(response.shopping_lists) == 1
    assert response.shopping_lists[0].name == 'List 2'


def test_list_shopping_lists_stream(create_shopping_list, list_shopping_lists_stream):
    response = list(list_shopping_lists_stream())
    assert not response

    create_shopping_list('List 1')
    create_shopping_list('List 2')

    shopping_lists = list(list_shopping_lists_stream())
    assert len(shopping_lists) == 2

    assert shopping_lists[0].name == 'List 1'
    assert shopping_lists[1].name == 'List 2'


def test_list_shopping_lists_stream_filter(create_shopping_list, list_shopping_lists_stream):
    create_shopping_list('List 1')
    create_shopping_list('List 2')

    shopping_lists = list(list_shopping_lists_stream(filter='List'))
    assert len(shopping_lists) == 2

    shopping_lists = list(list_shopping_lists_stream(filter='List 1'))
    assert len(shopping_lists) == 1
    assert shopping_lists[0].name == 'List 1'

    shopping_lists = list(list_shopping_lists_stream(filter='2'))
    assert len(shopping_lists) == 1
    assert shopping_lists[0].name == 'List 2'
