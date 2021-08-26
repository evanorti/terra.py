# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: terra/wasm/v1beta1/genesis.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cosmos.base.v1beta1 import \
    coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from terra.wasm.v1beta1 import \
    wasm_pb2 as terra_dot_wasm_dot_v1beta1_dot_wasm__pb2

DESCRIPTOR = _descriptor.FileDescriptor(
    name="terra/wasm/v1beta1/genesis.proto",
    package="terra.wasm.v1beta1",
    syntax="proto3",
    serialized_options=b"Z(github.com/terra-money/core/x/wasm/types",
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n terra/wasm/v1beta1/genesis.proto\x12\x12terra.wasm.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1dterra/wasm/v1beta1/wasm.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto"\xfa\x01\n\x0cGenesisState\x12\x30\n\x06params\x18\x01 \x01(\x0b\x32\x1a.terra.wasm.v1beta1.ParamsB\x04\xc8\xde\x1f\x00\x12$\n\x0clast_code_id\x18\x02 \x01(\x04\x42\x0e\xe2\xde\x1f\nLastCodeID\x12,\n\x10last_instance_id\x18\x03 \x01(\x04\x42\x12\xe2\xde\x1f\x0eLastInstanceID\x12-\n\x05\x63odes\x18\x04 \x03(\x0b\x32\x18.terra.wasm.v1beta1.CodeB\x04\xc8\xde\x1f\x00\x12\x35\n\tcontracts\x18\x05 \x03(\x0b\x32\x1c.terra.wasm.v1beta1.ContractB\x04\xc8\xde\x1f\x00"#\n\x05Model\x12\x0b\n\x03key\x18\x01 \x01(\x0c\x12\r\n\x05value\x18\x02 \x01(\x0c"Q\n\x04\x43ode\x12\x35\n\tcode_info\x18\x01 \x01(\x0b\x32\x1c.terra.wasm.v1beta1.CodeInfoB\x04\xc8\xde\x1f\x00\x12\x12\n\ncode_bytes\x18\x02 \x01(\x0c"\x82\x01\n\x08\x43ontract\x12=\n\rcontract_info\x18\x01 \x01(\x0b\x32 .terra.wasm.v1beta1.ContractInfoB\x04\xc8\xde\x1f\x00\x12\x37\n\x0e\x63ontract_store\x18\x02 \x03(\x0b\x32\x19.terra.wasm.v1beta1.ModelB\x04\xc8\xde\x1f\x00\x42*Z(github.com/terra-money/core/x/wasm/typesb\x06proto3',
    dependencies=[
        gogoproto_dot_gogo__pb2.DESCRIPTOR,
        terra_dot_wasm_dot_v1beta1_dot_wasm__pb2.DESCRIPTOR,
        cosmos_dot_base_dot_v1beta1_dot_coin__pb2.DESCRIPTOR,
    ],
)


