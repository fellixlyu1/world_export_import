import sqlite3
import sys

from PyQt5.QtGui import QImage, QTextCursor
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QGroupBox, QFormLayout, QComboBox, QLabel, QScrollArea, QVBoxLayout, QPushButton, QTextEdit
)

import visualizations

# Connect to the database
connection = sqlite3.connect("global_imp_exp.db")
cursor = connection.cursor()

# Data options and SQL statements mapping
data_options = ["Export", "Import", "Export Product Share", "Import Product Share",
                "Revealed Comparative Advantage", "World Growth", "Country Growth", "AHS Simple Average",
                "AHS Weighted Average", "AHS Total Tariff Lines", "AHS Dutiable Tariff Lines Share",
                "AHS Duty Free Tariff Lines Share", "AHS Specific Tariff Lines Share",
                "AHS AVE Tariff Lines Share", "AHS Max Rate", "AHS Min Rate", "AHS Specific Duty Imports",
                "AHS Dutiable Imports", "AHS Duty Free Imports", "MFN Simple Average", "MFN Weighted Average",
                "MFN Total Tariff Lines", "MFN Dutiable Tariff Lines Share", "MFN Duty Free Tariff Lines Share",
                "MFN Specific Tariff Lines Share", "MFN AVE Tariff Lines Share", "MFN Max Rate", "MFN Min Rate",
                "MFN Specific Duty Imports", "MFN Dutiable Imports", "MFN Duty Free Imports"]

sql_statement = ["Export", "Import", "ExportProductShare", "ImportProductShare",
                 "RevealedComparativeAdvantage", "WorldGrowth", "CountryGrowth", "AHSSimpleAverage",
                 "AHSWeightedAverage", "AHSTotalTariffLines", "AHSDutiableTariffLinesShare",
                 "AHSDutyFreeTariffLinesShare", "AHSSpecificTariffLinesShare",
                 "AHSAVETariffLinesShare", "AHSMaxRate", "AHSMinRate", "AHSSpecificDutyImports",
                 "AHSDutiableImports", "AHSDutyFreeImports", "MFNSimpleAverage", "MFNWeightedAverage",
                 "MFNTotalTariffLines", "MFNDutiableTariffLinesShare", "MFNDutyFreeTariffLinesShare",
                 "MFNSpecificTariffLinesShare", "MFNAVETariffLinesShare", "MFNMaxRate", "MFNMinRate",
                 "MFNSpecificDutyImports", "MFNDutiableImports", "MFNDutyFreeImports"]


def list_of_countries():
    country_list = []
    countries = cursor.execute("SELECT DISTINCT PartnerName FROM global_business_data").fetchall()
    country_list = [tup[0] for tup in countries]
    return country_list


def list_of_years():
    return [str(year) for year in range(1988, 2022)]


class PieWindow(QWidget):
    def __init__(self, cursor):
        super().__init__()
        self.cursor = cursor

        pie_group_box = QGroupBox('Pie Tool')
        pie_form = QFormLayout()

        self.year_list = list_of_years()

        self.year_combo = QComboBox()
        self.year_combo.addItems(self.year_list)

        self.column_combo = QComboBox()
        self.column_combo.addItems(data_options)

        pie_form.addRow(QLabel('Years: '), self.year_combo)
        pie_form.addRow(QLabel('Data: '), self.column_combo)

        fetch_pie_button = QPushButton('Pie Chart')
        fetch_pie_button.clicked.connect(self.fetch_pie_data)
        pie_form.addRow(fetch_pie_button)

        self.results_display = QTextEdit()
        self.results_display.setReadOnly(True)
        pie_form.addRow(self.results_display)

        pie_group_box.setLayout(pie_form)

        scroll = QScrollArea()
        scroll.setWidget(pie_group_box)
        scroll.setWidgetResizable(True)
        scroll.setFixedHeight(400)

        layout = QVBoxLayout(self)
        layout.addWidget(scroll)

    def fetch_pie_data(self):
        year = self.year_combo.currentText()
        column = self.column_combo.currentText()

        column_index = data_options.index(column)
        sql_column = sql_statement[column_index]

        query = f"SELECT {sql_column}, PartnerName FROM global_business_data WHERE Year = ?"
        self.cursor.execute(query, (year,))
        results = self.cursor.fetchall()

        data_values = [result[0] for result in results]
        countries = [result[1] for result in results]

        image_path = visualizations.get_pie_chart(countries, year, data_values, column)

        display_text = f"Results for {year}:\n\n"

        self.results_display.setPlainText(display_text)

        image = QImage(image_path)
        if image.isNull():
            self.results_display.append('Failed to load image.')
            return

        cursor = self.results_display.textCursor()
        cursor.movePosition(QTextCursor.End)
        cursor.insertImage(image)

        self.results_display.append(f"See the pie chart below:\n{image_path}")


