import openpyxl as xl
wb = xl.load_workbook('Employees.xlsx')
print('Type of wb:', type(wb))
print('Active worksheet object :', wb.active)
print('Worksheet names :', wb.sheetnames)
print('Worksheet objetcs :', wb.worksheets)
ws = wb['Emp']
print('Type of ws:', type(ws))

''this a document''