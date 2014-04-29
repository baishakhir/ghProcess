import sys
import os



def parse_csv(csv_doc):
    input_file = open(csv_doc, 'r')
    for line in input_file:
        if not line.startswith('|'):
            continue

        col = line.split('|')
        print "git clone " , col[-2]
        #print "|".join((c.strip() for c in col[1:len(col)-1]))

#imput the csvs from bq result: lang_stat.py
if __name__ == "__main__":
    csv_dir = sys.argv[1]
    for root, dirs, files in os.walk(csv_dir):
            for file in files:
                if file.endswith("java.csv"):
                     csv_doc = os.path.join(root, file)
                     parse_csv(csv_doc)
