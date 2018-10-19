# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: shopping_list.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='shopping_list.proto',
  package='shopping_list',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x13shopping_list.proto\x12\rshopping_list\"=\n\x0cShoppingList\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\"F\n\x04Item\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x0f\n\x07\x63hecked\x18\x04 \x01(\x08\"O\n\x19\x43reateShoppingListRequest\x12\x32\n\rshopping_list\x18\x01 \x01(\x0b\x32\x1b.shopping_list.ShoppingList\"O\n\x19UpdateShoppingListRequest\x12\x32\n\rshopping_list\x18\x01 \x01(\x0b\x32\x1b.shopping_list.ShoppingList\"5\n\x19\x44\x65leteShoppingListRequest\x12\x18\n\x10shopping_list_id\x18\x01 \x01(\t\"*\n\x18ListShoppingListsRequest\x12\x0e\n\x06\x66ilter\x18\x01 \x01(\t\"0\n\x1eListShoppingListsStreamRequest\x12\x0e\n\x06\x66ilter\x18\x01 \x01(\t\"M\n\x0e\x41\x64\x64ItemRequest\x12\x18\n\x10shopping_list_id\x18\x01 \x01(\t\x12!\n\x04item\x18\x02 \x01(\x0b\x32\x13.shopping_list.Item\">\n\x11RemoveItemRequest\x12\x18\n\x10shopping_list_id\x18\x01 \x01(\t\x12\x0f\n\x07item_id\x18\x02 \x01(\t\"S\n\x15SetItemCheckedRequest\x12\x18\n\x10shopping_list_id\x18\x01 \x01(\t\x12\x0f\n\x07item_id\x18\x02 \x01(\t\x12\x0f\n\x07\x63hecked\x18\x03 \x01(\x08\"<\n\x10ListItemsRequest\x12\x18\n\x10shopping_list_id\x18\x01 \x01(\t\x12\x0e\n\x06\x66ilter\x18\x02 \x01(\t\"B\n\x16ListItemsStreamRequest\x12\x18\n\x10shopping_list_id\x18\x01 \x01(\t\x12\x0e\n\x06\x66ilter\x18\x02 \x01(\t\"P\n\x1a\x44\x65leteShoppingListResponse\x12\x32\n\rshopping_list\x18\x01 \x01(\x0b\x32\x1b.shopping_list.ShoppingList\"P\n\x19ListShoppingListsResponse\x12\x33\n\x0eshopping_lists\x18\x01 \x03(\x0b\x32\x1b.shopping_list.ShoppingList\"4\n\x0f\x41\x64\x64ItemResponse\x12!\n\x04item\x18\x01 \x01(\x0b\x32\x13.shopping_list.Item\"7\n\x12RemoveItemResponse\x12!\n\x04item\x18\x01 \x01(\x0b\x32\x13.shopping_list.Item\";\n\x16SetItemCheckedResponse\x12!\n\x04item\x18\x01 \x01(\x0b\x32\x13.shopping_list.Item\"7\n\x11ListItemsResponse\x12\"\n\x05items\x18\x01 \x03(\x0b\x32\x13.shopping_list.Item2\xbc\x07\n\x13ShoppingListService\x12]\n\x12\x43reateShoppingList\x12(.shopping_list.CreateShoppingListRequest\x1a\x1b.shopping_list.ShoppingList\"\x00\x12]\n\x12UpdateShoppingList\x12(.shopping_list.UpdateShoppingListRequest\x1a\x1b.shopping_list.ShoppingList\"\x00\x12k\n\x12\x44\x65leteShoppingList\x12(.shopping_list.DeleteShoppingListRequest\x1a).shopping_list.DeleteShoppingListResponse\"\x00\x12h\n\x11ListShoppingLists\x12\'.shopping_list.ListShoppingListsRequest\x1a(.shopping_list.ListShoppingListsResponse\"\x00\x12i\n\x17ListShoppingListsStream\x12-.shopping_list.ListShoppingListsStreamRequest\x1a\x1b.shopping_list.ShoppingList\"\x00\x30\x01\x12J\n\x07\x41\x64\x64Item\x12\x1d.shopping_list.AddItemRequest\x1a\x1e.shopping_list.AddItemResponse\"\x00\x12S\n\nRemoveItem\x12 .shopping_list.RemoveItemRequest\x1a!.shopping_list.RemoveItemResponse\"\x00\x12_\n\x0eSetItemChecked\x12$.shopping_list.SetItemCheckedRequest\x1a%.shopping_list.SetItemCheckedResponse\"\x00\x12P\n\tListItems\x12\x1f.shopping_list.ListItemsRequest\x1a .shopping_list.ListItemsResponse\"\x00\x12Q\n\x0fListItemsStream\x12%.shopping_list.ListItemsStreamRequest\x1a\x13.shopping_list.Item\"\x00\x30\x01\x62\x06proto3')
)




