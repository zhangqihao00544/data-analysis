import openpyxl

with open('data/data.txt', 'r') as f:
    valus = f.readlines()

wb = openpyxl.Workbook()
sheet = wb.active
sheet.append(['satisfaction_level', 'last_evaluation', 'number_project', 'average_montly_hours', 'time_spend_company', 'Work_accident', 'left', 'promotion_last_5years', 'Department', 'salary'])
table = []
row = []
i = 0
while i < (len(valus)):
    row = [x.replace('\n', '') for x in valus[i: i + 10]]
    i += 10
    sheet.append(row)
wb.save('data/HR_comma_sep.xlsx')