class ScatterWindow(QWidget):
    def __init__(self, cursor):
        super().__init__()
        self.cursor = cursor

        scatter_group_box = QGroupBox('Scatter Plot Tool')
        scatter_form = QFormLayout()

        self.country_list = list_of_countries()

        self.country_combo = QComboBox()
        self.country_combo.addItems(self.country_list)

        self.column_combo = QComboBox()
        self.column_combo.addItems(data_options)

        scatter_form.addRow(QLabel('Countries: '), self.country_combo)
        scatter_form.addRow(QLabel('Data: '), self.column_combo)

        fetch_scatter_button = QPushButton('Scatter Plot')
        fetch_scatter_button.clicked.connect(self.fetch_scatter_data)
        scatter_form.addRow(fetch_scatter_button)

        self.results_display = QTextEdit()
        self.results_display.setReadOnly(True)
        scatter_form.addRow(self.results_display)

        scatter_group_box.setLayout(scatter_form)

        scroll = QScrollArea()
        scroll.setWidget(scatter_group_box)
        scroll.setWidgetResizable(True)
        scroll.setFixedHeight(400)

        layout = QVBoxLayout(self)
        layout.addWidget(scroll)

    def fetch_scatter_data(self):
        country = self.country_combo.currentText()
        column = self.column_combo.currentText()

        column_index = data_options.index(column)
        sql_column = sql_statement[column_index]

        query = f"SELECT {sql_column} FROM global_business_data WHERE PartnerName = ?"
        self.cursor.execute(query, (country,))
        results = self.cursor.fetchall()

        data_values = [result[0] for result in results]

        available_years = list_of_years()[:len(data_values)]

        image_path = visualizations.get_scatter_plot(data_values, available_years, column, country)

        display_text = f"Results for {country}:\n\n"
        self.results_display.setPlainText(display_text)

        image = QImage(image_path)
        if image.isNull():
            self.results_display.append('Failed to load image.')
            return

        cursor = self.results_display.textCursor()
        cursor.movePosition(QTextCursor.End)
        cursor.insertImage(image)

        self.results_display.append(f"See the scatter plot below:\n{image_path}")


class MainWindow(QWidget):
    def __init__(self, cursor):
        super().__init__()
        self.scatter_window = ScatterWindow(cursor)
        self.scatter_window.setGeometry(1000, 600, 600, 400)
        self.pie_window = PieWindow(cursor)
        self.pie_window.setGeometry(1000, 600, 600, 400)
        main_group_box = QGroupBox('Global Commerce Analysis')
        main_form = QFormLayout()

        scatter_button = QPushButton('Scatter Plot')
        scatter_button.clicked.connect(self.scatter_window.show)
        main_form.addRow(scatter_button)

        pie_button = QPushButton('Pie Chart')
        pie_button.clicked.connect(self.pie_window.show)
        main_form.addRow(pie_button)

        self.results_display = QTextEdit()
        self.results_display.setReadOnly(True)
        main_form.addRow(self.results_display)

        main_group_box.setLayout(main_form)

        scroll = QScrollArea()
        scroll.setWidget(main_group_box)
        scroll.setWidgetResizable(True)
        scroll.setFixedHeight(400)

        layout = QVBoxLayout(self)
        layout.addWidget(scroll)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow(cursor)
    main_window.setGeometry(1000, 600, 600, 400)
    main_window.show()
    sys.exit(app.exec_())
