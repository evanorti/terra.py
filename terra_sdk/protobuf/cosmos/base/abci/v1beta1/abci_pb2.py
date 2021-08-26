# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/base/abci/v1beta1/abci.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from tendermint.abci import types_pb2 as tendermint_dot_abci_dot_types__pb2

DESCRIPTOR = _descriptor.FileDescriptor(
    name="cosmos/base/abci/v1beta1/abci.proto",
    package="cosmos.base.abci.v1beta1",
    syntax="proto3",
    serialized_options=b'Z"github.com/cosmos/cosmos-sdk/types\330\341\036\000',
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n#cosmos/base/abci/v1beta1/abci.proto\x12\x18\x63osmos.base.abci.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1btendermint/abci/types.proto\x1a\x19google/protobuf/any.proto"\xb8\x02\n\nTxResponse\x12\x0e\n\x06height\x18\x01 \x01(\x03\x12\x1a\n\x06txhash\x18\x02 \x01(\tB\n\xe2\xde\x1f\x06TxHash\x12\x11\n\tcodespace\x18\x03 \x01(\t\x12\x0c\n\x04\x63ode\x18\x04 \x01(\r\x12\x0c\n\x04\x64\x61ta\x18\x05 \x01(\t\x12\x0f\n\x07raw_log\x18\x06 \x01(\t\x12O\n\x04logs\x18\x07 \x03(\x0b\x32(.cosmos.base.abci.v1beta1.ABCIMessageLogB\x17\xaa\xdf\x1f\x0f\x41\x42\x43IMessageLogs\xc8\xde\x1f\x00\x12\x0c\n\x04info\x18\x08 \x01(\t\x12\x12\n\ngas_wanted\x18\t \x01(\x03\x12\x10\n\x08gas_used\x18\n \x01(\x03\x12 \n\x02tx\x18\x0b \x01(\x0b\x32\x14.google.protobuf.Any\x12\x11\n\ttimestamp\x18\x0c \x01(\t:\x04\x88\xa0\x1f\x00"\x83\x01\n\x0e\x41\x42\x43IMessageLog\x12\x11\n\tmsg_index\x18\x01 \x01(\r\x12\x0b\n\x03log\x18\x02 \x01(\t\x12K\n\x06\x65vents\x18\x03 \x03(\x0b\x32%.cosmos.base.abci.v1beta1.StringEventB\x14\xaa\xdf\x1f\x0cStringEvents\xc8\xde\x1f\x00:\x04\x80\xdc \x01"`\n\x0bStringEvent\x12\x0c\n\x04type\x18\x01 \x01(\t\x12=\n\nattributes\x18\x02 \x03(\x0b\x32#.cosmos.base.abci.v1beta1.AttributeB\x04\xc8\xde\x1f\x00:\x04\x80\xdc \x01"\'\n\tAttribute\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t"[\n\x07GasInfo\x12)\n\ngas_wanted\x18\x01 \x01(\x04\x42\x15\xf2\xde\x1f\x11yaml:"gas_wanted"\x12%\n\x08gas_used\x18\x02 \x01(\x04\x42\x13\xf2\xde\x1f\x0fyaml:"gas_used""W\n\x06Result\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\x12\x0b\n\x03log\x18\x02 \x01(\t\x12,\n\x06\x65vents\x18\x03 \x03(\x0b\x32\x16.tendermint.abci.EventB\x04\xc8\xde\x1f\x00:\x04\x88\xa0\x1f\x00"\x85\x01\n\x12SimulationResponse\x12=\n\x08gas_info\x18\x01 \x01(\x0b\x32!.cosmos.base.abci.v1beta1.GasInfoB\x08\xd0\xde\x1f\x01\xc8\xde\x1f\x00\x12\x30\n\x06result\x18\x02 \x01(\x0b\x32 .cosmos.base.abci.v1beta1.Result"/\n\x07MsgData\x12\x10\n\x08msg_type\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c:\x04\x80\xdc \x01"B\n\tTxMsgData\x12/\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32!.cosmos.base.abci.v1beta1.MsgData:\x04\x80\xdc \x01"\x99\x02\n\x0fSearchTxsResult\x12:\n\x0btotal_count\x18\x01 \x01(\x04\x42%\xf2\xde\x1f\x12yaml:"total_count"\xea\xde\x1f\x0btotal_count\x12\r\n\x05\x63ount\x18\x02 \x01(\x04\x12:\n\x0bpage_number\x18\x03 \x01(\x04\x42%\xf2\xde\x1f\x12yaml:"page_number"\xea\xde\x1f\x0bpage_number\x12\x37\n\npage_total\x18\x04 \x01(\x04\x42#\xf2\xde\x1f\x11yaml:"page_total"\xea\xde\x1f\npage_total\x12\r\n\x05limit\x18\x05 \x01(\x04\x12\x31\n\x03txs\x18\x06 \x03(\x0b\x32$.cosmos.base.abci.v1beta1.TxResponse:\x04\x80\xdc \x01\x42(Z"github.com/cosmos/cosmos-sdk/types\xd8\xe1\x1e\x00\x62\x06proto3',
    dependencies=[
        gogoproto_dot_gogo__pb2.DESCRIPTOR,
        tendermint_dot_abci_dot_types__pb2.DESCRIPTOR,
        google_dot_protobuf_dot_any__pb2.DESCRIPTOR,
    ],
)


