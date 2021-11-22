from datetime import date


def getTodaysDateAsString():
    today = date.today()

    # dd_mm_YYYY
    return today.strftime("%m_%d_%Y")