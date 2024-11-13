#!/usr/bin/env python3

import sys
import pickle
from argparse import ArgumentParser

def main():
    argparser = ArgumentParser()
    argparser.add_argument("file", type=str, help="input pickle dump file")
    args = argparser.parse_args()

    with open(args.file, 'rb') as rh:
        data = pickle.load(rh)

    print (data)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)
    except Exception as e:
        raise e
