from datetime import datetime


# TODO Write unit tests
def datetime_to_str(datetime_: datetime) -> str:
    return datetime_.isoformat(timespec="milliseconds").replace(
        "+00:00", "Z"
    )  # TODO Find how to have "Z" in a way other than string replacement
