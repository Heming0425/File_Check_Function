import pandas as pd
import numpy as np
import openpyxl
from openpyxl import Workbook
import os
import csv

class SaveExcel:

    def __init__(self, filename):
        self.filename = filename
        self.data = Workbook()
        self.table = self.data.get_sheet_by_name(self.data.get_sheet_names()[0])
    
    def addata(self, data):
        self.table.append(data)
    
    def closefile(self):
        self.data.save(self.filename)

def checkFunction(basefile, checkfile, keyid, namelist, outfile):

    basef = pd.read_excel(basefile)
    checkf = pd.read_excel(checkfile)

    outSuccess = outfile + "/" + "output.xlsx"
    outError = outfile + "/" + "error.csv"

    saveExcel = SaveExcel(outSuccess)

    # colnames
    nS = []
    nS.append(keyid)
    for n in namelist:
        n1 = n
        n2 = n + "_提取"
        nm = "校对"
        nS.append(n1)
        nS.append(n2)
        nS.append(nm)

    # output file
    saveExcel.addata(nS)

    # check
    for i in range(basef.shape[0]):

        fileid = basef.loc[i, keyid]
        outline = checkf[checkf[keyid] == fileid]

        tmSave = []
        tmSave.append(fileid)
        if outline.shape[0] != 0:
            for j in namelist:
                s1 = str(basef.loc[i, j]).replace(" ","").replace("（","(").replace("）","(").replace("，",",")
                s2 = str(list(outline[j])[0]).replace(" ","").replace("（","(").replace("）","(").replace("，",",")
                tmSave.append(s1)
                tmSave.append(s2)
                if s1 == s2 or s1 in s2 or s2 in s1:
                    tmSave.append("True")
                else:
                    tmSave.append("False")
            saveExcel.addata(tmSave)
        else:
            tmSave = []
            tmSave.append(fileid)
            with open(outError, "a", encoding="utf-8-sig") as csvf:
                c = csv.writer(csvf)
                c.writerow(tmSave)
    
    saveExcel.closefile()