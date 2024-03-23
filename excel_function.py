import pandas as pd
from data_time import date_time

df = pd.read_excel("smieci.xlsx")


def main():
    day_win, month_win, year_win, hour_win = (
        date_time()
    )  # Day, Month, Year, Hour, acquired from windows system
    month_year = (
        month_win + " " + year_win
    )  # Joined Month and Year (database has exact same type of written values)

    i = 0  # added i variable to get index of a month in excel table

    for (
        column,
        items,
    ) in df.items():  # Iteration through values to find column "MIESIĄC"
        if column == "MIESIĄC":
            for (
                month
            ) in (
                items.str.lower()
            ):  # Iteration through values in "MIESIĄC to find value of the month (January, February and etc.)"
                i = i + 1
                if month == month_year:  # Finding current month
                    present_month = month
                    value = df.loc[[i - 1]]
                    print(value)

                    # DZIEN MIESIAC ROK - TYP CZYLI NP ZMIESZANE
                    # POTNIJ TO TAK
        # else:
        #     if column == present_month:
        #         for schedule_date in df.iloc[:, 1:]:
        #             print(schedule_date)


if __name__ == "__main__":
    main()
