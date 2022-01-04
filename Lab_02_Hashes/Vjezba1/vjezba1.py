import magic
import hashlib
import os
import glob

if __name__ == "__main__":
    files = glob.glob('./Vjezba1/*')
    print(files)
    for fn in files:
        print(fn + "--->" + magic.from_buffer(open(fn, "rb").read(2048)))
