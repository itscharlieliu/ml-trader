#!/usr/bin/python
from time import sleep

from trader.trader import Trader
import sys, argparse


def main(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument("api_key")
    args = parser.parse_args()
    api_key = args.api_key

    trader = Trader(api_key)

    for i in range(10):
        trader.update_data()
        print(trader.get_sentiment())
        sleep(1)


if __name__ == '__main__':
    main(sys.argv[1:])
