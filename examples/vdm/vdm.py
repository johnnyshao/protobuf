#! /usr/bin/env python3

from __future__ import print_function
from google.protobuf.json_format import MessageToJson
import vdm_pb2
import sys
import binascii
import argparse

parser = argparse.ArgumentParser(description = 'vdm2 protobuf encoder/decoder')
parser.add_argument('codec', choices = ['enc', 'decv', 'decft'], default = 'decv', help = 'encode or decode data in protobuf format')
args = parser.parse_args();
print(args)

if args.codec == 'enc':
  # Encode
  # Sample encoded data: 04 00 00 21 0A 07 08 BD 04 98 06 99 7A 12 0F 33 35 39 33 31 35 30 37 37 35 33 32 36 34 35 18 DF 9D 93 B1 B6 2C
  print('Encoding: ')
  value = vdm_pb2.Value()
  value.imei = '359315077532645'
  value.ts = 1526427078367
  value.values.core_msg_id = 573
  value.values.obd_sleep_voltage = 15641
  print(binascii.hexlify(value.SerializeToString()).upper())
else:
  encoded_data_hex = input("Enter protobuf encoded data: ")
  encoded_data_hex = encoded_data_hex.replace(' ', '')
  # Skip over 4-byte header
  print(encoded_data_hex[8:])
  if args.codec == 'decv':
    # Decode value
    # Sample encoded data: 04 00 00 21 0A 07 08 DF 1B 98 06 BD 60 12 0F 33 35 39 33 31 35 30 37 37 34 39 37 34 39 32 18 B7 8B E9 88 B8 2C
    decoded_data = vdm_pb2.Value()
  else:
    # Decode functional test
    # Sample encoded data: 140000b10a0f333539333135303737353332363435121438393436323034363635313030303635383032331a283939653962393665616463313736313234366139623435656435393363666462323034396264323020c4babc94b72c2a50080110011802200028df0230ecb5fad7053a3d76312e322e302d646576656c6f702b56454c31302d312d76302e302e302d302d302d3335312d313532363633353234342d70722d6a6f686e6e792d66743003380948ff01
    decoded_data = vdm_pb2.FunctionalTest()
  decoded_data.ParseFromString(bytes.fromhex(encoded_data_hex[8:]))
  print(MessageToJson(decoded_data))