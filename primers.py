import sys

def readconsole():
    vendor = input('Enter the Vendor Name:')
    if vendor == '':
        print('Please enter vendor.')
    return vendor


if __name__ == '__main__':
    try:
        vendor = sys.argv[1].upper()
    except:
        vendor = readconsole().upper()
    print(vendor)