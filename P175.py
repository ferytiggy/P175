# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 13:59:01 2024

@author: Aidan
"""

import matplotlib .pyplot as plt
import psutil as p

app_name_dict = []
count = 0
for process in p.process_iter():
    count = count + 1
    if count <=6:
        name = process.name()
        cpu_usage = p.cpu_percent()
        print(name, cpu_usage)
        app_name_dict.update({name:cpu_usage})

keymax = max(app_name_dict, key=app_name_dict.get)
print(keymax)

keymin = min(app_name_dict, key=app_name_dict.get)
print(keymin)

name_list = [keymax, keymin]
print(name_list)

app = app_name_dict.values()

max_app = max(app)
print(max_app)

min_app = min(app)
print(min_app)

max_min_list = [max_app, min_app]
print(max_min_list)

plt.figure(figsize=(15,7))
plt.xlabel("Apps")
plt.ylabel("Uso")
plt.bar(app_name_dict, app, width=0.6, color=("lime" ,"cyan"))
plt.show()
        