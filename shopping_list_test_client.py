#!/usr/bin/env python

"""Shopping list gRPC test client."""

import click
import grpc
import sys
import time

import shopping_list_pb2
import shopping_list_pb2_grpc


def read_certificates(certificates):
    """Read certificates from file. """
    with open(certificates, 'rb') as f:
        certificates = f.read()
    return certificates


def create_shopping_list(stub, name, description=None):
    """Convenience function for RPC to create a shopping list."""
    shopping_list = shopping_list_pb2.ShoppingList(
        name=name,
        description=description
    )
    request = shopping_list_pb2.CreateShoppingListRequest(
        shopping_list=shopping_list
    )

    response = stub.CreateShoppingList(request)
    return response


def delete_shopping_list(stub, shopping_list):
    """Convenience function for RPC to delete a shopping list."""
    request = shopping_list_pb2.DeleteShoppingListRequest(
        shopping_list_id=shopping_list.id
    )
    response = stub.DeleteShoppingList(request)
    return response


def list_shopping_lists(stub, filter=None):
    """Convenience function for RPC to list shopping lists."""
    request = shopping_list_pb2.ListShoppingListsStreamRequest(
        filter=filter
    )
    return stub.ListShoppingListsStream(request)


def add_item(stub, shopping_list, name, description=None):
    """Convenience function for RPC to add an item to a shopping list."""
    item = shopping_list_pb2.Item(
        name=name,
        description=description
    )
    request = shopping_list_pb2.AddItemRequest(
        shopping_list_id=shopping_list.id,
        item=item
    )
    response = stub.AddItem(request)
    return response.item


def remove_item(stub, shopping_list, item):
    """Convenience function for RPC to remove an item from a shopping list."""
    request = shopping_list_pb2.RemoveItemRequest(
        shopping_list_id=shopping_list.id,
        item_id=item.id
    )
    response = stub.RemoveItem(request)
    return response


def set_item_checked(stub, shopping_list, item, checked):
    """Convenience function for RPC to set whether an item is checked."""
    request = shopping_list_pb2.SetItemCheckedRequest(
        shopping_list_id=shopping_list.id,
        item_id=item.id,
        checked=checked
    )
    response = stub.SetItemChecked(request)
    return response


def list_items(stub, shopping_list, filter=None):
    """Convenience function for RPC to list items in a shopping list."""
    request = shopping_list_pb2.ListItemsStreamRequest(
        shopping_list_id=shopping_list.id,
        filter=filter
    )
    return stub.ListItemsStream(request)


def pretty_print_item(item):
    """Pretty-print an item, including its checked status."""
    print('  [{}] {}'.format(
        'x' if item.checked else ' ',
        item.name))


@click.command()
@click.option('--host', default='localhost', help='Host to connect to')
@click.option('--port', default=8443, help='Port on host to connect to')
@click.option('--use-tls/--no-use-tls', default=True, help='Use transport layer security (TLS)')
@click.option('--certificates', default='server.crt', help='Certificate file')
def main(host, port, use_tls, certificates):
    if use_tls:
        try:
            certificates = read_certificates(certificates)
        except IOError as e:
            print('Failed to read certificate: {}'.format(e))
            sys.exit(1)

        credentials = grpc.ssl_channel_credentials(root_certificates=certificates)
        channel = grpc.secure_channel('{}:{}'.format(host, port), credentials)
    else:
        channel = grpc.insecure_channel('{}:{}'.format(host, port))

    stub = shopping_list_pb2_grpc.ShoppingListServiceStub(channel)

    try:
        # Print existing shopping lists
        print('Existing shopping lists: ')
        for shopping_list in list_shopping_lists(stub):
            num_items = len(list(list_items(stub, shopping_list)))
            print('  {} ({} items)'.format(shopping_list.name, num_items))
        else:
            print('  (none)')

        # Create a new shopping list
        name = 'Groceries-' + str(int(time.time()))
        print('Creating shopping list "{}"'.format(name))
        groceries = create_shopping_list(stub, name, 'Items for dinner and snacks')

        # Add items to shopping list
        print('Adding items...')
        bread = add_item(stub, groceries, 'Bread')
        butter = add_item(stub, groceries, 'Butter')
        cheese = add_item(stub, groceries, 'Cheese')
        tofu = add_item(stub, groceries, 'Tofu')

        # Check some items
        print('Checking some items...')
        set_item_checked(stub, groceries, bread, True)
        set_item_checked(stub, groceries, butter, True)
        set_item_checked(stub, groceries, butter, False)
        set_item_checked(stub, groceries, cheese, True)

        # List items in the shopping list
        print('Items:')
        for item in list_items(stub, groceries, filter=None):
            pretty_print_item(item)

        # Remove some items
        print('Removing some items...')
        remove_item(stub, groceries, bread)
        remove_item(stub, groceries, tofu)

        # List items in the shopping list
        print('Items:')
        for item in list_items(stub, groceries, filter=None):
            pretty_print_item(item)

        # Create a new shopping list and add some items
        name = 'Pet Supplies-' + str(int(time.time()))
        print('Creating shopping list "{}"'.format(name))
        pet_supplies = create_shopping_list(stub, name)
        print('Adding items...')
        add_item(stub, pet_supplies, 'Poop bags')
        dog_food = add_item(stub, pet_supplies, 'Dog food')
        set_item_checked(stub, pet_supplies, dog_food, False)
        set_item_checked(stub, pet_supplies, dog_food, True)
        print('Items:')
        for item in list_items(stub, pet_supplies, filter=None):
            pretty_print_item(item)

        # Delete shopping lists
        print('Deleting shopping lists...')
        delete_shopping_list(stub, groceries)
        delete_shopping_list(stub, pet_supplies)

        # Print existing shopping lists
        print('Existing shopping lists: ')
        for shopping_list in list_shopping_lists(stub):
            num_items = len(list(list_items(stub, shopping_list)))
            print('  {} ({} items)'.format(shopping_list.name, num_items))
        else:
            print('  (none)')

        print('Done')

    except grpc.RpcError as rpc_error_call:
        # Exception object is also a grpc.Call.
        # See https://github.com/grpc/grpc/issues/9270#issuecomment-398796613
        code = rpc_error_call.code()
        details = rpc_error_call.details()
        print(code, details)


if __name__ == '__main__':
    main()
