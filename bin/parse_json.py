import json
import argparse
import logging
import os

def parse_content(current_file, previous_file):
    content = []
    content.append([json.load(open(current_file,  'r'))])
    content.append([json.load(open(previous_file, 'r'))])
    logging.info(str(content))
    return content

def concat(data):
    result = []
    for entry in data:
        result.append(entry['human_string'])
    # 重複を省くためにlistにsetしている
    return list(set(result))

def difference(content, entry):
    current  = content[0][0].values()
    previous = content[1][0].values()
    matched = list(set(concat(current)) & set(concat(previous)))
    absolute_difference = abs(len(matched) - len(previous))
    logging.info('Frame Number: ' + entry.split('_')[-1].split('.')[0] + ' Absolute Difference: ' + str(absolute_difference))
    print('Frame Number: ' + entry.split('_')[-1].split('.')[0] + ' Absolute Difference: ' + str(absolute_difference))

def absolute_filepath(filepath, filename):
    return filepath + '/' + filename

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Parse JSON.')
    parser.add_argument('directoryname',
                        action = 'store',
                        nargs = None,
                        const = None,
                        default = None,
                        type = str,
                        choices = None,
                        help = 'Please input absolute json directory path.',
                        metavar = None)
    arguments = parser.parse_args()

    logging.basicConfig(filename = 'parse_json.log',
                        level = logging.DEBUG,
                        format = '%(asctime)s %(message)s',
                        datefmt = '%m/%d/%Y %I:%M:%S %p')
    logging.info('Start parse json')

    entries = sorted(os.listdir(arguments.directoryname))

    for index, entry in enumerate(entries):
        if index >= 2:
            #print(entry + entries[index - 1])
            result = parse_content(absolute_filepath(arguments.directoryname, entry),
                                   absolute_filepath(arguments.directoryname, entries[index - 1]))
            difference(result, entry)
            #print(result)
