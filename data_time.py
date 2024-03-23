import datetime


def date_time():
    # Get the current date and time
    current_datetime = datetime.datetime.now()

    # Polish translations for "Month" and "Year"
    month_translation = {
        "January": "styczeń",
        "February": "luty",
        "March": "marzec",
        "April": "kwiecień",
        "May": "maj",
        "June": "czerwiec",
        "July": "lipiec",
        "August": "sierpień",
        "September": "wrzesień",
        "October": "październik",
        "November": "listopad",
        "December": "grudzień",
    }

    # Extract the current hour
    current_hour = current_datetime.hour

    # Format the current date with month and year
    date_time_pc = current_datetime.strftime("%d %B %Y")

    # Changing english into polish words
    for english_month, polish_month in month_translation.items():
        date_time_pc = date_time_pc.replace(english_month, polish_month)
    month_and_time = date_time_pc.lower(), current_hour

    # Splitting string into single words
    day_win, month_win, year_win = date_time_pc.split()

    return day_win, month_win, year_win, current_hour
