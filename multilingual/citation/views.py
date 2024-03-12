from django.shortcuts import render
from django.http import HttpResponse
import openpyxl,os
from django.conf import settings

# Create your views here.
def home(request):
    return HttpResponse("<a href='sindhi/'>Sindhi</a> <br> <a href='northeast/'>North East</a> <br> <a href='malayalam/'>Malayalam</a>")

def library(request,lib):
    # Assuming 'your_file.xlsx' is the name of your Excel file in the 'static' directory
    excel_file_path = os.path.join(settings.BASE_DIR, f'citation/static/citation/{lib}.xlsx')

    # Open the Excel file
    workbook = openpyxl.load_workbook(excel_file_path)

    # Assuming the data is in the first sheet (index 0)
    sheet = workbook.worksheets[0]
    headings = [cell.value for cell in sheet[1]]
    data = []
    flag=False
    if request.method=="POST":
        flag=True
        searched=request.POST.get("search")
        for row in sheet.iter_rows(min_row=2, values_only=True):
            if searched in row[0]:
                row_data = {
                    'column1': row[0],
                    'column2': row[1],
                    'column3': row[2],
                    'column4': row[3],
                    'column5': row[4],
                    'column6': row[5],
                    'column7': row[6],
                }
                data.append(row_data)
        # return render(request, 'citation/index.html',{'data':data, 'heads':headings})
    else:

        for row in sheet.iter_rows(min_row=2, values_only=True):
            # Assuming each row has data in all 6 columns
            row_data = {
                'column1': row[0],
                'column2': row[1],
                'column3': row[2],
                'column4': row[3],
                'column5': row[4],
                'column6': row[5],
                'column7': row[6],
            }
            data.append(row_data)

    return render(request, 'citation/index.html',{'data':data, 'heads':headings, 'flag':flag, 'lib':lib})