_SHOPPINGLIST = _descriptor.Descriptor(
  name='ShoppingList',
  full_name='shopping_list.ShoppingList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='shopping_list.ShoppingList.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='shopping_list.ShoppingList.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='shopping_list.ShoppingList.description', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=38,
  serialized_end=99,
)


_ITEM = _descriptor.Descriptor(
  name='Item',
  full_name='shopping_list.Item',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='shopping_list.Item.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='shopping_list.Item.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='shopping_list.Item.description', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='checked', full_name='shopping_list.Item.checked', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=101,
  serialized_end=171,
)


_CREATESHOPPINGLISTREQUEST = _descriptor.Descriptor(
  name='CreateShoppingListRequest',
  full_name='shopping_list.CreateShoppingListRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='shopping_list', full_name='shopping_list.CreateShoppingListRequest.shopping_list', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=173,
  serialized_end=252,
)


_UPDATESHOPPINGLISTREQUEST = _descriptor.Descriptor(
  name='UpdateShoppingListRequest',
  full_name='shopping_list.UpdateShoppingListRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='shopping_list', full_name='shopping_list.UpdateShoppingListRequest.shopping_list', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=254,
  serialized_end=333,
)


_DELETESHOPPINGLISTREQUEST = _descriptor.Descriptor(
  name='DeleteShoppingListRequest',
  full_name='shopping_list.DeleteShoppingListRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='shopping_list_id', full_name='shopping_list.DeleteShoppingListRequest.shopping_list_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=335,
  serialized_end=388,
)


_LISTSHOPPINGLISTSREQUEST = _descriptor.Descriptor(
  name='ListShoppingListsRequest',
  full_name='shopping_list.ListShoppingListsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='filter', full_name='shopping_list.ListShoppingListsRequest.filter', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=390,
  serialized_end=432,
)


_LISTSHOPPINGLISTSSTREAMREQUEST = _descriptor.Descriptor(
  name='ListShoppingListsStreamRequest',
  full_name='shopping_list.ListShoppingListsStreamRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='filter', full_name='shopping_list.ListShoppingListsStreamRequest.filter', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=434,
  serialized_end=482,
)


_ADDITEMREQUEST = _descriptor.Descriptor(
  name='AddItemRequest',
  full_name='shopping_list.AddItemRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='shopping_list_id', full_name='shopping_list.AddItemRequest.shopping_list_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='item', full_name='shopping_list.AddItemRequest.item', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=484,
  serialized_end=561,
)


_REMOVEITEMREQUEST = _descriptor.Descriptor(
  name='RemoveItemRequest',
  full_name='shopping_list.RemoveItemRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='shopping_list_id', full_name='shopping_list.RemoveItemRequest.shopping_list_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='item_id', full_name='shopping_list.RemoveItemRequest.item_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=563,
  serialized_end=625,
)


_SETITEMCHECKEDREQUEST = _descriptor.Descriptor(
  name='SetItemCheckedRequest',
  full_name='shopping_list.SetItemCheckedRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='shopping_list_id', full_name='shopping_list.SetItemCheckedRequest.shopping_list_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='item_id', full_name='shopping_list.SetItemCheckedRequest.item_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='checked', full_name='shopping_list.SetItemCheckedRequest.checked', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=627,
  serialized_end=710,
)


