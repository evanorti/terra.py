# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/authz/v1beta1/event.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name="cosmos/authz/v1beta1/event.proto",
    package="cosmos.authz.v1beta1",
    syntax="proto3",
    serialized_options=b"Z$github.com/cosmos/cosmos-sdk/x/authz",
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n cosmos/authz/v1beta1/event.proto\x12\x14\x63osmos.authz.v1beta1"D\n\nEventGrant\x12\x14\n\x0cmsg_type_url\x18\x02 \x01(\t\x12\x0f\n\x07granter\x18\x03 \x01(\t\x12\x0f\n\x07grantee\x18\x04 \x01(\t"E\n\x0b\x45ventRevoke\x12\x14\n\x0cmsg_type_url\x18\x02 \x01(\t\x12\x0f\n\x07granter\x18\x03 \x01(\t\x12\x0f\n\x07grantee\x18\x04 \x01(\tB&Z$github.com/cosmos/cosmos-sdk/x/authzb\x06proto3',
)


_EVENTGRANT = _descriptor.Descriptor(
    name="EventGrant",
    full_name="cosmos.authz.v1beta1.EventGrant",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="msg_type_url",
            full_name="cosmos.authz.v1beta1.EventGrant.msg_type_url",
            index=0,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="granter",
            full_name="cosmos.authz.v1beta1.EventGrant.granter",
            index=1,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="grantee",
            full_name="cosmos.authz.v1beta1.EventGrant.grantee",
            index=2,
            number=4,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=58,
    serialized_end=126,
)


_EVENTREVOKE = _descriptor.Descriptor(
    name="EventRevoke",
    full_name="cosmos.authz.v1beta1.EventRevoke",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="msg_type_url",
            full_name="cosmos.authz.v1beta1.EventRevoke.msg_type_url",
            index=0,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="granter",
            full_name="cosmos.authz.v1beta1.EventRevoke.granter",
            index=1,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="grantee",
            full_name="cosmos.authz.v1beta1.EventRevoke.grantee",
            index=2,
            number=4,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=128,
    serialized_end=197,
)

DESCRIPTOR.message_types_by_name["EventGrant"] = _EVENTGRANT
DESCRIPTOR.message_types_by_name["EventRevoke"] = _EVENTREVOKE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EventGrant = _reflection.GeneratedProtocolMessageType(
    "EventGrant",
    (_message.Message,),
    {
        "DESCRIPTOR": _EVENTGRANT,
        "__module__": "cosmos.authz.v1beta1.event_pb2"
        # @@protoc_insertion_point(class_scope:cosmos.authz.v1beta1.EventGrant)
    },
)
_sym_db.RegisterMessage(EventGrant)

EventRevoke = _reflection.GeneratedProtocolMessageType(
    "EventRevoke",
    (_message.Message,),
    {
        "DESCRIPTOR": _EVENTREVOKE,
        "__module__": "cosmos.authz.v1beta1.event_pb2"
        # @@protoc_insertion_point(class_scope:cosmos.authz.v1beta1.EventRevoke)
    },
)
_sym_db.RegisterMessage(EventRevoke)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
