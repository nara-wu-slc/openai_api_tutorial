#!/usr/bin/env python3

import sys
import os
import openai
import pickle
import uuid
from argparse import ArgumentParser


def main():
    argparser = ArgumentParser()
    argparser.add_argument("-v", "--verbose", action="store_true", help="verbose output")
    argparser.add_argument("file", type=str, help="chat completion log in *.pkl")
    args = argparser.parse_args()

    with open(args.file, 'rb') as wf:
        DATA = pickle.load(wf)
        print (DATA.choices[0].message.content)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt as e:
        sys.exit(1)
    except Exception as e:
        raise e
