import configparser
from main import read_file


config = configparser.ConfigParser()
config.read('config.ini')


source_filename = config.get('source', 'filename')
destination_filename = config.get('destination', 'filename')

content = read_file(source_filename)

keys = content[0].split()
values = content[1].split()
with open(destination_filename, 'w') as f:
    f.write(','.join(keys) + '\n')
    f.write(','.join(values) + '\n')
