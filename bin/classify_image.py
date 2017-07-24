from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import arguparse
import os.path
import re
import sys
import tarfile
import numpy as np
from six.moves import urllib
import tensorflow as tf

FLAGS = None

parser = argparse.ArgumentParser(description = 'Classify image')
