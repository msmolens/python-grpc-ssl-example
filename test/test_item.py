"""
Tests for ShoppingListService item methods.
"""

import grpc
import pytest

import shopping_list_pb2


@pytest.fixture
def add_item(service, context):
    """
    Fixture for factory function to add an item to a shopping list.
    """
    def _add_item(shopping_list, name, description=None):
        item = shopping_list_pb2.Item(
            name=name,
            description=description
        )
        request = shopping_list_pb2.AddItemRequest(
            shopping_list_id=shopping_list.id,
            item=item
        )
        response = service.AddItem(request, context)
        return response

    return _add_item


@pytest.fixture
def remove_item(service, context):
    """
    Fixture for factory function to remove an item from a shopping list.
    """
    def _remove_item(shopping_list, item_id):
        request = shopping_list_pb2.RemoveItemRequest(
            shopping_list_id=shopping_list.id,
            item_id=item_id
        )
        response = service.RemoveItem(request, context)
        return response

    return _remove_item


@pytest.fixture
def set_item_checked(service, context):
    """
    Fixture for factory function to set whether an item is checked.
    """
    def _set_item_checked(shopping_list, item, checked):
        request = shopping_list_pb2.SetItemCheckedRequest(
            shopping_list_id=shopping_list.id,
            item_id=item.id,
            checked=checked
        )
        response = service.SetItemChecked(request, context)
        return response

    return _set_item_checked


@pytest.fixture
def list_items(service, context):
    """
    Fixture for factory function to list the items in a shopping list.
    """
    def _list_items(shopping_list, filter=None):
        request = shopping_list_pb2.ListItemsRequest(
            shopping_list_id=shopping_list.id,
            filter=filter
        )
        response = service.ListItems(request, context)
        return response

    return _list_items


@pytest.fixture
def list_items_stream(service, context):
    """
    Fixture for factory function to list the items in a shopping list, returning
    results as a stream.
    """
    def _list_items_stream(shopping_list, filter=None):
        request = shopping_list_pb2.ListItemsStreamRequest(
            shopping_list_id=shopping_list.id,
            filter=filter
        )
        response = service.ListItemsStream(request, context)
        return response

    return _list_items_stream


def test_add_item(create_shopping_list, add_item):
    shopping_list = create_shopping_list('Groceries')

    response = add_item(shopping_list, 'Bread', 'Whole Wheat')
    item1 = response.item

    assert len(item1.id) > 0
    assert item1.name == 'Bread'
    assert item1.description == 'Whole Wheat'

    response = add_item(shopping_list, 'Yogurt', 'Full Fat')
    item2 = response.item

    assert len(item2.id) > 0
    assert item2.id != item1.id
    assert item2.name == 'Yogurt'
    assert item2.description == 'Full Fat'


def test_add_item_invalid_shopping_list(context, create_shopping_list, add_item):
    shopping_list = shopping_list_pb2.ShoppingList()

    add_item(shopping_list, 'Bread', 'Whole Wheat')

    context.set_code.assert_called_once_with(grpc.StatusCode.NOT_FOUND)
    context.set_details.assert_called_once_with('Not found')


def test_remove_item(create_shopping_list, add_item, remove_item):
    shopping_list = create_shopping_list('Groceries')
    item1 = add_item(shopping_list, 'Bread', 'Whole Wheat').item
    item2 = add_item(shopping_list, 'Bread', 'Sourdough').item

    response = remove_item(shopping_list, item1.id)
    assert response.item.id == item1.id
    response = remove_item(shopping_list, item2.id)
    assert response.item.id == item2.id


def test_remove_item_invalid_shopping_list(context, remove_item):
    shopping_list = shopping_list_pb2.ShoppingList()
    remove_item(shopping_list, '')

    context.set_code.assert_called_once_with(grpc.StatusCode.NOT_FOUND)
    context.set_details.assert_called_once_with('Shopping list not found')


def test_remove_invalid_item(context, create_shopping_list, add_item, remove_item):
    shopping_list = create_shopping_list('Groceries')
    add_item(shopping_list, 'Bread', 'Whole Wheat')

    remove_item(shopping_list, 'invalid_id')

    context.set_code.assert_called_once_with(grpc.StatusCode.NOT_FOUND)
    context.set_details.assert_called_once_with('Item not found')


