#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import hashlib
import binascii
import os
__version__ = '0.4'
show_ver = ['version', '-version', '--version', '--v', '-v']
crc_case = 'upper'


def show_help():
    print('sumtool '+__version__+' by Ivan Ignatenko\n'
          '\n'
          'Usage:\n'
          'sumtool <mode> -{algorithm} [file1 or checksum] [file2 or checksum]\n'
          '\n'
          '<Modes>:\n'
          '  c    Comparison mode (Compare two files)\n'
          '  v    Verification mode (Verify file by checksum)\n'
          '  g    Generation mode (Generate checksum of file)\n'
          '\n'
          '{Algorithms}:\n'
          '  md5 (Default)\n'
          '  sha1\n'
          '  sha224\n'
          '  sha256\n'
          '  sha384\n'
          '  sha512\n'
          '  crc32\n')


def md5(file):
    hasher = hashlib.md5()
    block_size = 65536
    with open(file, 'rb') as f:
        while True:
            data = f.read(block_size)
            if not data:
                break
            hasher.update(data)
    return hasher.hexdigest()


def sha1(file):
    hasher = hashlib.sha1()
    block_size = 65536
    with open(file, 'rb') as f:
        while True:
            data = f.read(block_size)
            if not data:
                break
            hasher.update(data)
    return hasher.hexdigest()


def sha224(file):
    hasher = hashlib.sha224()
    block_size = 65536
    with open(file, 'rb') as f:
        while True:
            data = f.read(block_size)
            if not data:
                break
            hasher.update(data)
    return hasher.hexdigest()


def sha256(file):
    hasher = hashlib.sha256()
    block_size = 65536
    with open(file, 'rb') as f:
        while True:
            data = f.read(block_size)
            if not data:
                break
            hasher.update(data)
    return hasher.hexdigest()


def sha384(file):
    hasher = hashlib.sha384()
    block_size = 65536
    with open(file, 'rb') as f:
        while True:
            data = f.read(block_size)
            if not data:
                break
            hasher.update(data)
    return hasher.hexdigest()


def sha512(file):
    hasher = hashlib.sha512()
    block_size = 65536
    with open(file, 'rb') as f:
        while True:
            data = f.read(block_size)
            if not data:
                break
            hasher.update(data)
    return hasher.hexdigest()


def crc32(file):
    buf = open(file, 'rb').read()
    buf = (binascii.crc32(buf) & 0xFFFFFFFF)
    if crc_case == 'lower':
        return ("%08X" % buf).lower()
    return "%08X" % buf


def crc_format(obj):
    if crc_case[:1] == 'l':
        return obj.lower()
    else:
        return obj.upper()


