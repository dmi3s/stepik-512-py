import datetime as dt


def main():
    date = dt.datetime.strptime(input(), "%Y %m %d")
    n_days = int(input())
    new_date = date + dt.timedelta(days=n_days)
    print("{d.year} {d.month} {d.day}".format(d=new_date))


main()
