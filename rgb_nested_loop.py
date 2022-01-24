# !/usr/bin/env python3
# Created By: Jedidiah.
# Date: Jan 22, 2022
# This program Prints RGB color numbers from 0 to 50 of red, green and blue.

def main():
    red = 0
    green = 0
    blue = 0

    for blue in range(1, 51, 1):
        print(" RGB:( {}, {}, {}) ".format(blue, green, red))
        for green in range(1, 51, 1):
            print("RGB: ( {}, {}, {}) ".format(blue, green, red))
            for red in range(1, 51, 1):
                print("RGB: ({}, {}, {} ) ".format(blue, green, red))


if __name__ == "__main__":
    main()
