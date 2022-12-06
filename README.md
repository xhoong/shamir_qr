## Shamir Backup QR-Code Generator for Crypto Wallet Seed Words

Shamir Backup is a method to secure backup your crypto wallet seed words.

The programme will encrypt the provided text and split it to 3 (settable) QR-code images. 
The 3 generated QR-codes can then be used to recover the original text, with minimum of 2 (settable)
QR-code required to recover.

The generated QR-code can then be printed out and shared with your trusted parties. 
In case you loss your secret words, you need get at least 2 (any 2), and use the programme
to recover the original text again by scanning the QR-code to uncover the scanned text.

All process is done locally, no information is transferred out during the programme execution.
By default, non-persist mode is used, so no intermediaries files is stored on disk, except the generated QR-codes.

For more info on Shamir secret sharing, visit [PyCyptodome doc](https://www.pycryptodome.org/src/protocol/ss#Crypto.Protocol.SecretSharing.Shamir)

## Install

To install, clone the repository and install the requirements.

```shell
pip install -r requirements.txt
```

Developed with `Python 3.9.x`

## Usage

To encrypt and split your secret:

```shell
python main.py --encrypt
```

Key in your 24 seed words separated with space. Example refer to [clear.txt](./sample_output/clear.txt)

```text
> python main.py --encrypt
Please enter the 24 seed words in sequence separate by space: require struggle ketchup hurt draft undo garlic defy truth tell decade auto pond release law depart army elevator luxury
 analyst critic model warm slice
Index #1: b'7e8b8e1a6cc1caf665ba4ba81576ae38'
Encrypted Shamir split saved to enc_1.txt (if persist) with QR code file encqr_1.png
Index #2: b'a772dd05bdcf90110ef051e980d87ce7'
Encrypted Shamir split saved to enc_2.txt (if persist) with QR code file encqr_2.png
Index #3: b'efda13f0f2ca59b3d7c9a7d6f3bdcd52'
Encrypted Shamir split saved to enc_3.txt (if persist) with QR code file encqr_3.png
```

The input will then be encrypted using `AES` and split the secret into `3` QR-code image. 
Refer to sample of generated QR-code in the [sample_output](./sample_output) folder for file 
[encqr_1.png](./sample_output/encqr_1.png), [encqr_2.png](./sample_output/encqr_2.png) and so on.

To decrypt and recover your secret:

```shell
python main.py --decrypt
```

Scanned the QR-code and copy the text content, input to the programme prompt. 
You need to scan at least 2 QR-codes to recover the 2 text content, depends on
your first encrypt, if you set the parameter `--min` (default to 2).

```text
> python main.py --decrypt

        Expecting 2 QR code(s) scanned text to restore seed codes.

Enter the QR code scanned text [entry 1]: eyJpIjogMSwgImsiOiAiYTAzNTIyNDAxNDJmYjUzYzQxNzQxZWZjNjVjMWQ5NjQiLCAidCI6ICJ3KytORDBHK3FwWDYwRjl2MmFuUzJKY3cxQktIMEUwTDNmL20rMmM1VmJyaXVIVWx5
bXQ2SGxLNmpaSHNFKzZRRkV4Qm5TOXdEN1FnZGhaM2lMRVlxU0pTbW02cDdiTVEwd1VzYWF3QzViUjk5QkpsdWZWQWVNeEtUNFByb25xN0N4Tmw3L050ZUIzUHJkU1FOdHBCQ2pPVDB5MnpIM2QwV3EwOFU5OExtbkt3NXd3ckZPMGpYaDFzWX
YxaDVkcy9uNGd6WDYxbDNEd3hFY2FOYWtaMTZVSmR1MkJsT2ZuTWxESlVBY3VmZWQreDNMWkRHbmdEUzB3eWxvTEpkTGEvSnVwNGVDNjdsM0k5TVlWWHpSMWl2Z2lDLzk5Mlp4dnlmZzBReFpJMTlCRmszanJaUmNDSlBGZkVaZnZuZGJNRGxh
b0RSR3B4SWpWRUMrWFVsaDc0c0R2TkZXb2N2VTRBbWNPRStXTEdTdz09In0=
Got key index 1 with key a0352240142fb53c41741efc65c1d964
Enter the QR code scanned text [entry 2]: eyJpIjogMywgImsiOiAiNTY4M2ZiMDdlMzk5YjQ1NzdjZGQ2NWJkOWJlZDk3ZjAiLCAidCI6ICJ3KytORDBHK3FwWDYwRjl2MmFuUzJKY3cxQktIMEUwTDNmL20rMmM1VmJyaXVIVWx5
bXQ2SGxLNmpaSHNFKzZRRkV4Qm5TOXdEN1FnZGhaM2lMRVlxU0pTbW02cDdiTVEwd1VzYWF3QzViUjk5QkpsdWZWQWVNeEtUNFByb25xN0N4Tmw3L050ZUIzUHJkU1FOdHBCQ2pPVDB5MnpIM2QwV3EwOFU5OExtbkt3NXd3ckZPMGpYaDFzWX
YxaDVkcy9uNGd6WDYxbDNEd3hFY2FOYWtaMTZVSmR1MkJsT2ZuTWxESlVBY3VmZWQreDNMWkRHbmdEUzB3eWxvTEpkTGEvSnVwNGVDNjdsM0k5TVlWWHpSMWl2Z2lDLzk5Mlp4dnlmZzBReFpJMTlCRmszanJaUmNDSlBGZkVaZnZuZGJNRGxh
b0RSR3B4SWpWRUMrWFVsaDc0c0R2TkZXb2N2VTRBbWNPRStXTEdTdz09In0=
Got key index 3 with key 5683fb07e399b4577cdd65bd9bed97f0

        Indexed seed words: (1)require (2)struggle (3)ketchup (4)hurt (5)draft (6)undo (7)garlic (8)defy (9)truth (10)tell (11)decade (12)auto (13)pond (14)release (15)law (16)depart
 (17)army (18)elevator (19)luxury (20)analyst (21)critic (22)model (23)warm (24)slice

        Seed words sequence: require struggle ketchup hurt draft undo garlic defy truth tell decade auto pond release law depart army elevator luxury analyst critic model warm slice 
```

### Extra Arguments

`--persist` 

- Together with `--encrypt`, to take input of seed words from file `clear.txt` and output the QR-code content in files,
e.g. `enc_1.txt`, `enc_2.txt` and so on. Hence, no human interaction required.
- When use together with `--decrypt`, it will read files `enc_1.txt`, `enc_2.txt` and so on to 
recover the original text. The recovered text will be saved to `clear2.txt`.

`--min`
- Minimum split to combine, for recovery of the original text, defaulted to 2
- When use with `--decrypt`, it will then prompt for entry for the number entered

`--split`
- The number of QR-codes to generate, defaulted to 3. The split number needs to be
higher than `--min` value. Only use for `--encrypt`.

### License

[MIT License](./LICENSE)