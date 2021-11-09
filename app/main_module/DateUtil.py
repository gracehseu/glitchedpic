from datetime import date


def getTodaysDateAsString():
    today = date.today()

    # dd_mm_YYYY
    return today.strftime("%d_%m_%Y")