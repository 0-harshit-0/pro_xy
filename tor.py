import os
import argparse

import stem.process
from stem.util import term

# Initialize parser
parser = argparse.ArgumentParser()

# Adding optional argument
parser.add_argument("-p", "--Port", help = "Port number", default = 65432)
parser.add_argument("-pl", "--Platform", help = "Platform", default = 0) # 0-linux, 1-windows
parser.add_argument("-t", "--Timeout", help = "IP change timeout in seconds", default = 60) # 60 seconds

# Read arguments from command line
args = parser.parse_args()

if args.Platform:
  # windows
  TOR_PATH = os.path.normpath("path\\to\\tor.exe")
else:
  # linux
  TOR_PATH = "tor"


def print_bootstrap_lines(line):
  if "Bootstrapped " in line:
    print(term.format(line, term.Color.BLUE))


print(term.format("Starting Tor:\n", term.Attr.BOLD))

tor_process = stem.process.launch_tor_with_config(
  config = {
    'SocksPort': str(args.Port),
    'MaxCircuitDirtiness': str(args.Timeout),
    'DataDirectory': 'conn'+str(args.Port)
  },
  init_msg_handler = print_bootstrap_lines,
  tor_cmd = TOR_PATH
)

print(term.format("\nChecking our endpoint:\n", term.Attr.BOLD))

