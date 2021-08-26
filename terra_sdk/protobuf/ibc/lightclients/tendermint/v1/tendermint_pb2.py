# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ibc/lightclients/tendermint/v1/tendermint.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from confio import proofs_pb2 as confio_dot_proofs__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import \
    duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import \
    timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from ibc.core.client.v1 import \
    client_pb2 as ibc_dot_core_dot_client_dot_v1_dot_client__pb2
from ibc.core.commitment.v1 import \
    commitment_pb2 as ibc_dot_core_dot_commitment_dot_v1_dot_commitment__pb2
from tendermint.types import types_pb2 as tendermint_dot_types_dot_types__pb2
from tendermint.types import \
    validator_pb2 as tendermint_dot_types_dot_validator__pb2

DESCRIPTOR = _descriptor.FileDescriptor(
    name="ibc/lightclients/tendermint/v1/tendermint.proto",
    package="ibc.lightclients.tendermint.v1",
    syntax="proto3",
    serialized_options=b"ZBgithub.com/cosmos/ibc-go/modules/light-clients/07-tendermint/types",
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n/ibc/lightclients/tendermint/v1/tendermint.proto\x12\x1eibc.lightclients.tendermint.v1\x1a tendermint/types/validator.proto\x1a\x1ctendermint/types/types.proto\x1a\x13\x63onfio/proofs.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1fibc/core/client/v1/client.proto\x1a\'ibc/core/commitment/v1/commitment.proto\x1a\x14gogoproto/gogo.proto"\xb8\x06\n\x0b\x43lientState\x12\x10\n\x08\x63hain_id\x18\x01 \x01(\t\x12Y\n\x0btrust_level\x18\x02 \x01(\x0b\x32(.ibc.lightclients.tendermint.v1.FractionB\x1a\xc8\xde\x1f\x00\xf2\xde\x1f\x12yaml:"trust_level"\x12V\n\x0ftrusting_period\x18\x03 \x01(\x0b\x32\x19.google.protobuf.DurationB"\xc8\xde\x1f\x00\x98\xdf\x1f\x01\xf2\xde\x1f\x16yaml:"trusting_period"\x12X\n\x10unbonding_period\x18\x04 \x01(\x0b\x32\x19.google.protobuf.DurationB#\xc8\xde\x1f\x00\x98\xdf\x1f\x01\xf2\xde\x1f\x17yaml:"unbonding_period"\x12V\n\x0fmax_clock_drift\x18\x05 \x01(\x0b\x32\x19.google.protobuf.DurationB"\xc8\xde\x1f\x00\x98\xdf\x1f\x01\xf2\xde\x1f\x16yaml:"max_clock_drift"\x12O\n\rfrozen_height\x18\x06 \x01(\x0b\x32\x1a.ibc.core.client.v1.HeightB\x1c\xc8\xde\x1f\x00\xf2\xde\x1f\x14yaml:"frozen_height"\x12O\n\rlatest_height\x18\x07 \x01(\x0b\x32\x1a.ibc.core.client.v1.HeightB\x1c\xc8\xde\x1f\x00\xf2\xde\x1f\x14yaml:"latest_height"\x12=\n\x0bproof_specs\x18\x08 \x03(\x0b\x32\x10.ics23.ProofSpecB\x16\xf2\xde\x1f\x12yaml:"proof_specs"\x12-\n\x0cupgrade_path\x18\t \x03(\tB\x17\xf2\xde\x1f\x13yaml:"upgrade_path"\x12G\n\x19\x61llow_update_after_expiry\x18\n \x01(\x08\x42$\xf2\xde\x1f yaml:"allow_update_after_expiry"\x12S\n\x1f\x61llow_update_after_misbehaviour\x18\x0b \x01(\x08\x42*\xf2\xde\x1f&yaml:"allow_update_after_misbehaviour":\x04\x88\xa0\x1f\x00"\xfe\x01\n\x0e\x43onsensusState\x12\x37\n\ttimestamp\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x08\xc8\xde\x1f\x00\x90\xdf\x1f\x01\x12\x36\n\x04root\x18\x02 \x01(\x0b\x32".ibc.core.commitment.v1.MerkleRootB\x04\xc8\xde\x1f\x00\x12u\n\x14next_validators_hash\x18\x03 \x01(\x0c\x42W\xfa\xde\x1f\x34github.com/tendermint/tendermint/libs/bytes.HexBytes\xf2\xde\x1f\x1byaml:"next_validators_hash":\x04\x88\xa0\x1f\x00"\xf1\x01\n\x0cMisbehaviour\x12\'\n\tclient_id\x18\x01 \x01(\tB\x14\xf2\xde\x1f\x10yaml:"client_id"\x12X\n\x08header_1\x18\x02 \x01(\x0b\x32&.ibc.lightclients.tendermint.v1.HeaderB\x1e\xe2\xde\x1f\x07Header1\xf2\xde\x1f\x0fyaml:"header_1"\x12X\n\x08header_2\x18\x03 \x01(\x0b\x32&.ibc.lightclients.tendermint.v1.HeaderB\x1e\xe2\xde\x1f\x07Header2\xf2\xde\x1f\x0fyaml:"header_2":\x04\x88\xa0\x1f\x00"\xdc\x02\n\x06Header\x12S\n\rsigned_header\x18\x01 \x01(\x0b\x32\x1e.tendermint.types.SignedHeaderB\x1c\xd0\xde\x1f\x01\xf2\xde\x1f\x14yaml:"signed_header"\x12O\n\rvalidator_set\x18\x02 \x01(\x0b\x32\x1e.tendermint.types.ValidatorSetB\x18\xf2\xde\x1f\x14yaml:"validator_set"\x12Q\n\x0etrusted_height\x18\x03 \x01(\x0b\x32\x1a.ibc.core.client.v1.HeightB\x1d\xc8\xde\x1f\x00\xf2\xde\x1f\x15yaml:"trusted_height"\x12Y\n\x12trusted_validators\x18\x04 \x01(\x0b\x32\x1e.tendermint.types.ValidatorSetB\x1d\xf2\xde\x1f\x19yaml:"trusted_validators""2\n\x08\x46raction\x12\x11\n\tnumerator\x18\x01 \x01(\x04\x12\x13\n\x0b\x64\x65nominator\x18\x02 \x01(\x04\x42\x44ZBgithub.com/cosmos/ibc-go/modules/light-clients/07-tendermint/typesb\x06proto3',
    dependencies=[
        tendermint_dot_types_dot_validator__pb2.DESCRIPTOR,
        tendermint_dot_types_dot_types__pb2.DESCRIPTOR,
        confio_dot_proofs__pb2.DESCRIPTOR,
        google_dot_protobuf_dot_duration__pb2.DESCRIPTOR,
        google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,
        ibc_dot_core_dot_client_dot_v1_dot_client__pb2.DESCRIPTOR,
        ibc_dot_core_dot_commitment_dot_v1_dot_commitment__pb2.DESCRIPTOR,
        gogoproto_dot_gogo__pb2.DESCRIPTOR,
    ],
)


