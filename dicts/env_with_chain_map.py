import argparse
import os
from collections import ChainMap

defaults = {"debug": False}

parser = argparse.ArgumentParser()
parser.add_argument('--debug')
args = parser.parse_args()
cli_args = {key:value for key, value in vars(args).items() if value}

config = ChainMap(cli_args, os.environ, defaults)

print(config.get('debug'))
