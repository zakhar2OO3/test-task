import matplotlib.pyplot as plt
import pandas as pd

zakhar_table = pd.read_csv('data.csv')

zakhar_table["event_date"] = pd.to_datetime(zakhar_table["event_date"])

attendance_by_date = zakhar_table.groupby("event_date")["is_attend"].sum()

plt.figure(figsize=(10, 5))
plt.plot(attendance_by_date.index, attendance_by_date.values, marker='o', linestyle='-', color='b')
plt.xlabel("Дата посещений")
plt.ylabel("Посещения")
plt.title("Дата")
plt.grid()

plt.show()