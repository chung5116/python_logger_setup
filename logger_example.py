from logger import create_logger





def main():
    logger_test.debug("runtime error")
    logger_test.info("EXPORT DONE!")

if __name__ == '__main__':
    logger_test = create_logger('obc')
    logger_test.debug('this is dubug')
    logger_test.info('Start')
    main()

