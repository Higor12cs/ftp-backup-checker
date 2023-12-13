from datetime import datetime
from openpyxl import Workbook
import os

class ExcelHandler:
    def create_excel(self, data, excel_file_name='files.xlsx'):
        workbook = Workbook()
        sheet = workbook.active

        for row, (filename, date_str) in enumerate(data, start=1):
            sheet[f'A{row}'] = filename
            date_obj = datetime.strptime(date_str + " " + str(datetime.now().year), "%b %d %H:%M %Y")
            excel_date_format = date_obj.strftime("%Y-%m-%d %H:%M")
            sheet[f'B{row}'] = excel_date_format

        base_path = os.path.dirname(__file__) 
        spreadsheets_path = os.path.join(base_path, '..', 'spreadsheets', excel_file_name)
        workbook.save(spreadsheets_path)