_CLIENTSTATE = _descriptor.Descriptor(
    name="ClientState",
    full_name="ibc.lightclients.tendermint.v1.ClientState",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="chain_id",
            full_name="ibc.lightclients.tendermint.v1.ClientState.chain_id",
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
            name="trust_level",
            full_name="ibc.lightclients.tendermint.v1.ClientState.trust_level",
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
            serialized_options=b'\310\336\037\000\362\336\037\022yaml:"trust_level"',
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="trusting_period",
            full_name="ibc.lightclients.tendermint.v1.ClientState.trusting_period",
            index=2,
            number=3,
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
            serialized_options=b'\310\336\037\000\230\337\037\001\362\336\037\026yaml:"trusting_period"',
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="unbonding_period",
            full_name="ibc.lightclients.tendermint.v1.ClientState.unbonding_period",
            index=3,
            number=4,
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
            serialized_options=b'\310\336\037\000\230\337\037\001\362\336\037\027yaml:"unbonding_period"',
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="max_clock_drift",
            full_name="ibc.lightclients.tendermint.v1.ClientState.max_clock_drift",
            index=4,
            number=5,
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
            serialized_options=b'\310\336\037\000\230\337\037\001\362\336\037\026yaml:"max_clock_drift"',
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="frozen_height",
            full_name="ibc.lightclients.tendermint.v1.ClientState.frozen_height",
            index=5,
            number=6,
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
            serialized_options=b'\310\336\037\000\362\336\037\024yaml:"frozen_height"',
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="latest_height",
            full_name="ibc.lightclients.tendermint.v1.ClientState.latest_height",
            index=6,
            number=7,
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
            serialized_options=b'\310\336\037\000\362\336\037\024yaml:"latest_height"',
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="proof_specs",
            full_name="ibc.lightclients.tendermint.v1.ClientState.proof_specs",
            index=7,
            number=8,
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
            serialized_options=b'\362\336\037\022yaml:"proof_specs"',
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="upgrade_path",
            full_name="ibc.lightclients.tendermint.v1.ClientState.upgrade_path",
            index=8,
            number=9,
            type=9,
            cpp_type=9,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b'\362\336\037\023yaml:"upgrade_path"',
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="allow_update_after_expiry",
            full_name="ibc.lightclients.tendermint.v1.ClientState.allow_update_after_expiry",
            index=9,
            number=10,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b'\362\336\037 yaml:"allow_update_after_expiry"',
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="allow_update_after_misbehaviour",
            full_name="ibc.lightclients.tendermint.v1.ClientState.allow_update_after_misbehaviour",
            index=10,
            number=11,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b'\362\336\037&yaml:"allow_update_after_misbehaviour"',
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
    serialized_start=330,
    serialized_end=1154,
)