_GENESISSTATE = _descriptor.Descriptor(
    name="GenesisState",
    full_name="terra.wasm.v1beta1.GenesisState",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="params",
            full_name="terra.wasm.v1beta1.GenesisState.params",
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
            serialized_options=b"\310\336\037\000",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="last_code_id",
            full_name="terra.wasm.v1beta1.GenesisState.last_code_id",
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
            serialized_options=b"\342\336\037\nLastCodeID",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="last_instance_id",
            full_name="terra.wasm.v1beta1.GenesisState.last_instance_id",
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
            serialized_options=b"\342\336\037\016LastInstanceID",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="codes",
            full_name="terra.wasm.v1beta1.GenesisState.codes",
            index=3,
            number=4,
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
        _descriptor.FieldDescriptor(
            name="contracts",
            full_name="terra.wasm.v1beta1.GenesisState.contracts",
            index=4,
            number=5,
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
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=142,
    serialized_end=392,
)


_MODEL = _descriptor.Descriptor(
    name="Model",
    full_name="terra.wasm.v1beta1.Model",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="key",
            full_name="terra.wasm.v1beta1.Model.key",
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
            name="value",
            full_name="terra.wasm.v1beta1.Model.value",
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
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=394,
    serialized_end=429,
)


_CODE = _descriptor.Descriptor(
    name="Code",
    full_name="terra.wasm.v1beta1.Code",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="code_info",
            full_name="terra.wasm.v1beta1.Code.code_info",
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
            serialized_options=b"\310\336\037\000",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="code_bytes",
            full_name="terra.wasm.v1beta1.Code.code_bytes",
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
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=431,
    serialized_end=512,
)


_CONTRACT = _descriptor.Descriptor(
    name="Contract",
    full_name="terra.wasm.v1beta1.Contract",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="contract_info",
            full_name="terra.wasm.v1beta1.Contract.contract_info",
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
            serialized_options=b"\310\336\037\000",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="contract_store",
            full_name="terra.wasm.v1beta1.Contract.contract_store",
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
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=515,
    serialized_end=645,
)

_GENESISSTATE.fields_by_name[
    "params"
].message_type = terra_dot_wasm_dot_v1beta1_dot_wasm__pb2._PARAMS
_GENESISSTATE.fields_by_name["codes"].message_type = _CODE
_GENESISSTATE.fields_by_name["contracts"].message_type = _CONTRACT
_CODE.fields_by_name[
    "code_info"
].message_type = terra_dot_wasm_dot_v1beta1_dot_wasm__pb2._CODEINFO
_CONTRACT.fields_by_name[
    "contract_info"
].message_type = terra_dot_wasm_dot_v1beta1_dot_wasm__pb2._CONTRACTINFO
_CONTRACT.fields_by_name["contract_store"].message_type = _MODEL
DESCRIPTOR.message_types_by_name["GenesisState"] = _GENESISSTATE
DESCRIPTOR.message_types_by_name["Model"] = _MODEL
DESCRIPTOR.message_types_by_name["Code"] = _CODE
DESCRIPTOR.message_types_by_name["Contract"] = _CONTRACT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GenesisState = _reflection.GeneratedProtocolMessageType(
    "GenesisState",
    (_message.Message,),
    {
        "DESCRIPTOR": _GENESISSTATE,
        "__module__": "terra.wasm.v1beta1.genesis_pb2"
        # @@protoc_insertion_point(class_scope:terra.wasm.v1beta1.GenesisState)
    },
)
_sym_db.RegisterMessage(GenesisState)

Model = _reflection.GeneratedProtocolMessageType(
    "Model",
    (_message.Message,),
    {
        "DESCRIPTOR": _MODEL,
        "__module__": "terra.wasm.v1beta1.genesis_pb2"
        # @@protoc_insertion_point(class_scope:terra.wasm.v1beta1.Model)
    },
)
_sym_db.RegisterMessage(Model)

Code = _reflection.GeneratedProtocolMessageType(
    "Code",
    (_message.Message,),
    {
        "DESCRIPTOR": _CODE,
        "__module__": "terra.wasm.v1beta1.genesis_pb2"
        # @@protoc_insertion_point(class_scope:terra.wasm.v1beta1.Code)
    },
)
_sym_db.RegisterMessage(Code)

Contract = _reflection.GeneratedProtocolMessageType(
    "Contract",
    (_message.Message,),
    {
        "DESCRIPTOR": _CONTRACT,
        "__module__": "terra.wasm.v1beta1.genesis_pb2"
        # @@protoc_insertion_point(class_scope:terra.wasm.v1beta1.Contract)
    },
)
_sym_db.RegisterMessage(Contract)


DESCRIPTOR._options = None
_GENESISSTATE.fields_by_name["params"]._options = None
_GENESISSTATE.fields_by_name["last_code_id"]._options = None
_GENESISSTATE.fields_by_name["last_instance_id"]._options = None
_GENESISSTATE.fields_by_name["codes"]._options = None
_GENESISSTATE.fields_by_name["contracts"]._options = None
_CODE.fields_by_name["code_info"]._options = None
_CONTRACT.fields_by_name["contract_info"]._options = None
_CONTRACT.fields_by_name["contract_store"]._options = None
# @@protoc_insertion_point(module_scope)
