from typing import List
import random
import argparse

from constants import feature_count, substance_count

parser = argparse.ArgumentParser(description='Генерирует случайные данные в качестве входных для обучения.')
parser.add_argument('--tsv', metavar='FILE', type=str, help='Путь для записи.')
parser.add_argument('--count', metavar='N', type=int, help='Количество.')

args = parser.parse_args()

def generate(filename: str, count: int) -> None:
    random.seed()
    lines = []

    with open(filename, 'w') as f:
        for n in range(0, count):
            [inputs, outputs] = generate_one()
            f.write('\t'.join(str(x) for x in inputs) + '\t' + '\t'.join(str(x) for x in outputs) + '\n')

def generate_one() -> List:
    inputs = []

    for n in range(0, feature_count):
        inputs.append(random.random())

    for n in range(0, substance_count):
        inputs.append(random.random())

    outputs = [random.random()]

    return [inputs, outputs]


generate('data.tsv', args.count)
