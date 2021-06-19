import argparse
import json
import re

parser = argparse.ArgumentParser(description='Converts geonames cities to JSON suitable for Firebase import')
parser.add_argument('--tsv', metavar='FILE', type=str, help='Path to a geonames TSV export file.')
#parser.add_argument('--countries', metavar='COUNTRIES', type=str, help='Comma-separated list of 2-letter country codes. Default: all countries.')
#parser.add_argument('--skip_cities', metavar='CITIES', type=str, help='Comma-separated list of city names to skip.', default='')
parser.add_argument('--limit', metavar='N', type=int, help='Only use first N matching cities.')

args = parser.parse_args()

#countries = []
#all_countries = (args.countries == None)
#if not all_countries:
    #countries = args.countries.split(',')

#skip_cities_with_empty = args.skip_cities.split(',')
#skip_cities = [c for c in skip_cities_with_empty if c]
all_countries = None

limit = args.limit
dict = {}

#pattern = re.compile('[A-Z]')
pattern = re.compile('.*[A-Z].*')

#print(pattern.match("123"))
#print(pattern.match("123A"))
#die;

with open(args.tsv) as f:
    for line in f:
        if limit == 0: break

        columns = line.rstrip().split(',')

        #if not all_countries:
            #country = columns[8]
            #if not country in countries: continue

        id = columns[1][1:-1]

        #print(pattern.match(id))
        if not pattern.match(id): continue

        title = columns[3][1:-1]
        keywords = []
        words = title.split()

        for word in words:
            for n in range(1, len(word) + 1):
                keywords.append(word[0:n].lower())
        #if title in skip_cities: continue

        dict[id] = {
            'title': title,
            'score': 1,
            'keywords': keywords,
        }

        if limit != None:
            limit -= 1

print(json.dumps(dict))
