from datetime import datetime


# TODO Write unit test
# TODO Figure out how to reproduce the date format that is in the data files
# in a clean way
def datetime_to_str(datetime_: datetime) -> str:
    return datetime_.isoformat(timespec="microseconds")
