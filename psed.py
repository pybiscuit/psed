import sys
import argparse
import re

parser = argparse.ArgumentParser(description='python implemented sed')
parser.add_argument('script', type=str, action='store')
parser.add_argument('files', type=str, action='store', nargs='?')
parser.add_argument('-r', action='store_true')

args = parser.parse_args()

def split_script(script):
    return script.split('/')

def get_input():
    userin = input(">>> ")
    return userin

split = split_script(args.script)


if args.r:
    if not args.files:
        reg_in = get_input()
        print(re.sub(split[1], split[2], reg_in))
    else:
        with open(args.files, 'r') as f:
            for line in f:
                if len(re.findall(split[1], line)) > 0:
                    print(re.sub(split[1], split[2], line))

if not args.files:
    std_in = get_input()

    print(std_in.replace(split[1], split[2]))
else:
    with open(args.files, 'r') as f:
        for line in f:
            if split[1] in line:
                print(line.replace(split[1], split[2]))

