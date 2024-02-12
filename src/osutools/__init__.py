import logging

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)

log_handler = logging.StreamHandler()
log.addHandler(log_handler)
