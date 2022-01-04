from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

imeStudenta = "IvicFilip" + "21854671" # NAPOMENA: SALT je BitLocker lozinka
digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
digest.update(str.encode(imeStudenta))
filename = digest.finalize().hex()

print(filename)