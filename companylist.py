import xlrd


workbook = xlrd.open_workbook(r'E:\1.xlsx')
sheet1 = workbook.sheet_by_index(0)
list = sheet1.col_values(0)
print(list)