if len(sys.argv) > 1:
    if len(sys.argv) == 4:
        try:
            if sys.argv[1] == 'c' or sys.argv[1] == '-c':
                result1 = md5(sys.argv[2])
                result2 = md5(sys.argv[3])
                if result1 == result2:
                    print('\nChecksums match.\n')
                    print(str('SUM: ' + result1))
                    print(' ')
                else:
                    print('\nChecksums mismatch found.\n')
                    print(str('SUM1: ' + result1))
                    print(str('SUM2: ' + result2))
                    print(' ')
            elif sys.argv[1] == 'v' or sys.argv[1] == '-v':
                replace = False
                if os.path.isfile(sys.argv[3]) and not os.path.isfile(sys.argv[2]):
                    sys.argv[2], sys.argv[3] = sys.argv[3], sys.argv[2]
                    replace = True

                result1 = md5(sys.argv[2])
                result2 = sys.argv[3]
                if result1 == result2:
                    print('\nChecksums match.\n')
                    print(str('SUM: ' + result1))
                    print(' ')
                else:
                    print('\nChecksums mismatch found.\n')
                    if replace:
                        result1, result2 = result2, result1
                    print(str('SUM1: ' + result1))
                    print(str('SUM2: ' + result2))
                    print(' ')

            elif sys.argv[1] == 'g' or sys.argv[1] == '-g':
                if sys.argv[2] == '-md5':
                    result1 = md5(sys.argv[3])
                    print('\nMD5: ' + result1 + '\n')

                elif sys.argv[2] == '-sha1' or sys.argv[2] == '-sha' or sys.argv[2] == '-1':
                    result1 = sha1(sys.argv[3])
                    print('\nSHA1: ' + result1 + '\n')

                elif sys.argv[2] == '-sha224' or sys.argv[2] == '-224':
                    result1 = sha224(sys.argv[3])
                    print('\nSHA224: ' + result1 + '\n')

                elif sys.argv[2] == '-sha256' or sys.argv[2] == '-256':
                    result1 = sha256(sys.argv[3])
                    print('\nSHA256: ' + result1 + '\n')

                elif sys.argv[2] == '-sha384' or sys.argv[2] == '-384':
                    result1 = sha384(sys.argv[3])
                    print('\nSHA384: ' + result1 + '\n')

                elif sys.argv[2] == '-sha512' or sys.argv[2] == '-512':
                    result1 = sha512(sys.argv[3])
                    print('\nSHA512: ' + result1 + '\n')

                elif sys.argv[2] == '-crc32' or sys.argv[2] == '-crc':
                    result1 = crc32(sys.argv[3])
                    print('\nCRC32: ' + crc_format(result1) + '\n')

        except IOError:
            if os.name == 'nt':
                print('No such file or checksum\n')
            else:
                print('\033[4mNo such file or checksum\033[0m\n')
            show_help()

    elif len(sys.argv) == 3 and (sys.argv[1] == 'g' or '-g'):
        try:
            result1 = md5(sys.argv[2])
            print('\nMD5: ' + result1 + '\n')

        except IOError:
            if os.name == 'nt':
                print('No such file or checksum\n')
            else:
                print('\033[4mNo such file or checksum\033[0m\n')
            show_help()

    elif len(sys.argv) == 5:
        try:
            if sys.argv[1] == 'c' or sys.argv[1] == '-c':
                if sys.argv[2] == '-md5':
                    result1 = md5(sys.argv[3])
                    result2 = md5(sys.argv[4])
                    if result1 == result2:
                        print('\nChecksums match.\n')
                        print(str('SUM: ' + result1))
                        print(' ')
                    else:
                        print('\nChecksums mismatch found.\n')
                        print(str('SUM1: ' + result1))
                        print(str('SUM2: ' + result2))
                        print(' ')

                elif sys.argv[2] == '-sha1' or sys.argv[2] == '-sha' or sys.argv[2] == '-1':
                    result1 = sha1(sys.argv[3])
                    result2 = sha1(sys.argv[4])
                    if result1 == result2:
                        print('\nChecksums match.\n')
                        print(str('SUM: ' + result1))
                        print(' ')
                    else:
                        print('\nChecksums mismatch found.\n')
                        print(str('SUM1: ' + result1))
                        print(str('SUM2: ' + result2))
                        print(' ')

                elif sys.argv[2] == '-sha224' or sys.argv[2] == '-224':
                    result1 = sha224(sys.argv[3])
                    result2 = sha224(sys.argv[4])
                    if result1 == result2:
                        print('\nChecksums match.\n')
                        print(str('SUM: ' + result1))
                        print(' ')
                    else:
                        print('\nChecksums mismatch found.\n')
                        print(str('SUM1: ' + result1))
                        print(str('SUM2: ' + result2))
                        print(' ')

                elif sys.argv[2] == '-sha256' or sys.argv[2] == '-256':
                    result1 = sha256(sys.argv[3])
                    result2 = sha256(sys.argv[4])
                    if result1 == result2:
                        print('\nChecksums match.\n')
                        print(str('SUM: ' + result1))
                        print(' ')
                    else:
                        print('\nChecksums mismatch found.\n')
                        print(str('SUM1: ' + result1))
                        print(str('SUM2: ' + result2))
                        print(' ')

                elif sys.argv[2] == '-sha384' or sys.argv[2] == '-384':
                    result1 = sha256(sys.argv[3])
                    result2 = sha256(sys.argv[4])
                    if result1 == result2:
                        print('\nChecksums match.\n')
                        print(str('SUM: ' + result1))
                        print(' ')
                    else:
                        print('\nChecksums mismatch found.\n')
                        print(str('SUM1: ' + result1))
                        print(str('SUM2: ' + result2))
                        print(' ')

                elif sys.argv[2] == '-sha512' or sys.argv[2] == '-512':
                    result1 = sha512(sys.argv[3])
                    result2 = sha512(sys.argv[4])
                    if result1 == result2:
                        print('\nChecksums match.\n')
                        print(str('SUM: ' + result1))
                        print(' ')
                    else:
                        print('\nChecksums mismatch found.\n')
                        print(str('SUM1: ' + result1))
                        print(str('SUM2: ' + result2))
                        print(' ')

                elif sys.argv[2] == '-crc32' or sys.argv[2] == '-crc':
                    result1 = crc32(sys.argv[3])
                    result2 = crc32(sys.argv[4])
                    if result1 == result2:
                        print('\nChecksums match.\n')
                        print(str('SUM: ' + result1))
                        print(' ')
                    else:
                        print('\nChecksums mismatch found.\n')
                        print(str('SUM1: ' + result1))
                        print(str('SUM2: ' + result2))
                        print(' ')

            elif sys.argv[1] == 'v' or sys.argv[1] == '-v':
                replace = False
                if os.path.isfile(sys.argv[4]) and not os.path.isfile(sys.argv[3]):
                    sys.argv[3], sys.argv[4] = sys.argv[4], sys.argv[3]
                    replace = True

                if sys.argv[2] == '-md5':
                    result1 = md5(sys.argv[3])
                    result2 = sys.argv[4]
                    if result1 == result2:
                        print('\nChecksums match.\n')
                        print(str('SUM: ' + result1))
                        print(' ')
                    else:
                        print('\nChecksums mismatch found.\n')
                        if replace:
                            result1, result2 = result2, result1
                        print(str('SUM1: ' + result1))
                        print(str('SUM2: ' + result2))
                        print(' ')

                elif sys.argv[2] == '-sha1' or sys.argv[2] == '-sha' or sys.argv[2] == '-1':
                    result1 = sha1(sys.argv[3])
                    result2 = sys.argv[4]
                    if result1 == result2:
                        print('\nChecksums match.\n')
                        print(str('SUM: ' + result1))
                        print(' ')
                    else:
                        print('\nChecksums mismatch found.\n')
                        if replace:
                            result1, result2 = result2, result1
                        print(str('SUM1: ' + result1))
                        print(str('SUM2: ' + result2))
                        print(' ')

                elif sys.argv[2] == '-sha224' or sys.argv[2] == '-224':
                    result1 = sha224(sys.argv[3])
                    result2 = sys.argv[4]
                    if result1 == result2:
                        print('\nChecksums match.\n')
                        print(str('SUM: ' + result1))
                        print(' ')
                    else:
                        print('\nChecksums mismatch found.\n')
                        if replace:
                            result1, result2 = result2, result1
                        print(str('SUM1: ' + result1))
                        print(str('SUM2: ' + result2))
                        print(' ')

                elif sys.argv[2] == '-sha256' or sys.argv[2] == '-256':
                    result1 = sha256(sys.argv[3])
                    result2 = sys.argv[4]
                    if result1 == result2:
                        print('\nChecksums match.\n')
                        print(str('SUM: ' + result1))
                        print(' ')
                    else:
                        print('\nChecksums mismatch found.\n')
                        if replace:
                            result1, result2 = result2, result1
                        print(str('SUM1: ' + result1))
                        print(str('SUM2: ' + result2))
                        print(' ')

                elif sys.argv[2] == '-sha384' or sys.argv[2] == '-384':
                    result1 = sha384(sys.argv[3])
                    result2 = sys.argv[4]
                    if result1 == result2:
                        print('\nChecksums match.\n')
                        print(str('SUM: ' + result1))
                        print(' ')
                    else:
                        print('\nChecksums mismatch found.\n')
                        if replace:
                            result1, result2 = result2, result1
                        print(str('SUM1: ' + result1))
                        print(str('SUM2: ' + result2))
                        print(' ')

                elif sys.argv[2] == '-sha512' or sys.argv[2] == '-512':
                    result1 = sha512(sys.argv[3])
                    result2 = sys.argv[4]
                    if result1 == result2:
                        print('\nChecksums match.\n')
                        print(str('SUM: ' + result1))
                        print(' ')
                    else:
                        print('\n Checksums mismatch found.\n')
                        if replace:
                            result1, result2 = result2, result1
                        print(str('SUM1: ' + result1))
                        print(str('SUM2: ' + result2))
                        print(' ')

                elif sys.argv[2] == '-crc32' or sys.argv[2] == '-crc':
                    result1 = crc32(sys.argv[3])
                    result2 = sys.argv[4]
                    if result1.lower() == result2.lower():
                        print('\nChecksums match.\n')
                        print(str('SUM: ' + result1))
                        print(' ')
                    else:
                        print('\nChecksums mismatch found.\n')
                        if replace:
                            result1, result2 = result2, result1
                        print(str('SUM1: ' + result1))
                        print(str('SUM2: ' + crc_format(result2)))
                        print(' ')

        except IOError:
            if os.name == 'nt':
                print('No such file or checksum\n')
            else:
                print('\033[4mNo such file or checksum\033[0m\n')
            show_help()
    elif 1 < len(sys.argv) < 4:
        if sys.argv[1] in show_ver:
            print('sumtool ' + __version__)
        else:
            show_help()
else:
    show_help()