_LISTITEMSREQUEST = _descriptor.Descriptor(
  name='ListItemsRequest',
  full_name='shopping_list.ListItemsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='shopping_list_id', full_name='shopping_list.ListItemsRequest.shopping_list_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='filter', full_name='shopping_list.ListItemsRequest.filter', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=712,
  serialized_end=772,
)


_LISTITEMSSTREAMREQUEST = _descriptor.Descriptor(
  name='ListItemsStreamRequest',
  full_name='shopping_list.ListItemsStreamRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='shopping_list_id', full_name='shopping_list.ListItemsStreamRequest.shopping_list_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='filter', full_name='shopping_list.ListItemsStreamRequest.filter', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=774,
  serialized_end=840,
)


_DELETESHOPPINGLISTRESPONSE = _descriptor.Descriptor(
  name='DeleteShoppingListResponse',
  full_name='shopping_list.DeleteShoppingListResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='shopping_list', full_name='shopping_list.DeleteShoppingListResponse.shopping_list', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=842,
  serialized_end=922,
)


_LISTSHOPPINGLISTSRESPONSE = _descriptor.Descriptor(
  name='ListShoppingListsResponse',
  full_name='shopping_list.ListShoppingListsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='shopping_lists', full_name='shopping_list.ListShoppingListsResponse.shopping_lists', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=924,
  serialized_end=1004,
)


_ADDITEMRESPONSE = _descriptor.Descriptor(
  name='AddItemResponse',
  full_name='shopping_list.AddItemResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='item', full_name='shopping_list.AddItemResponse.item', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1006,
  serialized_end=1058,
)


_REMOVEITEMRESPONSE = _descriptor.Descriptor(
  name='RemoveItemResponse',
  full_name='shopping_list.RemoveItemResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='item', full_name='shopping_list.RemoveItemResponse.item', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1060,
  serialized_end=1115,
)


_SETITEMCHECKEDRESPONSE = _descriptor.Descriptor(
  name='SetItemCheckedResponse',
  full_name='shopping_list.SetItemCheckedResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='item', full_name='shopping_list.SetItemCheckedResponse.item', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1117,
  serialized_end=1176,
)


_LISTITEMSRESPONSE = _descriptor.Descriptor(
  name='ListItemsResponse',
  full_name='shopping_list.ListItemsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='items', full_name='shopping_list.ListItemsResponse.items', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1178,
  serialized_end=1233,
)

