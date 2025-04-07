# from dotenv import load_dotenv
# import os

# load_dotenv(dotenv_path="custom.env")

# load_dotenv()

# LOG_LEVEL=os.getenv('LOG_LEVEL','INFO').upper()
# print("LOG_LEVEL from .env:", LOG_LEVEL)

# def log(message,level):
#     levels=['DEBUG','INFO','WARNING','ERROR','CRITICAL']
#     if levels.index(level)>=levels.index(LOG_LEVEL):
#         print(f"[{level}] {message}")

# log("this is DEBUG message","DEBUG")
# log("this is INFO message","INFO")
# log("this is WARNING message","WARNING")
# log("this is ERROR message","ERROR")
# log("this is CRITICAL message","CRITICAL")
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="custom.env", override=True)  # 👈 explicitly load custom.env

LOG_LEVEL = os.getenv('log_level', 'INFO').upper()
print("LOG_LEVEL from .env:", LOG_LEVEL)

def log(message, level):
    levels = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']
    if levels.index(level) >= levels.index(LOG_LEVEL):
        print(f"[{level}] {message}")

log("this is DEBUG message", "DEBUG")
log("this is INFO message", "INFO")
log("this is WARNING message", "WARNING")
log("this is ERROR message", "ERROR")
log("this is CRITICAL message", "CRITICAL")
