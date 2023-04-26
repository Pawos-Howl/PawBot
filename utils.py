import time
import logging
from datetime import datetime
from pytz import timezone

def toDateTime(str_time):
    str_time = str_time.replace("T", "-").replace("Z", "").split(".")[0]
    date = datetime.strptime(str_time, "%Y-%m-%d-%H:%M:%S")
    date = date.astimezone(timezone('US/Pacific'))
    return date


def timeConvert(now):
    miliTime = now.strftime("%H:%M:%S")
    hours, minutes, seconds = miliTime.split(":")
    hours, minutes = int(hours), int(minutes)
    hours -= 7
    setting = "AM"
    if hours > 12:
        setting = "PM"
        hours -= 12
    return ("%02d:%02d" + setting) % (hours, minutes)

def checktime(t):
    print(f"time passed to checktime: {t}")
    r = time.time()
    if r - t < 60: return "Less than a minute"
    elif r - t > 60: return f"for {int((r - t) / 60)} minutes" if int((r - t) / 60) > 1 else "for a minute"
    elif r - t > 60 and r - t > 3600: return f"for {int((r - t) / 3600)} hours"
    elif r - t > 3600 and r - t > 86400: return f"for {int((r - t) / 86400)} days"

def nowstr():
    now = datetime.now()
    return now.strftime("%m/%d/%Y") + " at " + timeConvert(now)

class CustomFormatter(logging.Formatter):
    """Logging Formatter to add colors"""

    LEVEL_COLOURS = [
        # (logging.DEBUG, '\x1b[35;1m'),
        # (logging.INFO, '\x1b[36;1m'),
        # (logging.WARNING, '\x1b[33;1m'),
        # (logging.ERROR, '\x1b[31m'),
        # (logging.CRITICAL, '\x1b[41m')
        (logging.DEBUG, '\x1b[38;5;34;1m'),# \u001b[38;5;34;1m
        (logging.INFO, '\x1b[38;5;129;1m'),
        (logging.WARNING, '\x1b[38;5;220;1m'),
        (logging.ERROR, '\x1b[31m'),
        (logging.CRITICAL, '\x1b[41m'),
    ]

    format = "%(levelname)s - %(message)s"

    FORMATS = {
        level: logging.Formatter(
            f'\x1b[30;1m%(asctime)s\x1b[0m {colour}%(levelname)-8s\x1b[0m \u001b[38;5;33;1m%(name)s\u001b[0m %(message)s',
            '%Y-%m-%d %H:%M:%S',
        )
        for level, colour in LEVEL_COLOURS
    }

    def format(self, record):
        formatter = self.FORMATS.get(record.levelno)
        if formatter is None:
            formatter = self.FORMATS[logging.INFO]

        # Override the traceback to always print in red
        if record.exc_info:
            text = formatter.formatException(record.exc_info)
            record.exc_text = f'\x1b[31m{text}\x1b[0m'

        output = formatter.format(record)

        # Remove the cache layer
        record.exc_text = None
        return output

def setupLogger():
    logging.root.setLevel(logging.NOTSET)
    handler = logging.StreamHandler()
    dt_fmt = '%Y-%m-%d %H:%M:%S'
    formatter = CustomFormatter()
    logger = logging.getLogger("PawBotAlerts")
    handler.setFormatter(formatter)
    logger.setLevel(logging.NOTSET)
    logger.addHandler(handler)
    
    return logger