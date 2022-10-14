#!/usr/bin/env python3
# coding=utf-8

import sys
from random import randint

from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi



class Main(QDialog):
    def __init__(self):
        super(Main, self).__init__()
        loadUi('uis/main.ui', self)  # загрузка формы в py-скрипт

        self.setWindowTitle('Работа с визуальными табличными данными в Python')
        self.setWindowIcon(QtGui.QIcon('images/logo.png'))

        self.btn_random_number.clicked.connect(self.fill_random_numbers)
        self.btn_solve.clicked.connect(self.solve)

    def fill_random_numbers(self):
        """
        заполняем таблицу случайными числами
        :return:
        """
        row = 0
        col = 0

        # заполняем таблицу случайными числами
        while row < self.tableWidget.rowCount():
            while col < self.tableWidget.columnCount():
                random_num = randint(-10, 10)
                self.tableWidget.setItem(row, col, QTableWidgetItem(str(random_num)))
                col += 1
            row += 1
            col = 0
        self.label_error.setText('')
        self.label_max_el.setText('Максимальный и минимальный элементы: ')

    def solve(self):
        list_information_max_num = find_max_and_min(self.tableWidget)
        if not list_information_max_num:
            self.label_error.setText('Введены некорректные данные!')
        else:
            self.label_max_el.setText(
                'Максимальный элемент: ' + str(list_information_max_num[0]) + ' [' +
                str(list_information_max_num[1]) + ';' + str(list_information_max_num[2]) + ']' + '. ' + 'Минимальный элемент: ' + str(list_information_max_num[3]) + ' [' +
                str(list_information_max_num[4]) + ';' + str(list_information_max_num[5]) + ']')
            self.label_error.setText('')
            # -*- решение задания -*-

            s = 0
            for i in range(self.tableWidget.rowCount()):
                for j in range(self.tableWidget.columnCount()):
                    s += int(self.tableWidget.item(i, j).text())

            self.label_sum.setText('Сумма всех элементов: ' + str(s))


            if (s) > 100:
                self.label_error.setText('Сумма элементов таблицы больше ста!')
            else:
                max = list_information_max_num[0]
                min = list_information_max_num[3]
                self.label_sum.setText('Минимум и максимум поменялись местами.')
                self.tableWidget.setItem(list_information_max_num[1], list_information_max_num[2],
                                         QTableWidgetItem(str(min)))
                self.tableWidget.setItem(list_information_max_num[4], list_information_max_num[5],
                                         QTableWidgetItem(str(max)))


                self.mod_col3()

    def mod_col3(self):
        """
        Увеличение чисел второго столбца на два
        """
        row = 1
        col = 0
        while col < self.tableWidget.columnCount():
            self.tableWidget.setItem(row, col, QTableWidgetItem(str(0)))
            col += 1



def find_max_and_min(table_widget):
    """
    находим максимальное число из таблицы и его координаты
    :param table_widget: таблица
    :return: [max_num, row_max_number, col_max_number], если выкинуто исключение,
            то None
    """

    row_max_number = 0  # номер строки, в котором находится максимальне число
    col_max_number = 0  # номер столбца, в котором находится максимальне число
    row_min_number = 0
    col_min_number = 0

    try:
        max_num = int(table_widget.item(row_max_number, col_max_number).text())
        min_num = int(table_widget.item(row_min_number, col_min_number).text())
        row = 0
        col = 0
        while row < table_widget.rowCount():
            while col < table_widget.columnCount():
                number = int(table_widget.item(row, col).text())
                if number >= max_num:
                    max_num = number
                    row_max_number = row
                    col_max_number = col
                if number <= min_num:
                    min_num = number
                    row_min_number = row
                    col_min_number = col
                col += 1
            row += 1
            col = 0
        return [max_num, row_max_number, col_max_number, min_num, row_min_number, col_min_number]
    except Exception:
            return None

def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
