import logging
import google.cloud.logging


def _install_gcloud_logging_handler(logger: logging.Logger, level: int) -> None:
    """
    Installs a logging handler which will record messages to Google Cloud Logging, if they are at least the given level.
    """

    handler = google.cloud.logging.handlers.CloudLoggingHandler(
        google.cloud.logging.Client()
    )

    handler.setLevel(level)
    logger.addHandler(handler)


def _install_console_logging_handler(logger: logging.Logger) -> None:
    """
    Installs a logging handler which will print all messages to the console (command line/tty).
    
    Log levels are assumed to be controlled at the logger level, rather than the handler.
    """

    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter("%(asctime)s [%(name)s][%(levelname)s] %(message)s")
    handler.setFormatter(formatter)

    logger.addHandler(handler)


def configure_root_logger(verbosity: int) -> None:
    """
    Configures the root (global) logger according to the arbitrary level of verbosity desired by the user (e.g., in number of `-v` flags).
    """

    logger = logging.getLogger()

    if verbosity >= 3:
        logger.setLevel(logging.DEBUG)
    elif verbosity >= 2:
        logger.setLevel(logging.INFO)
    else:
        logger.setLevel(logging.WARN)

    _install_console_logging_handler(logger)
    _install_gcloud_logging_handler(logger, logging.WARN)


def configure_package_logger(logger: logging.Logger, verbosity: int) -> None:
    """
    Configures a package-level logger according to the arbitrary level of verbosity desired by the user (e.g., in number of `-v` flags).

    This is meant for use with the _primary_ package being invoked, not all packages (which can instead roll up to the root logger, configured differently).
    """

    if verbosity >= 2:
        logger.setLevel(logging.DEBUG)
    elif verbosity >= 1:
        logger.setLevel(logging.INFO)
    else:
        logger.setLevel(logging.WARN)

    _install_console_logging_handler(logger)
    _install_gcloud_logging_handler(logger, logging.INFO)
    logger.propagate = False
