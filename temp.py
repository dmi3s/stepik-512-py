from datetime import datetime as dt
now = dt.now()
print(f"Текущее время {now:%d.%m.%Y %H:%M}")
