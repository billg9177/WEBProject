#!/usr/bin/env python3
"""

"""
import requests
from bs4 import BeautifulSoup
import sys
import os


def readconsole():
    vendor = input('\nEnter the Vendor Name:')
    if vendor == '':
        print('\nPlease enter vendor.  Currently only "Midway and Midsouth" are supported\n')
        sys.exit(99)
    return vendor


def midway():
    """

    :return:
    """
    source = requests.get(
        'https://www.midwayusa.com/primers/br?cid=17587&PersistedItemsPerPage=96').text
    soup = BeautifulSoup(source, 'lxml')

    if ("Mixed Availability" or "Backorder OK" or "Available") not in soup.prettify():
        print('\nMidway is out of stock of all primers\n')
        return "no"
    else:
        source = requests.get('https://www.midwayusa.com/product/953733657').text
        soup = BeautifulSoup(source, 'lxml')
        if "Out of Stock" not in soup.prettify():
            print('Midway has Federal Small Pistol Primers #100')

        source = requests.get('https://www.midwayusa.com/product/953155826?pid=155826').text
        soup = BeautifulSoup(source, 'lxml')
        if "Out of Stock" not in soup.prettify():
            print('Midway has Federal Large Pistol Primers #150')

        source = requests.get('https://www.midwayusa.com/product/953179134').text
        soup = BeautifulSoup(source, 'lxml')
        if "Out of Stock" not in soup.prettify():
            print('Midway has Federal Small Rifle Primers #205')

        source = requests.get('https://www.midwayusa.com/product/953519190?pid=875511').text
        soup = BeautifulSoup(source, 'lxml')
        if "Out of Stock" not in soup.prettify():
            print('Midway has Federal Large Rifle Primers #210')

        return


def midsouth():
    """

    :return:
    """
    source = requests.get(
        'https://www.midsouthshooterssupply.com/dept/reloading/primers?instock=true').text
    soup = BeautifulSoup(source, 'lxml')
    print('\nMidsouth: Checking all primers.')
    if "Sorry! There are no active items in stock for this category" in soup.prettify():
        return "no"
    else:
        source = requests.get(
            'https://www.midsouthshooterssupply.com/dept/reloading/primers/small-pistol?instock=true').text
        soup = BeautifulSoup(source, 'lxml')
        print('\nMidsouth: Checking small-pistol primers.')
        if "Sorry! There are no active items in stock for this category" not in soup.prettify():
            print('\nMidsouth has small pistol primers.')

        source = requests.get(
            'https://www.midsouthshooterssupply.com/dept/reloading/primers/large-pistol?instock=true').text
        soup = BeautifulSoup(source, 'lxml')
        print('\nMidsouth: Checking large-pistol primers.')
        if "Sorry! There are no active items in stock for this category" not in soup.prettify():
            print('\nMidsouth has large pistol primers.')

        source = requests.get(
            'https://www.midsouthshooterssupply.com/dept/reloading/primers/small-rifle?instock=true').text
        soup = BeautifulSoup(source, 'lxml')
        print('\nMidsouth: Checking small-rifle primers.')
        if "Sorry! There are no active items in stock for this category" not in soup.prettify():
            print('\nMidsouth has small rifle primers.')

        source = requests.get(
            'https://www.midsouthshooterssupply.com/dept/reloading/primers/large-rifle?instock=true').text
        soup = BeautifulSoup(source, 'lxml')
        print('\nMidsouth: Checking large-rifle primers.')
        if "Sorry! There are no active items in stock for this category" not in soup.prettify():
            print('\nMidsouth has large rifle primers.')
        return


def brownells():
    return


def main(vendor):
    """

    :param vendor:
    :return:
    """
    if "MIDSOUTH" in vendor:
        yes_no = midsouth()
    elif "MIDWAY" in vendor:
        yes_no = midway()
    else:
        print('Sorry', vendor, 'is not supported.')
        sys.exit()

    if yes_no:
        print("\n**********\n")
        print(vendor.upper())
        os.system('say "Sorry"')
        os.system('say "no Primers in stock"')
        print("\tDoes not have any Primers in stock")
        print("\n**********\n")
    else:
        print("\n**********\n")
        print(vendor.upper())
        os.system('say "Go buy primers"')
        os.system('say "vendor has Primers in stock"')
        print("\tHas Primers in stock")
        print("\n**********\n")


if __name__ == '__main__':
    try:
        vendor = sys.argv[1].upper()
    except:
        vendor = readconsole().upper()
    print(vendor)
    main(vendor)
