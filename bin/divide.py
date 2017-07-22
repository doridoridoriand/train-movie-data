import cv2
import numpy as np
import argparse
import os
import logging

parser = argparse.ArgumentParser(description = 'Convert movie to sequence of images.')
parser.add_argument('filename',
                    action = 'store',
                    nargs = None,
                    const = None,
                    default = None,
                    type = str,
                    choices = None,
                    help = 'Please input source movie filename',
                    metavar = None)
parser.add_argument('-p', '--additional-prefix',
                    action = 'store',
                    nargs = '?',
                    const = None,
                    default = None,
                    type = str,
                    choices = None,
                    help = 'Add additional prefix if you need.',
                    metavar = None)
arguments = parser.parse_args()

logging.basicConfig(filename = 'app.log',
                    level = logging.DEBUG,
                    format = '%(asctime)s %(message)s',
                    datefmt = '%m/%d/%Y %I:%M:%S %p')
logging.info('Start to divide movie file: ' + arguments.filename)

cap = cv2.VideoCapture('../source/' + arguments.filename)

if arguments.additional_prefix == None:
    arguments.additional_prefix = ''

i = 0
while(cap.isOpened()):
    flag, frame = cap.read()

    if flag == False:
        break

    cv2.imwrite('../image/' +
                arguments.additional_prefix +
                arguments.filename.split(".")[0] +
                '%s' % str(i).zfill(10) + '.png', frame)
    logging.info('FRAME: ' + arguments.additional_prefix + '-%s' % str(i).zfill(10) + 'saved.')
    i += 1

