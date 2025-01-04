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
    argparser.add_argument("-s", "--system", type=str, metavar="FILE", help="file for the system prompt")
    argparser.add_argument("-S", "--system-prompt", type=str, default="You are a helpful assistant. Please follow the instruction given by the user.", help="system prompt string (ignored when specified -s/--system)")
    argparser.add_argument("-u", "--user", type=str, metavar="FILE", help="file for the user prompt")
    argparser.add_argument("-U", "--user-prompt", type=str, default="Please tell me useful tips for OpenAI API.", help="user prompt string (ignored when specified -u/--user)")
    argparser.add_argument("-a", "--add", type=str, metavar="FILE", help="additional file for the user prompt (to be appended at the end)")
    argparser.add_argument("-o", "--output", type=str, help="output prefix")
    argparser.add_argument("-d", "--dir", type=str, default="responses", help="output directory for responses")
    args = argparser.parse_args()

    _api_key = os.environ.get("OPENAI_API_KEY")
    if _api_key:
        openai.api_key = _api_key
    else:
        raise RuntimeError ("API key is not specified. Please set the environment variable OPENAI_API_KEY.")

    SYSTEM_PROMPT = args.system_prompt
    if args.system:
        with open(args.system, 'rt') as rh:
            SYSTEM_PROMPT = rh.read().rstrip('\n')

    USER_PROMPT = args.user_prompt
    if args.user:
        with open(args.user, 'rt') as rh:
            USER_PROMPT = rh.read().rstrip('\n')
    if args.add:
        with open(args.add, 'rt') as rh:
            USER_PROMPT += '\n==\n' + rh.read().rstrip('\n')


    if not os.path.isdir(args.dir):
        if os.path.exists(args.dir):
            raise NotADirectoryError (f"Another file {args.dir} is found, so output cannot be stored in the specified directory. Abort.")
        else:
            os.makedirs(args.dir)

    _id = args.output if args.output else '{}_{}'.format(datetime.datetime.now().strftime("%Y%m%d_%H%M%S.%f"), uuid.uuid4())

    output = f"{args.dir}/{_id}.pkl"
    if os.path.exists(output):
        raise FileExistsError (f"Output file {output} already exists. Abort.")

    if args.verbose:
        print (f"ID: {_id}", file=sys.stderr)
        print (f"model: {args.model}", file=sys.stderr)
        print (f"output: {output}", file=sys.stderr)
        print (f"system prompt: {SYSTEM_PROMPT}", file=sys.stderr)
        print (f"user prompt: {USER_PROMPT}", file=sys.stderr)

    response = openai.chat.completions.create(
            model = args.model,
            messages = [
                {'role': "system", 'content': SYSTEM_PROMPT},
                {'role': "user", 'content': USER_PROMPT}
                ]
            )

    with open(output, 'wb') as wf:
        pickle.dump(response, wf)

    print (f"Success! Response dumped into {output}.")

    if args.verbose:
        print (response, file=sys.stderr)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt as e:
        sys.exit(1)
    except Exception as e:
        raise e
