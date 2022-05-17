import argparse
import sys
import shutil
import os
import nbformat as nbf


def main(): #creo un parser e passo come unico argomento il nome del file
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="what is the file to move?")
    args = parser.parse_args()
    sys.stdout.write(move(args))

directory = os.getcwd()
filenames = os.listdir(directory)

def move(args):
    if args.file in filenames:
        nb = nbf.v4.new_notebook()
        first = """\
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import plotly.express as px
from scipy import stats
pd.set_option("display.max_columns",100)"""

        second = """\
user = str(input("insert file name"))
df = pd.read_csv(user + ".csv")"""

        third = """\
df.head()"""

        nb['cells'] = [nbf.v4.new_code_cell(first),
                       nbf.v4.new_code_cell(second),
                       nbf.v4.new_code_cell(third)]
        nbf.write(nb, args.file.split("_")[0] + '.ipynb')

        name = args.file.split("_")[0]
        folder = os.path.splitext(args.file.split("_")[1])[0]
        if not os.path.isdir(os.path.join(directory,folder)):
                    os.makedirs(os.path.join(directory, folder))
                    shutil.move(os.path.join(directory,args.file),os.path.join(directory,folder))
                    shutil.move(os.path.join(directory, args.file.split("_")[0] + '.ipynb'), os.path.join(directory, folder))
        else:
            shutil.move(os.path.join(directory, args.file), os.path.join(directory, folder))
            shutil.move(os.path.join(directory, args.file.split("_")[0] + '.ipynb'), os.path.join(directory, folder))

    else:
        message = "file does not exist"
        return message


if __name__ == '__main__':
    main()