_CONSENSUSSTATE = _descriptor.Descriptor(
    name="ConsensusState",
    full_name="ibc.lightclients.tendermint.v1.ConsensusState",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="timestamp",
            full_name="ibc.lightclients.tendermint.v1.ConsensusState.timestamp",
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
            serialized_options=b"\310\336\037\000\220\337\037\001",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="root",
            full_name="ibc.lightclients.tendermint.v1.ConsensusState.root",
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
            serialized_options=b"\310\336\037\000",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="next_validators_hash",
            full_name="ibc.lightclients.tendermint.v1.ConsensusState.next_validators_hash",
            index=2,
            number=3,
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
            serialized_options=b'\372\336\0374github.com/tendermint/tendermint/libs/bytes.HexBytes\362\336\037\033yaml:"next_validators_hash"',
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
    serialized_start=1157,
    serialized_end=1411,
)


_MISBEHAVIOUR = _descriptor.Descriptor(
    name="Misbehaviour",
    full_name="ibc.lightclients.tendermint.v1.Misbehaviour",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="client_id",
            full_name="ibc.lightclients.tendermint.v1.Misbehaviour.client_id",
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
            serialized_options=b'\362\336\037\020yaml:"client_id"',
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="header_1",
            full_name="ibc.lightclients.tendermint.v1.Misbehaviour.header_1",
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
            serialized_options=b'\342\336\037\007Header1\362\336\037\017yaml:"header_1"',
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="header_2",
            full_name="ibc.lightclients.tendermint.v1.Misbehaviour.header_2",
            index=2,
            number=3,
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
            serialized_options=b'\342\336\037\007Header2\362\336\037\017yaml:"header_2"',
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
    serialized_start=1414,
    serialized_end=1655,
)


_HEADER = _descriptor.Descriptor(
    name="Header",
    full_name="ibc.lightclients.tendermint.v1.Header",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="signed_header",
            full_name="ibc.lightclients.tendermint.v1.Header.signed_header",
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
            serialized_options=b'\320\336\037\001\362\336\037\024yaml:"signed_header"',
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="validator_set",
            full_name="ibc.lightclients.tendermint.v1.Header.validator_set",
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
            serialized_options=b'\362\336\037\024yaml:"validator_set"',
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="trusted_height",
            full_name="ibc.lightclients.tendermint.v1.Header.trusted_height",
            index=2,
            number=3,
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
            serialized_options=b'\310\336\037\000\362\336\037\025yaml:"trusted_height"',
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="trusted_validators",
            full_name="ibc.lightclients.tendermint.v1.Header.trusted_validators",
            index=3,
            number=4,
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
            serialized_options=b'\362\336\037\031yaml:"trusted_validators"',
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
    serialized_start=1658,
    serialized_end=2006,
)


_FRACTION = _descriptor.Descriptor(
    name="Fraction",
    full_name="ibc.lightclients.tendermint.v1.Fraction",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="numerator",
            full_name="ibc.lightclients.tendermint.v1.Fraction.numerator",
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
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="denominator",
            full_name="ibc.lightclients.tendermint.v1.Fraction.denominator",
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
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=2008,
    serialized_end=2058,
)

_CLIENTSTATE.fields_by_name["trust_level"].message_type = _FRACTION
_CLIENTSTATE.fields_by_name[
    "trusting_period"
].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_CLIENTSTATE.fields_by_name[
    "unbonding_period"
].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_CLIENTSTATE.fields_by_name[
    "max_clock_drift"
].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_CLIENTSTATE.fields_by_name[
    "frozen_height"
].message_type = ibc_dot_core_dot_client_dot_v1_dot_client__pb2._HEIGHT
_CLIENTSTATE.fields_by_name[
    "latest_height"
].message_type = ibc_dot_core_dot_client_dot_v1_dot_client__pb2._HEIGHT
_CLIENTSTATE.fields_by_name[
    "proof_specs"
].message_type = confio_dot_proofs__pb2._PROOFSPEC
_CONSENSUSSTATE.fields_by_name[
    "timestamp"
].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_CONSENSUSSTATE.fields_by_name[
    "root"
].message_type = ibc_dot_core_dot_commitment_dot_v1_dot_commitment__pb2._MERKLEROOT
_MISBEHAVIOUR.fields_by_name["header_1"].message_type = _HEADER
_MISBEHAVIOUR.fields_by_name["header_2"].message_type = _HEADER
_HEADER.fields_by_name[
    "signed_header"
].message_type = tendermint_dot_types_dot_types__pb2._SIGNEDHEADER
_HEADER.fields_by_name[
    "validator_set"
].message_type = tendermint_dot_types_dot_validator__pb2._VALIDATORSET
_HEADER.fields_by_name[
    "trusted_height"
].message_type = ibc_dot_core_dot_client_dot_v1_dot_client__pb2._HEIGHT
_HEADER.fields_by_name[
    "trusted_validators"
].message_type = tendermint_dot_types_dot_validator__pb2._VALIDATORSET
DESCRIPTOR.message_types_by_name["ClientState"] = _CLIENTSTATE
DESCRIPTOR.message_types_by_name["ConsensusState"] = _CONSENSUSSTATE
DESCRIPTOR.message_types_by_name["Misbehaviour"] = _MISBEHAVIOUR
DESCRIPTOR.message_types_by_name["Header"] = _HEADER
DESCRIPTOR.message_types_by_name["Fraction"] = _FRACTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ClientState = _reflection.GeneratedProtocolMessageType(
    "ClientState",
    (_message.Message,),
    {
        "DESCRIPTOR": _CLIENTSTATE,
        "__module__": "ibc.lightclients.tendermint.v1.tendermint_pb2"
        # @@protoc_insertion_point(class_scope:ibc.lightclients.tendermint.v1.ClientState)
    },
)
_sym_db.RegisterMessage(ClientState)

