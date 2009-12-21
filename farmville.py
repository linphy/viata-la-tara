#!/usr/bin/env python
import logging
from optparse import OptionParser
import sys
import mousecontrol

# FarmVille constants
# for zoom level 1 whatever that is
XDIST = 25
YDIST = 12

def parse_options():
    parser = OptionParser()
    parser.set_defaults(zoom=1, log_level=logging.WARN)
    parser.add_option('-z', '--zoom',
                      type='int', dest='zoom',
                      help='zoom level: 1 - 4')
    parser.add_option('-v', '--verbose',
                      action='store_const', const=logging.INFO, dest='log_level',
                      help='set logging level to INFO')
    parser.add_option('--debug',
                      action='store_const', const=logging.DEBUG, dest='log_level',
                      help='set logging level to DEBUG')
    return parser.parse_args()

def main():
    options, args = parse_options()
    nrows, ncols = (int(x) for x in args)
    logging.basicConfig(level=options.log_level)
    logging.debug('zoom = %d, ncols = %d, nrows = %d' % (options.zoom, ncols, nrows))

if __name__ == '__main__':
    main()
