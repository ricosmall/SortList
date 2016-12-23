#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import re
from numbertrans import chineseToNumber

def sortNames(arr):
    def changeToSort(item):
        regChn = re.compile(r'([零|一|二|三|四|五|六|七|八|九|十|百]+)')
        regNum = re.compile(r'([0-9]+)')

        if regNum.search(item) != None:
            itemnum = int(re.sub(r'\D', '', item))
        elif regChn.search(item) != None:
            chnNum = regChn.search(item).group()
            itemnum = chineseToNumber(chnNum)
        else:
            pass

        return itemnum

    resultlist = sorted(arr, key=lambda item: changeToSort(item))

    return resultlist
