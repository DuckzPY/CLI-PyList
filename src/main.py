# Import libraries

import os
import sys
import pickle
import argparse
import typing


# Import modules

import logo

# Create argument parser
parser = argparse.ArgumentParser()
parser.parse_args()

parser.add_argument("--file", "-f")
parser.add_argument("--new", "-n")
parser.add_argument("--remove", "-rm")
parser.add_argument("--read", "-r")
parser.add_argument("--open", "-o")
parser.add_argument("--config", "-cfg")
parser.add_argument("--edit", "-e")
parser.add_argument("--tag", "-t")
parser.add_argument("--done", "-d")
parser.add_argument("--undone", "-ud")
parser.add_argument("--sort", "-s")
parser.add_argument("--priority", "-p")
parser.add_argument("--open", "-o")
parser.add_argument("--clear", "-c")
parser.add_argument("--export", "-ex")
parser.add_argument("--import", "-i")
parser.add_argument("--version", "-v")


args = parser.parse_args()
print(args)