_CREATESHOPPINGLISTREQUEST.fields_by_name['shopping_list'].message_type = _SHOPPINGLIST
_UPDATESHOPPINGLISTREQUEST.fields_by_name['shopping_list'].message_type = _SHOPPINGLIST
_ADDITEMREQUEST.fields_by_name['item'].message_type = _ITEM
_DELETESHOPPINGLISTRESPONSE.fields_by_name['shopping_list'].message_type = _SHOPPINGLIST
_LISTSHOPPINGLISTSRESPONSE.fields_by_name['shopping_lists'].message_type = _SHOPPINGLIST
_ADDITEMRESPONSE.fields_by_name['item'].message_type = _ITEM
_REMOVEITEMRESPONSE.fields_by_name['item'].message_type = _ITEM
_SETITEMCHECKEDRESPONSE.fields_by_name['item'].message_type = _ITEM
_LISTITEMSRESPONSE.fields_by_name['items'].message_type = _ITEM
DESCRIPTOR.message_types_by_name['ShoppingList'] = _SHOPPINGLIST
DESCRIPTOR.message_types_by_name['Item'] = _ITEM
DESCRIPTOR.message_types_by_name['CreateShoppingListRequest'] = _CREATESHOPPINGLISTREQUEST
DESCRIPTOR.message_types_by_name['UpdateShoppingListRequest'] = _UPDATESHOPPINGLISTREQUEST
DESCRIPTOR.message_types_by_name['DeleteShoppingListRequest'] = _DELETESHOPPINGLISTREQUEST
DESCRIPTOR.message_types_by_name['ListShoppingListsRequest'] = _LISTSHOPPINGLISTSREQUEST
DESCRIPTOR.message_types_by_name['ListShoppingListsStreamRequest'] = _LISTSHOPPINGLISTSSTREAMREQUEST
DESCRIPTOR.message_types_by_name['AddItemRequest'] = _ADDITEMREQUEST
DESCRIPTOR.message_types_by_name['RemoveItemRequest'] = _REMOVEITEMREQUEST
DESCRIPTOR.message_types_by_name['SetItemCheckedRequest'] = _SETITEMCHECKEDREQUEST
DESCRIPTOR.message_types_by_name['ListItemsRequest'] = _LISTITEMSREQUEST
DESCRIPTOR.message_types_by_name['ListItemsStreamRequest'] = _LISTITEMSSTREAMREQUEST
DESCRIPTOR.message_types_by_name['DeleteShoppingListResponse'] = _DELETESHOPPINGLISTRESPONSE
DESCRIPTOR.message_types_by_name['ListShoppingListsResponse'] = _LISTSHOPPINGLISTSRESPONSE
DESCRIPTOR.message_types_by_name['AddItemResponse'] = _ADDITEMRESPONSE
DESCRIPTOR.message_types_by_name['RemoveItemResponse'] = _REMOVEITEMRESPONSE
DESCRIPTOR.message_types_by_name['SetItemCheckedResponse'] = _SETITEMCHECKEDRESPONSE
DESCRIPTOR.message_types_by_name['ListItemsResponse'] = _LISTITEMSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ShoppingList = _reflection.GeneratedProtocolMessageType('ShoppingList', (_message.Message,), dict(
  DESCRIPTOR = _SHOPPINGLIST,
  __module__ = 'shopping_list_pb2'
  # @@protoc_insertion_point(class_scope:shopping_list.ShoppingList)
  ))
_sym_db.RegisterMessage(ShoppingList)

Item = _reflection.GeneratedProtocolMessageType('Item', (_message.Message,), dict(
  DESCRIPTOR = _ITEM,
  __module__ = 'shopping_list_pb2'
  # @@protoc_insertion_point(class_scope:shopping_list.Item)
  ))
_sym_db.RegisterMessage(Item)

CreateShoppingListRequest = _reflection.GeneratedProtocolMessageType('CreateShoppingListRequest', (_message.Message,), dict(
  DESCRIPTOR = _CREATESHOPPINGLISTREQUEST,
  __module__ = 'shopping_list_pb2'
  # @@protoc_insertion_point(class_scope:shopping_list.CreateShoppingListRequest)
  ))
_sym_db.RegisterMessage(CreateShoppingListRequest)

UpdateShoppingListRequest = _reflection.GeneratedProtocolMessageType('UpdateShoppingListRequest', (_message.Message,), dict(
  DESCRIPTOR = _UPDATESHOPPINGLISTREQUEST,
  __module__ = 'shopping_list_pb2'
  # @@protoc_insertion_point(class_scope:shopping_list.UpdateShoppingListRequest)
  ))
_sym_db.RegisterMessage(UpdateShoppingListRequest)

DeleteShoppingListRequest = _reflection.GeneratedProtocolMessageType('DeleteShoppingListRequest', (_message.Message,), dict(
  DESCRIPTOR = _DELETESHOPPINGLISTREQUEST,
  __module__ = 'shopping_list_pb2'
  # @@protoc_insertion_point(class_scope:shopping_list.DeleteShoppingListRequest)
  ))
_sym_db.RegisterMessage(DeleteShoppingListRequest)

ListShoppingListsRequest = _reflection.GeneratedProtocolMessageType('ListShoppingListsRequest', (_message.Message,), dict(
  DESCRIPTOR = _LISTSHOPPINGLISTSREQUEST,
  __module__ = 'shopping_list_pb2'
  # @@protoc_insertion_point(class_scope:shopping_list.ListShoppingListsRequest)
  ))