_TXRESPONSE = _descriptor.Descriptor(
    name="TxResponse",
    full_name="cosmos.base.abci.v1beta1.TxResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="height",
            full_name="cosmos.base.abci.v1beta1.TxResponse.height",
            index=0,
            number=1,
            type=3,
            cpp_type=2,
            label=1,
            has_default_value=False,
            default_value=0,
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
            name="txhash",
            full_name="cosmos.base.abci.v1beta1.TxResponse.txhash",
            index=1,
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
            serialized_options=b"\342\336\037\006TxHash",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="codespace",
            full_name="cosmos.base.abci.v1beta1.TxResponse.codespace",
            index=2,
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
            name="code",
            full_name="cosmos.base.abci.v1beta1.TxResponse.code",
            index=3,
            number=4,
            type=13,
            cpp_type=3,
            label=1,
            has_default_value=False,
            default_value=0,
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
            name="data",
            full_name="cosmos.base.abci.v1beta1.TxResponse.data",
            index=4,
            number=5,
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
            name="raw_log",
            full_name="cosmos.base.abci.v1beta1.TxResponse.raw_log",
            index=5,
            number=6,
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
            name="logs",
            full_name="cosmos.base.abci.v1beta1.TxResponse.logs",
            index=6,
            number=7,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\252\337\037\017ABCIMessageLogs\310\336\037\000",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="info",
            full_name="cosmos.base.abci.v1beta1.TxResponse.info",
            index=7,
            number=8,
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
            name="gas_wanted",
            full_name="cosmos.base.abci.v1beta1.TxResponse.gas_wanted",
            index=8,
            number=9,
            type=3,
            cpp_type=2,
            label=1,
            has_default_value=False,
            default_value=0,
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
            name="gas_used",
            full_name="cosmos.base.abci.v1beta1.TxResponse.gas_used",
            index=9,
            number=10,
            type=3,
            cpp_type=2,
            label=1,
            has_default_value=False,
            default_value=0,
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
            name="tx",
            full_name="cosmos.base.abci.v1beta1.TxResponse.tx",
            index=10,
            number=11,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
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
            name="timestamp",
            full_name="cosmos.base.abci.v1beta1.TxResponse.timestamp",
            index=11,
            number=12,
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
    serialized_options=b"\210\240\037\000",
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=144,
    serialized_end=456,
)


_ABCIMESSAGELOG = _descriptor.Descriptor(
    name="ABCIMessageLog",
    full_name="cosmos.base.abci.v1beta1.ABCIMessageLog",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="msg_index",
            full_name="cosmos.base.abci.v1beta1.ABCIMessageLog.msg_index",
            index=0,
            number=1,
            type=13,
            cpp_type=3,
            label=1,
            has_default_value=False,
            default_value=0,
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
            name="log",
            full_name="cosmos.base.abci.v1beta1.ABCIMessageLog.log",
            index=1,
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
            name="events",
            full_name="cosmos.base.abci.v1beta1.ABCIMessageLog.events",
            index=2,
            number=3,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\252\337\037\014StringEvents\310\336\037\000",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=b"\200\334 \001",
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=459,
    serialized_end=590,
)


