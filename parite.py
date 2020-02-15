#! /usr/bin/env python3
# coding: utf-8

import analysis.xml as x_an
import analysis.csv as c_an

import os

def launch_analysis(data_file):
    directory = os.path.dirname(os.path.dirname(__file__)) # we get the right path.

def main():
    c_an.launch_analysis('current_mps.csv')
    x_an.launch_analysis('SyceronBrut.xml')

if __name__ == "__main__":
    main()