_sym_db.RegisterMessage(ListShoppingListsRequest)

ListShoppingListsStreamRequest = _reflection.GeneratedProtocolMessageType('ListShoppingListsStreamRequest', (_message.Message,), dict(
  DESCRIPTOR = _LISTSHOPPINGLISTSSTREAMREQUEST,
  __module__ = 'shopping_list_pb2'
  # @@protoc_insertion_point(class_scope:shopping_list.ListShoppingListsStreamRequest)
  ))
_sym_db.RegisterMessage(ListShoppingListsStreamRequest)

AddItemRequest = _reflection.GeneratedProtocolMessageType('AddItemRequest', (_message.Message,), dict(
  DESCRIPTOR = _ADDITEMREQUEST,
  __module__ = 'shopping_list_pb2'
  # @@protoc_insertion_point(class_scope:shopping_list.AddItemRequest)
  ))
_sym_db.RegisterMessage(AddItemRequest)

RemoveItemRequest = _reflection.GeneratedProtocolMessageType('RemoveItemRequest', (_message.Message,), dict(
  DESCRIPTOR = _REMOVEITEMREQUEST,
  __module__ = 'shopping_list_pb2'
  # @@protoc_insertion_point(class_scope:shopping_list.RemoveItemRequest)
  ))
_sym_db.RegisterMessage(RemoveItemRequest)

SetItemCheckedRequest = _reflection.GeneratedProtocolMessageType('SetItemCheckedRequest', (_message.Message,), dict(
  DESCRIPTOR = _SETITEMCHECKEDREQUEST,
  __module__ = 'shopping_list_pb2'
  # @@protoc_insertion_point(class_scope:shopping_list.SetItemCheckedRequest)
  ))
_sym_db.RegisterMessage(SetItemCheckedRequest)

ListItemsRequest = _reflection.GeneratedProtocolMessageType('ListItemsRequest', (_message.Message,), dict(
  DESCRIPTOR = _LISTITEMSREQUEST,
  __module__ = 'shopping_list_pb2'
  # @@protoc_insertion_point(class_scope:shopping_list.ListItemsRequest)
  ))
_sym_db.RegisterMessage(ListItemsRequest)

ListItemsStreamRequest = _reflection.GeneratedProtocolMessageType('ListItemsStreamRequest', (_message.Message,), dict(
  DESCRIPTOR = _LISTITEMSSTREAMREQUEST,
  __module__ = 'shopping_list_pb2'
  # @@protoc_insertion_point(class_scope:shopping_list.ListItemsStreamRequest)
  ))
_sym_db.RegisterMessage(ListItemsStreamRequest)

DeleteShoppingListResponse = _reflection.GeneratedProtocolMessageType('DeleteShoppingListResponse', (_message.Message,), dict(
  DESCRIPTOR = _DELETESHOPPINGLISTRESPONSE,
  __module__ = 'shopping_list_pb2'
  # @@protoc_insertion_point(class_scope:shopping_list.DeleteShoppingListResponse)
  ))
_sym_db.RegisterMessage(DeleteShoppingListResponse)

ListShoppingListsResponse = _reflection.GeneratedProtocolMessageType('ListShoppingListsResponse', (_message.Message,), dict(
  DESCRIPTOR = _LISTSHOPPINGLISTSRESPONSE,
  __module__ = 'shopping_list_pb2'
  # @@protoc_insertion_point(class_scope:shopping_list.ListShoppingListsResponse)
  ))
_sym_db.RegisterMessage(ListShoppingListsResponse)

AddItemResponse = _reflection.GeneratedProtocolMessageType('AddItemResponse', (_message.Message,), dict(
  DESCRIPTOR = _ADDITEMRESPONSE,
  __module__ = 'shopping_list_pb2'
  # @@protoc_insertion_point(class_scope:shopping_list.AddItemResponse)
  ))
_sym_db.RegisterMessage(AddItemResponse)

