import argparse
import json
import re

parser = argparse.ArgumentParser(description='Преобразует список заболеваний в МКБ 10')
parser.add_argument('--tsv', metavar='FILE', type=str, help='Path to a geonames TSV export file.')
parser.add_argument('--limit', metavar='N', type=int, help='Only use first N matching cities.')

args = parser.parse_args()

limit = args.limit
dict = {}

pattern = re.compile('.*[A-Z].*')

with open(args.tsv) as f:
    for line in f:
        if limit == 0: break

        columns = line.rstrip().split(',')

        id = columns[1][1:-1]

        if not pattern.match(id): continue

        title = columns[3][1:-1]
        keywords = []
        words = title.split()

        for word in words:
            for n in range(1, len(word) + 1):
                keywords.append(word[0:n].lower())

        dict[id] = {
            'title': title,
            'score': 1,
            'keywords': keywords,
        }

        if limit != None:
            limit -= 1

print(json.dumps(dict))
