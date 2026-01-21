import csv
import random
import requests
from io import StringIO
from escpos.printer import Usb

CSV_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQwDUvoYUHL83wZBhQeT7CJJnJnm1Pqkmicgs6UtAnuo3D4uv-TmXSrA1CKnRWt9YqycouftvAGiEqm/pub?output=csv"

response = requests.get(CSV_URL)
response.raise_for_status()

csv_data = StringIO(response.text)
reader = csv.reader(csv_data)

rows = list(reader)

# Remove header row if present
rows = rows[1:]

if not rows:
    exit()

word, translation = random.choice(rows)

printer = Usb(0x04b8, 0x0e15)

printer.set(align="center", bold=True, width=2, height=2)
printer.text("VOCABULARY OF THE DAY\n\n")

printer.set(bold=True, width=2, height=2)
printer.text(word + "\n\n")

printer.set(bold=False, width=1, height=1)
printer.text(translation + "\n\n")

printer.text("----------------------\n")
printer.cut()
