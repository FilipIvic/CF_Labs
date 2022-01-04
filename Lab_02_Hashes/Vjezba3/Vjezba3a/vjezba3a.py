import hashlib

file = "test.docx"
BLOCK_SIZE = 65536

file_hash1 = hashlib.sha1()
file_hash2 = hashlib.sha256()
file_hash3 = hashlib.md5()
with open(file, 'rb') as f:
    fb = f.read(BLOCK_SIZE)
    while len(fb) > 0:
        file_hash1.update(fb)
        file_hash2.update(fb)
        file_hash3.update(fb)
        fb = f.read(BLOCK_SIZE)

print ("--------" + file + "---------")
print ("MD5:    " + file_hash3.hexdigest())
print ("SHA1:   " + file_hash1.hexdigest())
print ("SHA256: " + file_hash2.hexdigest())


file = "test.jpg"
BLOCK_SIZE = 65536

file_hash1 = hashlib.sha1()
file_hash2 = hashlib.sha256()
file_hash3 = hashlib.md5()
with open(file, 'rb') as f:
    fb = f.read(BLOCK_SIZE)
    while len(fb) > 0:
        file_hash1.update(fb)
        file_hash2.update(fb)
        file_hash3.update(fb)
        fb = f.read(BLOCK_SIZE)

print ("--------" + file + "---------")
print ("MD5:    " + file_hash3.hexdigest())
print ("SHA1:   " + file_hash1.hexdigest())
print ("SHA256: " + file_hash2.hexdigest())


