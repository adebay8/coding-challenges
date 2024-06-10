import argparse
import os
import sys
import io

parser = argparse.ArgumentParser()
parser.add_argument("file", help="path to the file", nargs='?', default=sys.stdin)
parser.add_argument("-c", help="number of bytes in the file", action="store_true")
parser.add_argument("-l", help="number of lines in the file", action="store_true")
parser.add_argument("-w", help="number of words in the file", action="store_true")
parser.add_argument("-m", help="number of characters in the file", action="store_true")

args = parser.parse_args()

result = ""

if not any(list(vars(args).values())[1:]):
    args.c, args.l, args.w, args.m = True, True, True, True

f = args.file if isinstance(args.file, io.IOBase) else open(args.file)

content = f.read()

if args.c: 
    if f.seekable():
        f.seek(0, os.SEEK_END)
        result += f"\t{f.tell()}"
    else:
        result += f"\t{len(content.encode('utf-8'))}"

if args.l:
    line_count = content.count('\n')
    result += f"\t{line_count}"

if args.w:
    word_count = len(content.split())
    result += f"\t{word_count}"
        
if args.m:
    char_count = len(content)
    result += "\t{}".format(char_count)

print(f"{result} {args.file if isinstance(args.file, str) else ''}")

if not isinstance(args.file, io.IOBase):
    f.close()