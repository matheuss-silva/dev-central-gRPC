"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor # type: ignore
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12notification.proto\"&\n\x13NotificationRequest\x12\x0f\n\x07message\x18\x01 \x01(\t\",\n\x14NotificationResponse\x12\x14\n\x0c\x63onfirmation\x18\x01 \x01(\t2V\n\x13NotificationService\x12?\n\x10SendNotification\x12\x14.NotificationRequest\x1a\x15.NotificationResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'notification_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_NOTIFICATIONREQUEST']._serialized_start=22
  _globals['_NOTIFICATIONREQUEST']._serialized_end=60
  _globals['_NOTIFICATIONRESPONSE']._serialized_start=62
  _globals['_NOTIFICATIONRESPONSE']._serialized_end=106
  _globals['_NOTIFICATIONSERVICE']._serialized_start=108
  _globals['_NOTIFICATIONSERVICE']._serialized_end=194
# @@protoc_insertion_point(module_scope)
