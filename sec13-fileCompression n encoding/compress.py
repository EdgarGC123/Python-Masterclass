import zlib, base64

data = open('demo.txt','r').read()
data_bytes = bytes(data,'utf-8')#convert giant string into bytes
compressed_data = zlib.compress(data_bytes, 9)# compress bytes into smaller bytes. 9 is the max level of compression, 1 is minumum
encoded_and_compressed_data = base64.b64encode(compressed_data)#encoding the compressed bytes into a base64
decoded_data = encoded_and_compressed_data.decode('utf-8')#decompressed into a string. still encoded, still compressed, still bitten
#^ this was done in order to write (file.write()) bytes into the txt file
compressed_file=open('compressed.txt','w')
compressed_file.write(decoded_data)
# print(compressed_data)
# print(decoded_data)



#after creating the compressed.txt file, we need to convert it back to bytes, decode it, decompress and convert back to string. 


decompressed_data = zlib.decompress(base64.b64decode(compressed_data))
print(decompressed_data)