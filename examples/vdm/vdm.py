#! /usr/bin/env python3

from __future__ import print_function
from google.protobuf.json_format import MessageToJson
import vdm_pb2
import sys
import binascii

# Decode
encoded_data_hex = input("Enter protobuf encoded data: ")
encoded_data_hex = encoded_data_hex.replace(' ', '')
# Skip over 4-byte header
print(encoded_data_hex[8:])
decoded_data = vdm_pb2.Value()
decoded_data.ParseFromString(bytes.fromhex(encoded_data_hex[8:]))
print(MessageToJson(decoded_data))

# Encode
# Sample encoded data: 04 00 00 21 0A 07 08 BD 04 98 06 99 7A 12 0F 33 35 39 33 31 35 30 37 37 35 33 32 36 34 35 18 DF 9D 93 B1 B6 2C
print('Encoding: ')
value = vdm_pb2.Value()
value.imei = '359315077532645'
value.ts = 1526427078367
value.values.core_msg_id = 573
value.values.obd_sleep_voltage = 15641
print(binascii.hexlify(value.SerializeToString()).upper())