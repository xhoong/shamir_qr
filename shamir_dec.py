from binascii import unhexlify, a2b_base64
from Crypto.Cipher import AES
from Crypto.Protocol.SecretSharing import Shamir
import io
import json
import re

import shamirs_enc

def shamir_decrypt (min: int, persist: bool):
    shares = []
    ### Reading content from QR code copied text to file `enc_x.txt`, expect 2 key to combine for recovery
    print(f"\n\tExpecting {min} QR code(s) scanned text to restore seed codes.\n")
    for x in range(min):
        if persist:
            with open(f"enc_{x+1}.txt") as fi:
                dec_js = json.loads(a2b_base64(fi.read()))
        else:
            dec_js = json.loads(a2b_base64(input(f"Enter the QR code scanned text [entry {x+1}]: ")))
        print(f"Got key index {dec_js['i']} with key {dec_js['k']}")
        shares.append((int(dec_js["i"]), unhexlify(dec_js["k"])))
        en_txt = dec_js['t']

    key = Shamir.combine(shares)

    enc_data = io.BytesIO(a2b_base64(en_txt))
    nonce, tag = [ enc_data.read(shamirs_enc.KEY_LENGTH) for _ in range(2) ]
    cipher = AES.new(key, AES.MODE_EAX, nonce)
    try:
        p = re.compile(r"\(\d+\)(.*)")
        result = cipher.decrypt(enc_data.read())
        cipher.verify(tag)
        print(f"\n\tIndexed seed words: {result.decode('UTF-8')}")
        print(f"\n\tSeed words sequence: {' '.join([p.search(_w).group(1) for _w in result.decode('UTF-8').split(' ') if p.match(_w)])}")
        if persist:
            with open("clear2.txt", "wb") as fo:
                print("Seed words written to clear2.txt file.")
                fo.write(result)
                fo.write(bytes("\n\n", "UTF-8"))
                fo.write(bytes(" ".join([p.search(_w).group(1) for _w in result.decode('UTF-8').split(' ') if p.match(_w)]), "UTF-8"))
    except ValueError:
        print("The shares were incorrect")