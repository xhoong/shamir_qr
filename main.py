import shamirs_enc
import shamir_dec
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser("main.py", description="Program to encrypt secure seed word and split using Shamir")
    parser.add_argument("--split", "-s", type=int, help="the number of split (3)", default=3)
    parser.add_argument("--min", "-m", type=int, help="the min number to combine (2)", default=2)
    parser.add_argument("--encrypt", help="enable encryption and split", action="store_true")
    parser.add_argument("--decrypt", help="enable encryption and split", action="store_true")
    parser.add_argument("--persist", help="enable output of encrypted or decrypted file", action="store_true")


    args = parser.parse_args()
    ###  Split to 3, with minimum 2 to combine
    if args.encrypt:
        if args.split < args.min:
            raise RuntimeError("Minimum combine number (--min) needs to be higher than split (--split)")
        if args.persist:
            with open("clear.txt", "rb") as fi:
                print("Persist flag enabled, will read the 24 seed words from file [clear.txt].")
                clr_txt = fi.read().decode("utf-8")
        else:
            clr_txt = input("Please enter the 24 seed words in sequence separate by space: ")

        words = clr_txt.split(' ')
        if len(words) != 24:
            raise RuntimeError("The secure key words need to be in 24 words separated by space")
        shamirs_enc.shamir_encrypt(" ".join([f"({i}){w}" for i, w in zip(range(1, 25), words)]),
                                   args.min, args.split, args.persist)
    elif args.decrypt:
        shamir_dec.shamir_decrypt(args.min, args.persist)
    else:
        print("Nothing to do")

