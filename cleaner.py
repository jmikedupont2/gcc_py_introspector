from toolz.curried import *
import json
import click
import splitter

@click.command()
@click.argument('input-file', type=click.File('r'))
@click.argument('output-file', type=click.File('w'))
def main (input_file, output_file):
    data = json.load(input_file)
    res = { 'nodes' : [] }
    for x in data['nodes']:
        y = splitter.clean(x)
        res['nodes'].append(y)
    json.dump(res, output_file)

#out_degrees = countby(first,  edges)
if __name__ == '__main__':
    main()
