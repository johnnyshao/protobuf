#! /usr/bin/env python3

from __future__ import print_function
from google.protobuf.json_format import MessageToJson
import vdm_pb2
import sys

encoded_data_hex = input("Enter protobuf encoded data: ")
encoded_data_hex = encoded_data_hex.replace(' ', '')
#print(encoded_data_hex)
decoded_data = vdm_pb2.Value()
decoded_data.ParseFromString(bytes.fromhex(encoded_data_hex[8:]))
print(MessageToJson(decoded_data))