_STRINGEVENT = _descriptor.Descriptor(
    name="StringEvent",
    full_name="cosmos.base.abci.v1beta1.StringEvent",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="type",
            full_name="cosmos.base.abci.v1beta1.StringEvent.type",
            index=0,
            number=1,
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
            name="attributes",
            full_name="cosmos.base.abci.v1beta1.StringEvent.attributes",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\310\336\037\000",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=b"\200\334 \001",
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=592,
    serialized_end=688,
)


_ATTRIBUTE = _descriptor.Descriptor(
    name="Attribute",
    full_name="cosmos.base.abci.v1beta1.Attribute",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="key",
            full_name="cosmos.base.abci.v1beta1.Attribute.key",
            index=0,
            number=1,
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
            name="value",
            full_name="cosmos.base.abci.v1beta1.Attribute.value",
            index=1,
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
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=690,
    serialized_end=729,
)


_GASINFO = _descriptor.Descriptor(
    name="GasInfo",
    full_name="cosmos.base.abci.v1beta1.GasInfo",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="gas_wanted",
            full_name="cosmos.base.abci.v1beta1.GasInfo.gas_wanted",
            index=0,
            number=1,
            type=4,
            cpp_type=4,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b'\362\336\037\021yaml:"gas_wanted"',
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="gas_used",
            full_name="cosmos.base.abci.v1beta1.GasInfo.gas_used",
            index=1,
            number=2,
            type=4,
            cpp_type=4,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b'\362\336\037\017yaml:"gas_used"',
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
    serialized_start=731,
    serialized_end=822,
)


_RESULT = _descriptor.Descriptor(
    name="Result",
    full_name="cosmos.base.abci.v1beta1.Result",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="data",
            full_name="cosmos.base.abci.v1beta1.Result.data",
            index=0,
            number=1,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"",
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
            name="log",
            full_name="cosmos.base.abci.v1beta1.Result.log",
            index=1,
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
            name="events",
            full_name="cosmos.base.abci.v1beta1.Result.events",
            index=2,
            number=3,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\310\336\037\000",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=b"\210\240\037\000",
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=824,
    serialized_end=911,
)


_SIMULATIONRESPONSE = _descriptor.Descriptor(
    name="SimulationResponse",
    full_name="cosmos.base.abci.v1beta1.SimulationResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="gas_info",
            full_name="cosmos.base.abci.v1beta1.SimulationResponse.gas_info",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\320\336\037\001\310\336\037\000",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="result",
            full_name="cosmos.base.abci.v1beta1.SimulationResponse.result",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
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
    serialized_start=914,
    serialized_end=1047,
)


_MSGDATA = _descriptor.Descriptor(
    name="MsgData",
    full_name="cosmos.base.abci.v1beta1.MsgData",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="msg_type",
            full_name="cosmos.base.abci.v1beta1.MsgData.msg_type",
            index=0,
            number=1,
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
            name="data",
            full_name="cosmos.base.abci.v1beta1.MsgData.data",
            index=1,
            number=2,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"",
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
    serialized_options=b"\200\334 \001",
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=1049,
    serialized_end=1096,
)


_TXMSGDATA = _descriptor.Descriptor(
    name="TxMsgData",
    full_name="cosmos.base.abci.v1beta1.TxMsgData",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="data",
            full_name="cosmos.base.abci.v1beta1.TxMsgData.data",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
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
    serialized_options=b"\200\334 \001",
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=1098,
    serialized_end=1164,
)


