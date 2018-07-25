#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""little pogram taking the last website opened in firefox and opening it"""

import sqlite3
import webbrowser
import time

db_file_location = r'C:\Users\pierr\AppData\Roaming\Mozilla\Firefox\Profiles\o4eve06y.default\places.sqlite'
conn = sqlite3.connect(db_file_location)
cursor = conn.cursor()
cursor.execute("""SELECT url, last_visit_date FROM moz_places""")
history = cursor.fetchall()
conn.close()

history_sorted_by_last_visit_date = sorted(history, key = lambda tup: 0 if tup[1] is None else tup[1])
history_sorted_by_last_visit_date.reverse()

url_list = []
i=0
while i <5:
    url_list.append(history_sorted_by_last_visit_date[i][0])
    i += 1

# open defaut browser with a list of url 
for url in url_list:
    webbrowser.open_new_tab(url)
    time.sleep(1)