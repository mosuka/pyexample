import datetime
import logging
import os
from typing import Any, Dict, List

from pythonjsonlogger import jsonlogger
from pytz import timezone

# Get log level from environment variable
log_level_str = os.getenv("LOG_LEVEL", "DEBUG").upper()
log_level = getattr(logging, log_level_str, logging.DEBUG)


class JsonFormatter(jsonlogger.JsonFormatter):
    """
    Custom JSON formatter for logging.
    This formatter adds custom fields to the log record.
    """

    def parse(self) -> List[str]:
        """ "
        Parse the log record and add custom fields."
        """
        return [
            "process",
            "timestamp",
            "level",
            "name",
            "message",
            "stack_info",
        ]

    def add_fields(
        self,
        log_record: Dict[str, Any],
        record: logging.LogRecord,
        message_dict: Dict[str, Any],
    ) -> None:
        """
        Add custom fields to the log record.

        Args:
            log_record (Dict[str, Any]): The dictionary representing the log record.
            record (logging.LogRecord): The original log record.
            message_dict (Dict[str, Any]): Additional message fields.
        """

        super().add_fields(log_record, record, message_dict)

        # Set timestamp to UTC
        if log_record.get("timestamp"):
            log_record["timestamp"] = (
                datetime.datetime.strptime(log_record["timestamp"], "%Y-%m-%dT%H:%M:%S%z")
                .astimezone(timezone("UTC"))
                .strftime("%Y-%m-%dT%H:%M:%S%z")
            )
        else:
            log_record["timestamp"] = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S%z")

        if log_record.get("level"):
            log_record["level"] = log_record["level"].upper()
        else:
            log_record["level"] = record.levelname


def getLogger(module_name: str) -> logging.Logger:
    """
    Get a logger instance with a custom JSON formatter.

    Args:
        module_name (str): Name of the module.

    Returns:
        logging.Logger: Logger instance.
    """
    logger = logging.getLogger(module_name)
    handler = logging.StreamHandler()

    handler.setLevel(log_level)
    handler.setFormatter(JsonFormatter())
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    logger.propagate = False

    return logger