_SEARCHTXSRESULT = _descriptor.Descriptor(
    name="SearchTxsResult",
    full_name="cosmos.base.abci.v1beta1.SearchTxsResult",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="total_count",
            full_name="cosmos.base.abci.v1beta1.SearchTxsResult.total_count",
            index=0,
            number=1,
            type=4,
            cpp_type=4,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b'\362\336\037\022yaml:"total_count"\352\336\037\013total_count',
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="count",
            full_name="cosmos.base.abci.v1beta1.SearchTxsResult.count",
            index=1,
            number=2,
            type=4,
            cpp_type=4,
            label=1,
            has_default_value=False,
            default_value=0,
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
            name="page_number",
            full_name="cosmos.base.abci.v1beta1.SearchTxsResult.page_number",
            index=2,
            number=3,
            type=4,
            cpp_type=4,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b'\362\336\037\022yaml:"page_number"\352\336\037\013page_number',
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="page_total",
            full_name="cosmos.base.abci.v1beta1.SearchTxsResult.page_total",
            index=3,
            number=4,
            type=4,
            cpp_type=4,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b'\362\336\037\021yaml:"page_total"\352\336\037\npage_total',
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="limit",
            full_name="cosmos.base.abci.v1beta1.SearchTxsResult.limit",
            index=4,
            number=5,
            type=4,
            cpp_type=4,
            label=1,
            has_default_value=False,
            default_value=0,
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
            name="txs",
            full_name="cosmos.base.abci.v1beta1.SearchTxsResult.txs",
            index=5,
            number=6,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
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
    serialized_options=b"\200\334 \001",
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=1167,
    serialized_end=1448,
)

_TXRESPONSE.fields_by_name["logs"].message_type = _ABCIMESSAGELOG
_TXRESPONSE.fields_by_name["tx"].message_type = google_dot_protobuf_dot_any__pb2._ANY
_ABCIMESSAGELOG.fields_by_name["events"].message_type = _STRINGEVENT
_STRINGEVENT.fields_by_name["attributes"].message_type = _ATTRIBUTE
_RESULT.fields_by_name[
    "events"
].message_type = tendermint_dot_abci_dot_types__pb2._EVENT
_SIMULATIONRESPONSE.fields_by_name["gas_info"].message_type = _GASINFO
_SIMULATIONRESPONSE.fields_by_name["result"].message_type = _RESULT
_TXMSGDATA.fields_by_name["data"].message_type = _MSGDATA
_SEARCHTXSRESULT.fields_by_name["txs"].message_type = _TXRESPONSE
DESCRIPTOR.message_types_by_name["TxResponse"] = _TXRESPONSE
DESCRIPTOR.message_types_by_name["ABCIMessageLog"] = _ABCIMESSAGELOG
DESCRIPTOR.message_types_by_name["StringEvent"] = _STRINGEVENT
DESCRIPTOR.message_types_by_name["Attribute"] = _ATTRIBUTE
DESCRIPTOR.message_types_by_name["GasInfo"] = _GASINFO
DESCRIPTOR.message_types_by_name["Result"] = _RESULT
DESCRIPTOR.message_types_by_name["SimulationResponse"] = _SIMULATIONRESPONSE
DESCRIPTOR.message_types_by_name["MsgData"] = _MSGDATA
DESCRIPTOR.message_types_by_name["TxMsgData"] = _TXMSGDATA
DESCRIPTOR.message_types_by_name["SearchTxsResult"] = _SEARCHTXSRESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TxResponse = _reflection.GeneratedProtocolMessageType(
    "TxResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _TXRESPONSE,
        "__module__": "cosmos.base.abci.v1beta1.abci_pb2"
        # @@protoc_insertion_point(class_scope:cosmos.base.abci.v1beta1.TxResponse)
    },
)
_sym_db.RegisterMessage(TxResponse)

ABCIMessageLog = _reflection.GeneratedProtocolMessageType(
    "ABCIMessageLog",
    (_message.Message,),
    {
        "DESCRIPTOR": _ABCIMESSAGELOG,
        "__module__": "cosmos.base.abci.v1beta1.abci_pb2"
        # @@protoc_insertion_point(class_scope:cosmos.base.abci.v1beta1.ABCIMessageLog)
    },
)
_sym_db.RegisterMessage(ABCIMessageLog)

StringEvent = _reflection.GeneratedProtocolMessageType(
    "StringEvent",
    (_message.Message,),
    {
        "DESCRIPTOR": _STRINGEVENT,
        "__module__": "cosmos.base.abci.v1beta1.abci_pb2"
        # @@protoc_insertion_point(class_scope:cosmos.base.abci.v1beta1.StringEvent)
    },
)
_sym_db.RegisterMessage(StringEvent)

