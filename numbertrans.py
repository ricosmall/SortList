#!/usr/bin/env python3
# coding=utf-8


DIC_UNIT = {'十': 10,'拾': 10,'百': 100,'佰': 100,'千': 1000,'仟': 1000,'万': 10000,'萬': 10000,'亿': 100000000,'億': 100000000,'兆': 1000000000000,'京': 10000000000000000,}
DIC_SEC = {'万', '萬', '亿', '億', '兆', '京'}
DIC_NUM = {'零': 0,'〇': 0,'壹': 1,'一': 1,'贰': 2,'二': 2,'两': 2,'叁': 3,'三': 3,'肆': 4,'四': 4,'伍': 5,'五': 5,'陆': 6,'六': 6,'柒': 7,'七': 7,'捌': 8,'八': 8,'玖': 9,'九': 9,}

def chineseToNumber(cnNum):
    result = 0
    section = 0
    number = 0
    position = 0
    def handleSpecialNumThenList(cnNumWords):
        if cnNumWords[0] == '十':
            cnNumWords = '一' + cnNumWords
        posWanYi = cnNumWords.find('万亿') or cnNumWords.find('萬億')
        posYiYi = cnNumWords.find('亿亿') or cnNumWords.find('億億')
        if posWanYi > -1:
            cnNumWords = cnNumWords[0:posWanYi] + '兆' + cnNumWords[posWanYi + 2:]
        if posYiYi > -1:
            cnNumWords = cnNumWords[0:posYiYi] + '京' + cnNumWords[posYiYi + 2:]
        return list(cnNumWords)
    cnNumList = handleSpecialNumThenList(cnNum)
    length = len(cnNumList)
    while position < length:
        cnWord = cnNumList[position]
        if cnWord in DIC_NUM:
            number = DIC_NUM[cnWord]
            position += 1
            if position >= length:
                section += number
                result += section
                break
        else:
            unit = DIC_UNIT[cnWord]
            if cnWord in DIC_SEC:
                section = (section + number) * unit
                result += section
                section = 0
            else:
                section += number * unit
            number = 0
            position += 1
            if position >= length:
                result += section
                break
    return result

LI_NUMCHAR = ['零', '一', '二', '三', '四', '五', '六', '七', '八', '九']
LI_NUMUNIT = ['', '十', '百', '千']
LI_NUMSEC = ['', '万', '亿', '万亿', '亿亿']

def numberToChinese(num):
    chnStr = ''
    unitPos = 0
    strIns = ''
    needZero = False
    def sectionToChinese(secnum, unitStr):
        chnString = unitStr
        strInsert = ''
        unitPosition = 0
        needAddZero = True
        while secnum > 0:
            v = secnum % 10
            if v == 0:
                if not needAddZero:
                    needAddZero = True
                    chnString = LI_NUMCHAR[v] + chnString
            else:
                needAddZero = False
                strInsert = LI_NUMCHAR[v]
                strInsert += LI_NUMUNIT[unitPosition]
                chnString = strInsert + chnString
            unitPosition += 1
            secnum = secnum // 10
        return chnString
    if num == 0:
        chnStr = LI_NUMCHAR[num]
    while num > 0:
        section = num % 10000
        if needZero:
            chnStr = LI_NUMCHAR[0] + chnStr
        strIns = LI_NUMSEC[unitPos] if section != 0 else LI_NUMSEC[0]
        chnStr = sectionToChinese(section, strIns) + chnStr
        needZero = section < 1000 and section > 0
        num = num // 10000
        unitPos += 1
    def handleSpecialChnStr(chn):
        if chn[0:2] == '一十':
            chn = '十' + chn[2:]
        return chn
    chnStr = handleSpecialChnStr(chnStr)
    return chnStr
