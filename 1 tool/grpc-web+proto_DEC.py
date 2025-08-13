import blackboxprotobuf

hex_string='0a180a0570617065721206e59cb0e790832801301442010048011001'

bytes_string=bytes.fromhex(hex_string)

dec_data,message_type=blackboxprotobuf.protobuf_to_json(bytes_string)

print(dec_data)
print(message_type)