ConsensusState = _reflection.GeneratedProtocolMessageType(
    "ConsensusState",
    (_message.Message,),
    {
        "DESCRIPTOR": _CONSENSUSSTATE,
        "__module__": "ibc.lightclients.tendermint.v1.tendermint_pb2"
        # @@protoc_insertion_point(class_scope:ibc.lightclients.tendermint.v1.ConsensusState)
    },
)
_sym_db.RegisterMessage(ConsensusState)

Misbehaviour = _reflection.GeneratedProtocolMessageType(
    "Misbehaviour",
    (_message.Message,),
    {
        "DESCRIPTOR": _MISBEHAVIOUR,
        "__module__": "ibc.lightclients.tendermint.v1.tendermint_pb2"
        # @@protoc_insertion_point(class_scope:ibc.lightclients.tendermint.v1.Misbehaviour)
    },
)
_sym_db.RegisterMessage(Misbehaviour)

Header = _reflection.GeneratedProtocolMessageType(
    "Header",
    (_message.Message,),
    {
        "DESCRIPTOR": _HEADER,
        "__module__": "ibc.lightclients.tendermint.v1.tendermint_pb2"
        # @@protoc_insertion_point(class_scope:ibc.lightclients.tendermint.v1.Header)
    },
)
_sym_db.RegisterMessage(Header)

Fraction = _reflection.GeneratedProtocolMessageType(
    "Fraction",
    (_message.Message,),
    {
        "DESCRIPTOR": _FRACTION,
        "__module__": "ibc.lightclients.tendermint.v1.tendermint_pb2"
        # @@protoc_insertion_point(class_scope:ibc.lightclients.tendermint.v1.Fraction)
    },
)
_sym_db.RegisterMessage(Fraction)


DESCRIPTOR._options = None
_CLIENTSTATE.fields_by_name["trust_level"]._options = None
_CLIENTSTATE.fields_by_name["trusting_period"]._options = None
_CLIENTSTATE.fields_by_name["unbonding_period"]._options = None
_CLIENTSTATE.fields_by_name["max_clock_drift"]._options = None
_CLIENTSTATE.fields_by_name["frozen_height"]._options = None
_CLIENTSTATE.fields_by_name["latest_height"]._options = None
_CLIENTSTATE.fields_by_name["proof_specs"]._options = None
_CLIENTSTATE.fields_by_name["upgrade_path"]._options = None
_CLIENTSTATE.fields_by_name["allow_update_after_expiry"]._options = None
_CLIENTSTATE.fields_by_name["allow_update_after_misbehaviour"]._options = None
_CLIENTSTATE._options = None
_CONSENSUSSTATE.fields_by_name["timestamp"]._options = None
_CONSENSUSSTATE.fields_by_name["root"]._options = None
_CONSENSUSSTATE.fields_by_name["next_validators_hash"]._options = None
_CONSENSUSSTATE._options = None
_MISBEHAVIOUR.fields_by_name["client_id"]._options = None
_MISBEHAVIOUR.fields_by_name["header_1"]._options = None
_MISBEHAVIOUR.fields_by_name["header_2"]._options = None
_MISBEHAVIOUR._options = None
_HEADER.fields_by_name["signed_header"]._options = None
_HEADER.fields_by_name["validator_set"]._options = None
_HEADER.fields_by_name["trusted_height"]._options = None
_HEADER.fields_by_name["trusted_validators"]._options = None
# @@protoc_insertion_point(module_scope)
