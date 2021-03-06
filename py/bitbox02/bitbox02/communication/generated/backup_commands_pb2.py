# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: backup_commands.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='backup_commands.proto',
  package='shiftcrypto.bitbox02',
  syntax='proto3',
  serialized_pb=_b('\n\x15\x62\x61\x63kup_commands.proto\x12\x14shiftcrypto.bitbox02\"$\n\x12\x43heckBackupRequest\x12\x0e\n\x06silent\x18\x01 \x01(\x08\"!\n\x13\x43heckBackupResponse\x12\n\n\x02id\x18\x01 \x01(\t\"A\n\x13\x43reateBackupRequest\x12\x11\n\ttimestamp\x18\x01 \x01(\r\x12\x17\n\x0ftimezone_offset\x18\x02 \x01(\x05\"\x14\n\x12ListBackupsRequest\"9\n\nBackupInfo\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\ttimestamp\x18\x02 \x01(\r\x12\x0c\n\x04name\x18\x04 \x01(\t\"E\n\x13ListBackupsResponse\x12.\n\x04info\x18\x01 \x03(\x0b\x32 .shiftcrypto.bitbox02.BackupInfo\"N\n\x14RestoreBackupRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\ttimestamp\x18\x02 \x01(\r\x12\x17\n\x0ftimezone_offset\x18\x03 \x01(\x05\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_CHECKBACKUPREQUEST = _descriptor.Descriptor(
  name='CheckBackupRequest',
  full_name='shiftcrypto.bitbox02.CheckBackupRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='silent', full_name='shiftcrypto.bitbox02.CheckBackupRequest.silent', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=47,
  serialized_end=83,
)


_CHECKBACKUPRESPONSE = _descriptor.Descriptor(
  name='CheckBackupResponse',
  full_name='shiftcrypto.bitbox02.CheckBackupResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='shiftcrypto.bitbox02.CheckBackupResponse.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=85,
  serialized_end=118,
)


_CREATEBACKUPREQUEST = _descriptor.Descriptor(
  name='CreateBackupRequest',
  full_name='shiftcrypto.bitbox02.CreateBackupRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='shiftcrypto.bitbox02.CreateBackupRequest.timestamp', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timezone_offset', full_name='shiftcrypto.bitbox02.CreateBackupRequest.timezone_offset', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=120,
  serialized_end=185,
)


_LISTBACKUPSREQUEST = _descriptor.Descriptor(
  name='ListBackupsRequest',
  full_name='shiftcrypto.bitbox02.ListBackupsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=187,
  serialized_end=207,
)


_BACKUPINFO = _descriptor.Descriptor(
  name='BackupInfo',
  full_name='shiftcrypto.bitbox02.BackupInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='shiftcrypto.bitbox02.BackupInfo.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='shiftcrypto.bitbox02.BackupInfo.timestamp', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='shiftcrypto.bitbox02.BackupInfo.name', index=2,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=209,
  serialized_end=266,
)


_LISTBACKUPSRESPONSE = _descriptor.Descriptor(
  name='ListBackupsResponse',
  full_name='shiftcrypto.bitbox02.ListBackupsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='info', full_name='shiftcrypto.bitbox02.ListBackupsResponse.info', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=268,
  serialized_end=337,
)


_RESTOREBACKUPREQUEST = _descriptor.Descriptor(
  name='RestoreBackupRequest',
  full_name='shiftcrypto.bitbox02.RestoreBackupRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='shiftcrypto.bitbox02.RestoreBackupRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='shiftcrypto.bitbox02.RestoreBackupRequest.timestamp', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timezone_offset', full_name='shiftcrypto.bitbox02.RestoreBackupRequest.timezone_offset', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=339,
  serialized_end=417,
)

_LISTBACKUPSRESPONSE.fields_by_name['info'].message_type = _BACKUPINFO
DESCRIPTOR.message_types_by_name['CheckBackupRequest'] = _CHECKBACKUPREQUEST
DESCRIPTOR.message_types_by_name['CheckBackupResponse'] = _CHECKBACKUPRESPONSE
DESCRIPTOR.message_types_by_name['CreateBackupRequest'] = _CREATEBACKUPREQUEST
DESCRIPTOR.message_types_by_name['ListBackupsRequest'] = _LISTBACKUPSREQUEST
DESCRIPTOR.message_types_by_name['BackupInfo'] = _BACKUPINFO
DESCRIPTOR.message_types_by_name['ListBackupsResponse'] = _LISTBACKUPSRESPONSE
DESCRIPTOR.message_types_by_name['RestoreBackupRequest'] = _RESTOREBACKUPREQUEST

CheckBackupRequest = _reflection.GeneratedProtocolMessageType('CheckBackupRequest', (_message.Message,), dict(
  DESCRIPTOR = _CHECKBACKUPREQUEST,
  __module__ = 'backup_commands_pb2'
  # @@protoc_insertion_point(class_scope:shiftcrypto.bitbox02.CheckBackupRequest)
  ))
_sym_db.RegisterMessage(CheckBackupRequest)

CheckBackupResponse = _reflection.GeneratedProtocolMessageType('CheckBackupResponse', (_message.Message,), dict(
  DESCRIPTOR = _CHECKBACKUPRESPONSE,
  __module__ = 'backup_commands_pb2'
  # @@protoc_insertion_point(class_scope:shiftcrypto.bitbox02.CheckBackupResponse)
  ))
_sym_db.RegisterMessage(CheckBackupResponse)

CreateBackupRequest = _reflection.GeneratedProtocolMessageType('CreateBackupRequest', (_message.Message,), dict(
  DESCRIPTOR = _CREATEBACKUPREQUEST,
  __module__ = 'backup_commands_pb2'
  # @@protoc_insertion_point(class_scope:shiftcrypto.bitbox02.CreateBackupRequest)
  ))
_sym_db.RegisterMessage(CreateBackupRequest)

ListBackupsRequest = _reflection.GeneratedProtocolMessageType('ListBackupsRequest', (_message.Message,), dict(
  DESCRIPTOR = _LISTBACKUPSREQUEST,
  __module__ = 'backup_commands_pb2'
  # @@protoc_insertion_point(class_scope:shiftcrypto.bitbox02.ListBackupsRequest)
  ))
_sym_db.RegisterMessage(ListBackupsRequest)

BackupInfo = _reflection.GeneratedProtocolMessageType('BackupInfo', (_message.Message,), dict(
  DESCRIPTOR = _BACKUPINFO,
  __module__ = 'backup_commands_pb2'
  # @@protoc_insertion_point(class_scope:shiftcrypto.bitbox02.BackupInfo)
  ))
_sym_db.RegisterMessage(BackupInfo)

ListBackupsResponse = _reflection.GeneratedProtocolMessageType('ListBackupsResponse', (_message.Message,), dict(
  DESCRIPTOR = _LISTBACKUPSRESPONSE,
  __module__ = 'backup_commands_pb2'
  # @@protoc_insertion_point(class_scope:shiftcrypto.bitbox02.ListBackupsResponse)
  ))
_sym_db.RegisterMessage(ListBackupsResponse)

RestoreBackupRequest = _reflection.GeneratedProtocolMessageType('RestoreBackupRequest', (_message.Message,), dict(
  DESCRIPTOR = _RESTOREBACKUPREQUEST,
  __module__ = 'backup_commands_pb2'
  # @@protoc_insertion_point(class_scope:shiftcrypto.bitbox02.RestoreBackupRequest)
  ))
_sym_db.RegisterMessage(RestoreBackupRequest)


# @@protoc_insertion_point(module_scope)
