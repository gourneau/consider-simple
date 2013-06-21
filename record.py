# -*- coding: utf-8 -*-

from optparse import OptionParser
import sys

from consider import Consider


def record(out):
    con = Consider()
    for p in con.packet_generator():
        #data = map(str, [p.low_alpha, p.high_alpha, p.low_beta, p.high_beta])
        #out.write(','.join(data))
        out.write(str(p))
        #print(p)


def main():
    parser = OptionParser(usage='%prog [options]')
    parser.add_option('-f', '--file',
                      action='store', type='string', dest='filename')
    options, args = parser.parse_args()

    out = open("brain.txt", 'w+')

    try:
        record(out)
    except KeyboardInterrupt:
        if hasattr(out, 'close'):
            out.close()


if __name__ == '__main__':
    main()
