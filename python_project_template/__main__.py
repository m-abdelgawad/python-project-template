import os
import yaml
from packages.project import project
from packages.logger import logger
from packages.timestamp import timestamp


# Initiate logger
log = logger.get(app_name='log')


def main():

    log.info('Start program execution')

    # Import configurations
    config_path = os.path.join(project.get_absolute_path(), 'config.yaml')
    with open(config_path) as config_file:
        config = yaml.safe_load(config_file)

    # Start testing logger
    log.info('Configuration Username: ' + config['account']['username'])
    log.info('Configuration Password: ' + config['account']['password'])
    current_timestamp = timestamp.get_current()
    log.info('Current Timestamp: ' + current_timestamp)
    # Finished testing logger

    # raise Exception("Test exception to test the error logging")

    log.info('Finished program execution')


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        log.error(e)
