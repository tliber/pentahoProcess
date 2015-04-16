import re
import sys


def main(PentahoLog):
  processes = re.findall('pentaho\s+(\d+).*\n', PentahoLog.decode())
  print (processes)
  return processes
if __name__ == '__main__':
  fin = open(sys.argv[1], 'rb')
  text = fin.read()
  main(text)