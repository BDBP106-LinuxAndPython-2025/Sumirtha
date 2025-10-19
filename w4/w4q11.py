#11. How to read and write binary data? Example programs:
#Writing binary:
with open("snapshot_blob.bin", "wb") as f:
    f.write(b'\x00\x01\x02\x03')
#Reading binary:
with open("snapshot_blob.bin", "rb") as f:
    data = f.read()
    print(data)