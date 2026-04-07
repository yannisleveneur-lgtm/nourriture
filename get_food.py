from food import Food
import argparse

import sys
print("Running script...")

parser = argparse.ArgumentParser("Food Informations")
parser.add_argument('-f', '--food', help="your food name", default='tomate')

# use the parser to get all the needed arguments
# retrieve and display food infos
# save the displayed infos to a csv file
