import logging
import datetime
import os

# DEBUG 等級，即時看
# INFO 等級，事後看

log_dir_path = 'Logger/'
log_filename = datetime.datetime.now().strftime("%Y-%m-%d_%H_%M_%S.log")

def create_logger(log_folder):
    # config
    logging.captureWarnings(True)
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    my_logger = logging.getLogger('py.warnings')
    my_logger.setLevel(logging.INFO)

    # 若不存在目錄則新建
    if not os.path.exists(log_dir_path + log_folder):
        os.makedirs(log_dir_path + log_folder)

    # file handler
    fileHandler = logging.FileHandler(log_dir_path + log_folder + '/' + log_filename,'w','utf-8')
    fileHandler.setFormatter(formatter)
    my_logger.addHandler(fileHandler)

    # console handler
    consoleHandler = logging.StreamHandler()
    consoleHandler.setLevel(logging.DEBUG)
    consoleHandler.setFormatter(formatter)
    my_logger.addHandler(consoleHandler)

    return my_logger
