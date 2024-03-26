import pandas as pd
from data_time import date_time

df = pd.read_excel("smieci.xlsx")


def main():
    # Day, Month, Year, Hour, acquired from windows system
    day_win, month_win, year_win, hour_win = date_time()

    # Joined Month and Year (database has exact same type of written values)
    month_year = month_win + " " + year_win

    message = "\n"

    # Iterate over each row in the DataFrame
    for index, row in df.iterrows():

        # Checked if the month matches the current month
        if row["MIESIĄC"].lower() == month_year.lower():

            # Iterate over each column in the row
            for column in df.columns[1:]:  # Skip the first column which is 'MIESIĄC'
                if "," in str(row[column]):
                    multiple_data = row[column].split(",")
                    for single_data in multiple_data:
                        message = str(single_data) + " " + month_year + " " + column
                        print(message)
                else:
                    message = str(row[column]) + " " + month_year + " " + column
                    print(message)


if __name__ == "__main__":
    main()
