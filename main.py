
import xlrd
import json

class wordsearch():
    wordlist = []
    ignoreword = []
    def __init__(self):
        print("hello")
        pass
    def saveWordDummy(self):
        xl_workbook = xlrd.open_workbook("./basicword.xls")
        xl_sheet = xl_workbook.sheet_by_index(0)
        ncol = xl_sheet.ncols
        nrow = xl_sheet.nrows
        for i in range(1, nrow):
            if xl_sheet.row_values(i)[3] == "중고":
                self.wordlist.append(xl_sheet.row_values(i))

        with open("wordlist.txt", 'w') as outfile:
            json.dump(self.wordlist, outfile)
    def loadWordlist(self):
        with open("wordlist.txt", "r") as json_file:
            self.wordlist = json.load(json_file)
        pass
    def process_srt(self):
        self.loadWordlist()
        f = open("p1.srt", 'r')
        srt = f.readlines()
        found = 0
        for i in range(len(srt)):
            if i % 4 == 2:
                splited = srt[i].split(" ")
                for sp in splited:
                    for w in self.wordlist:
                        if sp == w[1] or sp == w[4] or sp == w[5]:
                            found = 1
                            break
                    if found == 1:
                        print("_____", end=' ')
                        self.ignoreword.append(sp)
                        found = 0
                    else:
                        print(sp, end=' ')
        print("remember list: ", self.ignoreword)
        with open("ignore.txt", 'w') as outfile:
            json.dump(self.ignoreword, outfile)






        pass







ws = wordsearch()
ws.process_srt()


