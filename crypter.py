#!/bin/python
import argparse
import binascii

def main():
  method, sinput = get_args()
  algo = switch_algo(method)
  soutput = algo(sinput)
  print(soutput)

##########
# methods
##########

def get_args():
  parser = argparse.ArgumentParser(
      description=f'converts a string into binary/hex',
      epilog='python crypter.py binary string')
  parser.add_argument(
      'method', type=str, help='output format')
  parser.add_argument(
      'input', type=str, help='input string')
  args = parser.parse_args()
  return(args.method, args.input)

def switch_algo(method):
  dict_algo = {
    'binary': StrToBin,
    'hex': StrToHex,
  }
  algo = dict_algo[method]
  return(algo)

def StrToBin(string):
  sBinArray = [format(x, 'b') for x in bytearray(string, encoding="utf-8")]
  out = ""
  for sBin in sBinArray:
    while len(sBin) < 8:
      sBin = "0" + sBin
    out += sBin
  return out

def StrToHex(string):
  bString = bytes(string, "utf-8")
  asciiBin = binascii.hexlify(bString)
  sString = asciiBin.decode("utf-8")
  return sString

def BinToDec(string):
  num = int(string, 2)
  return str(num)

def IntToHex(iNum):
  hexNum = hex(iNum)
  return str(hexNum)

##########
# call
##########

if __name__ == "__main__":
    main()