def test_set_item_checked(create_shopping_list, add_item, set_item_checked):
    shopping_list = create_shopping_list('Groceries')

    response = add_item(shopping_list, 'Bread', 'Whole Wheat')
    item = response.item

    assert not item.checked

    item = set_item_checked(shopping_list, item, False).item
    assert not item.checked

    item = set_item_checked(shopping_list, item, True).item
    assert item.checked


def test_set_item_checked_invalid_shopping_list(context, set_item_checked):
    shopping_list = shopping_list_pb2.ShoppingList()
    item = shopping_list_pb2.Item()
    set_item_checked(shopping_list, item, True)

    context.set_code.assert_called_once_with(grpc.StatusCode.NOT_FOUND)
    context.set_details.assert_called_once_with('Shopping list not found')


def test_set_invalid_item_checked(context, create_shopping_list, add_item, set_item_checked):
    shopping_list = create_shopping_list('Groceries')

    item = shopping_list_pb2.Item()
    set_item_checked(shopping_list, item, True)

    context.set_code.assert_called_once_with(grpc.StatusCode.NOT_FOUND)
    context.set_details.assert_called_once_with('Item not found')


def test_list_items(create_shopping_list, add_item, remove_item, list_items):
    shopping_list = create_shopping_list('Groceries')
    response = list_items(shopping_list)
    assert not response.items

    item1 = add_item(shopping_list, 'Salt').item
    item2 = add_item(shopping_list, 'Pepper').item

    response = list_items(shopping_list)
    assert len(response.items) == 2
    assert response.items[0].name == 'Salt'
    assert response.items[1].name == 'Pepper'

    remove_item(shopping_list, item1.id)

    response = list_items(shopping_list)
    assert len(response.items) == 1
    assert response.items[0].name == 'Pepper'

    remove_item(shopping_list, item2.id)
    response = list_items(shopping_list)
    assert not response.items


def test_list_items_filter(create_shopping_list, add_item, list_items):
    shopping_list = create_shopping_list('Groceries')
    add_item(shopping_list, 'Salt')
    add_item(shopping_list, 'Pepper')
    add_item(shopping_list, 'Pepper Jack Cheese')
    add_item(shopping_list, 'Cheddar Cheese')

    response = list_items(shopping_list, filter='Salt')
    assert len(response.items) == 1

    response = list_items(shopping_list, filter='Jack')
    assert len(response.items) == 1

    response = list_items(shopping_list, filter='Pepper')
    assert len(response.items) == 2

    response = list_items(shopping_list, filter='Cheese')
    assert len(response.items) == 2


def test_list_items_stream(create_shopping_list, add_item, remove_item, list_items_stream):
    shopping_list = create_shopping_list('Groceries')
    response = list(list_items_stream(shopping_list))
    assert not response

    item1 = add_item(shopping_list, 'Salt').item
    item2 = add_item(shopping_list, 'Pepper').item

    items = list(list_items_stream(shopping_list))
    assert len(items) == 2
    assert items[0].name == 'Salt'
    assert items[1].name == 'Pepper'

    remove_item(shopping_list, item1.id)
    items = list(list_items_stream(shopping_list))
    assert len(items) == 1
    assert items[0].name == 'Pepper'

    remove_item(shopping_list, item2.id)
    items = list(list_items_stream(shopping_list))
    assert not items


def test_list_items_stream_filter(create_shopping_list, add_item, list_items_stream):
    shopping_list = create_shopping_list('Groceries')
    add_item(shopping_list, 'Salt')
    add_item(shopping_list, 'Pepper')
    add_item(shopping_list, 'Pepper Jack Cheese')
    add_item(shopping_list, 'Cheddar Cheese')

    items = list(list_items_stream(shopping_list, filter='Salt'))
    assert len(items) == 1

    items = list(list_items_stream(shopping_list, filter='Jack'))
    assert len(items) == 1

    items = list(list_items_stream(shopping_list, filter='Pepper'))
    assert len(items) == 2

    items = list(list_items_stream(shopping_list, filter='Cheese'))
    assert len(items) == 2