RemoveItemResponse = _reflection.GeneratedProtocolMessageType('RemoveItemResponse', (_message.Message,), dict(
  DESCRIPTOR = _REMOVEITEMRESPONSE,
  __module__ = 'shopping_list_pb2'
  # @@protoc_insertion_point(class_scope:shopping_list.RemoveItemResponse)
  ))
_sym_db.RegisterMessage(RemoveItemResponse)

SetItemCheckedResponse = _reflection.GeneratedProtocolMessageType('SetItemCheckedResponse', (_message.Message,), dict(
  DESCRIPTOR = _SETITEMCHECKEDRESPONSE,
  __module__ = 'shopping_list_pb2'
  # @@protoc_insertion_point(class_scope:shopping_list.SetItemCheckedResponse)
  ))
_sym_db.RegisterMessage(SetItemCheckedResponse)

ListItemsResponse = _reflection.GeneratedProtocolMessageType('ListItemsResponse', (_message.Message,), dict(
  DESCRIPTOR = _LISTITEMSRESPONSE,
  __module__ = 'shopping_list_pb2'
  # @@protoc_insertion_point(class_scope:shopping_list.ListItemsResponse)
  ))
_sym_db.RegisterMessage(ListItemsResponse)



_SHOPPINGLISTSERVICE = _descriptor.ServiceDescriptor(
  name='ShoppingListService',
  full_name='shopping_list.ShoppingListService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1236,
  serialized_end=2192,
  methods=[
  _descriptor.MethodDescriptor(
    name='CreateShoppingList',
    full_name='shopping_list.ShoppingListService.CreateShoppingList',
    index=0,
    containing_service=None,
    input_type=_CREATESHOPPINGLISTREQUEST,
    output_type=_SHOPPINGLIST,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateShoppingList',
    full_name='shopping_list.ShoppingListService.UpdateShoppingList',
    index=1,
    containing_service=None,
    input_type=_UPDATESHOPPINGLISTREQUEST,
    output_type=_SHOPPINGLIST,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteShoppingList',
    full_name='shopping_list.ShoppingListService.DeleteShoppingList',
    index=2,
    containing_service=None,
    input_type=_DELETESHOPPINGLISTREQUEST,
    output_type=_DELETESHOPPINGLISTRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ListShoppingLists',
    full_name='shopping_list.ShoppingListService.ListShoppingLists',
    index=3,
    containing_service=None,
    input_type=_LISTSHOPPINGLISTSREQUEST,
    output_type=_LISTSHOPPINGLISTSRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ListShoppingListsStream',
    full_name='shopping_list.ShoppingListService.ListShoppingListsStream',
    index=4,
    containing_service=None,
    input_type=_LISTSHOPPINGLISTSSTREAMREQUEST,
    output_type=_SHOPPINGLIST,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='AddItem',
    full_name='shopping_list.ShoppingListService.AddItem',
    index=5,
    containing_service=None,
    input_type=_ADDITEMREQUEST,
    output_type=_ADDITEMRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='RemoveItem',
    full_name='shopping_list.ShoppingListService.RemoveItem',
    index=6,
    containing_service=None,
    input_type=_REMOVEITEMREQUEST,
    output_type=_REMOVEITEMRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SetItemChecked',
    full_name='shopping_list.ShoppingListService.SetItemChecked',
    index=7,
    containing_service=None,
    input_type=_SETITEMCHECKEDREQUEST,
    output_type=_SETITEMCHECKEDRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ListItems',
    full_name='shopping_list.ShoppingListService.ListItems',
    index=8,
    containing_service=None,
    input_type=_LISTITEMSREQUEST,
    output_type=_LISTITEMSRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ListItemsStream',
    full_name='shopping_list.ShoppingListService.ListItemsStream',
    index=9,
    containing_service=None,
    input_type=_LISTITEMSSTREAMREQUEST,
    output_type=_ITEM,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_SHOPPINGLISTSERVICE)

DESCRIPTOR.services_by_name['ShoppingListService'] = _SHOPPINGLISTSERVICE

# @@protoc_insertion_point(module_scope)
