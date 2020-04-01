import xlrd


class ExcelDataReader:
    """ Excel Data Reader"""

    def __init__(self, file_path, sheet_name):
        self.file_path = file_path
        self.sheet_name = sheet_name
        wb = xlrd.open_workbook(self.file_path)
        self.sheet = wb.sheet_by_name(self.sheet_name)

    def get_data_sheet(self):
        return self.sheet

    def get_row_count(self):
        print("---- total_row_count ---- ", self.sheet.nrows)
        return self.sheet.nrows

    def get_cell_data(self, row_num, col_num):
        value = self.sheet.cell_value(row_num, col_num)
        return value

    def get_current_test_row(self, test_name):
        current_test_row_num = -1
        row_count = self.get_row_count()
        for r in range(row_count):
            if self.sheet.cell_value(r, 0) == test_name:
                current_test_row_num = r
                break
        return current_test_row_num

    def get_data_sets_count(self, test_name):
        current_test_row_num = self.get_current_test_row(test_name)
        print("---- current_test_row_num ---- ", current_test_row_num)
        sets = 0
        if current_test_row_num != -1:
            first_data_set_row_num = current_test_row_num + 2
            print("---- first_data_set_row_num ---- ", first_data_set_row_num)
            print(self.sheet.cell_type(24, 0))
            print(self.get_cell_data(24, 0))
            # while self.get_cell_data(first_data_set_row_num, 0) != '':
            #     # print("--- cell value--", self.get_cell_data(first_data_set_row_num, 0))
            #     # print("---- cell type ---", self.sheet.cell_type(first_data_set_row_num, 0))
            #     sets += 1
            #     first_data_set_row_num += 1
            #     print("----sets & first row -----", sets, first_data_set_row_num)
            #     print("---- after --- ", self.sheet.cell_type(first_data_set_row_num, 0))
            # return sets
        else:
            print("No such test exist in the test data sheet")

    # def get_test_data(self, test_name):
    #     current_test_row_num = self.get_current_test_row(test_name)
    #     print("---- current_test_row_num ---- ", current_test_row_num)
    #     sets = self.get_data_sets_count(test_name)
    #     print("---- total data sets ---- ", sets)
    #     if current_test_row_num != -1 and sets != 0:
    #         first_data_set_row_num = current_test_row_num + 2
    #         for row in range(sets):
    #             if self.sheet.cell_value(first_data_set_row_num, 0) == 'Y':
    #                 for cell in self.sheet.row(first_data_set_row_num):
    #                     val = cell.value
    #                     print(val)
    #     else:
    #         print("No such test exist in the test data sheet")


obj = ExcelDataReader(file_path="D:\\qababu\\github\\pycharm\\SeleniumWithPython\\resources\\TestData.xlsx",
                      sheet_name="MockData")
obj.get_data_sets_count("TestCase_004")
