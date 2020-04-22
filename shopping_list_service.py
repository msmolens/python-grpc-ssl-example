"""Shopping list gRPC service."""

import grpc
import uuid

from collections import OrderedDict, namedtuple

from shopping_list_pb2 import (
    AddItemResponse,
    DeleteShoppingListResponse,
    Item,
    ListItemsResponse,
    ListShoppingListsResponse,
    RemoveItemResponse,
    SetItemCheckedResponse,
    ShoppingList,
)

from shopping_list_pb2_grpc import ShoppingListServiceServicer


# Container for shopping list data.
# Fields:
# - shopping_list: shopping_list_pb2.ShoppingList
# - items: Ordered dictionary of shopping_list_pb2.Item keyed on item ID
ShoppingListData = namedtuple('ShoppingListData', ['shopping_list', 'items'])


class ShoppingListService(ShoppingListServiceServicer):
    """
    Shopping list service implementation.
    """
    def __init__(self):
        # Ordered dictionary of ShoppingListData keyed on shopping list ID
        self._data = OrderedDict()

    def _generateId(self):
        return uuid.uuid4().hex

    def _filteredShoppingLists(self, filter=None):
        """
        Return generator expression of shopping lists with names that match the specified filter.
        """
        return (
            data.shopping_list
            for data in self._data.values()
            if not filter or filter in data.shopping_list.name
        )

    def _filteredItems(self, items, filter=None):
        """
        Return generator expression of items with names that match the specified filter.
        """
        return (
            item
            for item in items.values()
            if not filter or filter in item.name
        )

    def CreateShoppingList(self, request, context):
        if not request.shopping_list.name:
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details('Name cannot be empty')
            return ShoppingList()

        request.shopping_list.id = self._generateId()

        self._data[request.shopping_list.id] = ShoppingListData(
            shopping_list=request.shopping_list,
            items=OrderedDict()
        )

        return request.shopping_list

    def UpdateShoppingList(self, request, context):
        if request.shopping_list.id not in self._data:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('Not found')
            return ShoppingList()

        if not request.shopping_list.name:
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details('Name cannot be empty')
            return ShoppingList()

        data = self._data[request.shopping_list.id]
        self._data[request.shopping_list.id] = ShoppingListData(
            shopping_list=request.shopping_list,
            items=data.items
        )

        return request.shopping_list

    def DeleteShoppingList(self, request, context):
        data = self._data.pop(request.shopping_list_id, None)
        if data is None:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('Not found')
            return ShoppingList()

        return DeleteShoppingListResponse(
            shopping_list=data.shopping_list
        )

    def ListShoppingLists(self, request, context):
        response = ListShoppingListsResponse(
            shopping_lists=self._filteredShoppingLists(request.filter)
        )
        return response

    def ListShoppingListsStream(self, request, context):
        return self._filteredShoppingLists(request.filter)

    def AddItem(self, request, context):
        data = self._data.get(request.shopping_list_id)
        if data is None:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('Not found')
            return Item()

        request.item.id = self._generateId()

        data.items[request.item.id] = request.item

        response = AddItemResponse(
            item=request.item
        )

        return response

    def RemoveItem(self, request, context):
        data = self._data.get(request.shopping_list_id)
        if data is None:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('Shopping list not found')
            return RemoveItemResponse()

        item = data.items.pop(request.item_id, None)
        if item is None:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('Item not found')
            return RemoveItemResponse()

        return RemoveItemResponse(
            item=item
        )

    def SetItemChecked(self, request, context):
        data = self._data.get(request.shopping_list_id)
        if data is None:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('Shopping list not found')
            return SetItemCheckedResponse()

        item = data.items.get(request.item_id, None)
        if item is None:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('Item not found')
            return SetItemCheckedResponse()

        item.checked = request.checked

        return SetItemCheckedResponse(
            item=item
        )

    def ListItems(self, request, context):
        data = self._data.get(request.shopping_list_id)
        if data is None:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('Shopping list not found')
            return SetItemCheckedResponse()

        response = ListItemsResponse(
            items=self._filteredItems(data.items, request.filter)
        )
        return response

    def ListItemsStream(self, request, context):
        data = self._data.get(request.shopping_list_id)
        if data is None:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('Shopping list not found')
            return SetItemCheckedResponse()

        return self._filteredItems(data.items, request.filter)
