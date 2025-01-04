#!/usr/bin/env python3

import sys
import os
import openai
import datetime
import pickle
import uuid
from argparse import ArgumentParser


def main():
    argparser = ArgumentParser()
    argparser.add_argument("-v", "--verbose", action="store_true", help="verbose output")
    argparser.add_argument("-m", "--model", type=str, default="gpt-4o-mini", help="model name")
    argparser.add_argument("-d", "--dir", type=str, default="responses", help="output directory for responses")
    args = argparser.parse_args()

    _api_key = os.environ.get("OPENAI_API_KEY")
    if _api_key:
        openai.api_key = _api_key
    else:
        raise RuntimeError ("API key is not specified. Please set the environment variable OPENAI_API_KEY.")

    if not os.path.isdir(args.dir):
        if os.path.exists(args.dir):
            raise RuntimeError (f"Another file {args.dir} is found, so output cannot be stored there. Abort.")
        else:
            os.makedirs(args.dir)

    _id = '{}_{}'.format(datetime.datetime.now().strftime("%Y%m%d_%H%M%S.%f"), uuid.uuid4())
    response = openai.chat.completions.create(
            model = args.model,
            messages = [
                {'role': "system", 'content': "あなたはプロの翻訳者です。与えられた英文を日本語に翻訳してください。"},
                {'role': "user", 'content': "私の名前は中野です。中野駅の近くに住んで十五年経ちました。"}
                ]
            )

    with open(f"{args.dir}/{_id}.pkl", 'wb') as wf:
        pickle.dump(response, wf)

    print (f"Success! Response dumped into {args.dir}/{_id}.pkl.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt as e:
        sys.exit(1)
    except Exception as e:
        raise e