Attribute = _reflection.GeneratedProtocolMessageType(
    "Attribute",
    (_message.Message,),
    {
        "DESCRIPTOR": _ATTRIBUTE,
        "__module__": "cosmos.base.abci.v1beta1.abci_pb2"
        # @@protoc_insertion_point(class_scope:cosmos.base.abci.v1beta1.Attribute)
    },
)
_sym_db.RegisterMessage(Attribute)

GasInfo = _reflection.GeneratedProtocolMessageType(
    "GasInfo",
    (_message.Message,),
    {
        "DESCRIPTOR": _GASINFO,
        "__module__": "cosmos.base.abci.v1beta1.abci_pb2"
        # @@protoc_insertion_point(class_scope:cosmos.base.abci.v1beta1.GasInfo)
    },
)
_sym_db.RegisterMessage(GasInfo)

Result = _reflection.GeneratedProtocolMessageType(
    "Result",
    (_message.Message,),
    {
        "DESCRIPTOR": _RESULT,
        "__module__": "cosmos.base.abci.v1beta1.abci_pb2"
        # @@protoc_insertion_point(class_scope:cosmos.base.abci.v1beta1.Result)
    },
)
_sym_db.RegisterMessage(Result)

SimulationResponse = _reflection.GeneratedProtocolMessageType(
    "SimulationResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _SIMULATIONRESPONSE,
        "__module__": "cosmos.base.abci.v1beta1.abci_pb2"
        # @@protoc_insertion_point(class_scope:cosmos.base.abci.v1beta1.SimulationResponse)
    },
)
_sym_db.RegisterMessage(SimulationResponse)

MsgData = _reflection.GeneratedProtocolMessageType(
    "MsgData",
    (_message.Message,),
    {
        "DESCRIPTOR": _MSGDATA,
        "__module__": "cosmos.base.abci.v1beta1.abci_pb2"
        # @@protoc_insertion_point(class_scope:cosmos.base.abci.v1beta1.MsgData)
    },
)
_sym_db.RegisterMessage(MsgData)

TxMsgData = _reflection.GeneratedProtocolMessageType(
    "TxMsgData",
    (_message.Message,),
    {
        "DESCRIPTOR": _TXMSGDATA,
        "__module__": "cosmos.base.abci.v1beta1.abci_pb2"
        # @@protoc_insertion_point(class_scope:cosmos.base.abci.v1beta1.TxMsgData)
    },
)
_sym_db.RegisterMessage(TxMsgData)

SearchTxsResult = _reflection.GeneratedProtocolMessageType(
    "SearchTxsResult",
    (_message.Message,),
    {
        "DESCRIPTOR": _SEARCHTXSRESULT,
        "__module__": "cosmos.base.abci.v1beta1.abci_pb2"
        # @@protoc_insertion_point(class_scope:cosmos.base.abci.v1beta1.SearchTxsResult)
    },
)
_sym_db.RegisterMessage(SearchTxsResult)


DESCRIPTOR._options = None
_TXRESPONSE.fields_by_name["txhash"]._options = None
_TXRESPONSE.fields_by_name["logs"]._options = None
_TXRESPONSE._options = None
_ABCIMESSAGELOG.fields_by_name["events"]._options = None
_ABCIMESSAGELOG._options = None
_STRINGEVENT.fields_by_name["attributes"]._options = None
_STRINGEVENT._options = None
_GASINFO.fields_by_name["gas_wanted"]._options = None
_GASINFO.fields_by_name["gas_used"]._options = None
_RESULT.fields_by_name["events"]._options = None
_RESULT._options = None
_SIMULATIONRESPONSE.fields_by_name["gas_info"]._options = None
_MSGDATA._options = None
_TXMSGDATA._options = None
_SEARCHTXSRESULT.fields_by_name["total_count"]._options = None
_SEARCHTXSRESULT.fields_by_name["page_number"]._options = None
_SEARCHTXSRESULT.fields_by_name["page_total"]._options = None
_SEARCHTXSRESULT._options = None
# @@protoc_insertion_point(module_scope)
