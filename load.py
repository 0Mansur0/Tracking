from enum import Enum
import os
import sys
import sqlite3
import time
from typing import Callable


class InvalidAnswer(ValueError):
    def __init__(self, message):
        self.message = message


class ExitCodes(Enum):
    INVALID_USAGE = 1
    SQLITE3_ERROR = 2
    KEYBOARD_INTERRUPT = 130


def main() -> int:
    db_settings = {}

    db_settings["typing"] = {
        "db_path": "typing/typing.db",
        "table": "tests",
        "layout": "Holemak"
    }

    # NOT READY FOR PRODUCTION
    db_settings["control"] = {
        "db_path": "control/control.db",
        "table": "activities"
    }
    
    date = time.strftime("%Y-%m-%d")

    try:
        commit_tests_sqlite(**db_settings["typing"], date=date)
    except InvalidAnswer as e:
        print(e)
        return ExitCodes.INVALID_USAGE.value
    except sqlite3.Error as e:
        print(f"Database error occured while writing: {e}")
        return ExitCodes.SQLITE3_ERROR.value

    return 0


def commit_tests_sqlite(db_path: str, table: str, date: str, layout: str) -> None:
    """Prompt user for speed and accuracy and ensure the results
    were submitted intentionally. Then try to write into provided
    location with the parameters"""

    speed = get_float("Speed: ", lambda value: (0 < value < 10000))
    accuracy = get_float("Accuracy: ", lambda value: (80 < value < 100))


    # Try to connect to sqlite3 database at provided path and exit
    # in case of error
    con = sqlite3.connect(db_path)

    cur = con.cursor()
    cur.execute(f"""
        INSERT INTO {table}(
            date,
            speed,
            accuracy,
            layout_id
        )
        VALUES (
            ?, ?, ?, (
                SELECT id
                FROM layouts
                WHERE name = ?
            )
        )""",
        (date, speed, accuracy, layout))
    
    con.commit()
    con.close()
    print("Successfully written results!")


def confirm(prompt: str | None) -> bool:
    """Prompt user for answer with the provided prompt
    concatenated with "Are sure? [n / y] " with leading space if prompt is non-empty.
    If user does not agree or disagree, InvalidAnswer exception raised"""


    agreed = ["yes", "y"]
    disagreed = ["no", "n"]

    question = (f'{prompt} ' if prompt else '') + f"Are sure? [n / y] "    
    answer = input(question)
        
    if answer.lower() in agreed:
        return True
    elif answer.lower() in disagreed:
        return False
    else:
        raise InvalidAnswer(f"Answer better be one of {agreed!r} or {disagreed!r}")


def get_float(prompt: str, condition: Callable[[float], bool]) -> float:
    """Use the provided prompt and get float which
    can be validated with a function."""
    while True:
        try:
            result: float = float(input(prompt))
            if not condition(result):
                continue
            return result
        except ValueError:
            continue    


if __name__ == "__main__":
    try:
        sys.exit(main())    
    except KeyboardInterrupt:
        print('\nInterrupted')
        try:
            sys.exit(ExitCodes.KEYBOARD_INTERRUPT.value)
        except SystemExit:
            os._exit(ExitCodes.KEYBOARD_INTERRUPT.value)