from dotenv import load_dotenv
import os
import pyodbc

load_dotenv()

class DB:
    def __init__(self) -> None:
        cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                            "Server=DESKTOP-RBDGU2B\SQLEXPRESS;"
                            "Database=Final_Project;"
                            "Trusted_Connection=yes;")

        self.cursor = cnxn.cursor()


    def execute(self, query):
        self.cursor.execute(query)
        