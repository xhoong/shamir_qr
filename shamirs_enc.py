from binascii import hexlify, b2a_base64
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Protocol.SecretSharing import Shamir
import json
import qrcode
qr = qrcode.QRCode(
    version=None,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

KEY_LENGTH=16

## 16 bytes key with random word of nonce
###  Split to 3, with minimum 2 to combine
def shamir_encrypt(data: str, min: int, split: int, persist: bool):
    key = get_random_bytes(KEY_LENGTH)
    nonce = get_random_bytes(KEY_LENGTH)
    shares = Shamir.split(min, split, key)

    cipher = AES.new(key, AES.MODE_EAX, nonce)
    ct, tag = cipher.encrypt(bytes(data, 'UTF-8')), cipher.digest()
    en_text = b2a_base64(nonce + tag + ct, newline=False)

    for idx, share in shares:
        print("Index #%d: %s" % (idx, hexlify(share)))

        share = {"i": idx,"k":hexlify(share).decode('UTF-8'),"t":en_text.decode('UTF-8')}
        b64_txt = b2a_base64(bytes(json.dumps(share), 'UTF-8'), newline=False)
        if persist:
            with open(f"enc_{idx}.txt", "wb") as fo:
                fo.write(b64_txt)
        qr.add_data(b64_txt.decode('UTF-8'))
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        img.save(f"encqr_{idx}.png")
        print(f"Encrypted Shamir split saved to enc_{idx}.txt (if persist) with QR code file encqr_{idx}.png")



