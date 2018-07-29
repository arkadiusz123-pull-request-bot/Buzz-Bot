from save import *
import config

def error_fatal(reason, logged_reason):
    # log before reporting error, cause that just seems like the right way to do it
    logged_error = "[FATAL]: " + str(logged_reason)  # "FATAL" is capped to be easier to see
    error_save(logged_error)
    print("-------------Fatal Error-------------")
    print("Reason: " + str(reason))
    print("Check saves/errors.log for more information.")
    print("-------------------------------------")
    input()
    exit()


def error_normal(reason, logged_reason):
    # log before reporting error, cause that just seems like the right way to do it
    logged_error = "[Error]:  " + str(logged_reason)
    error_save(logged_error)
    print("[Error]: "+str(reason))


def error_warning(reason, logged_reason):
    # log before reporting error, cause that just seems like the right way to do it
    logged_error = "[Warning]: " + str(logged_reason)
    error_save(logged_error)
    print("[Warning]: "+str(reason))

def dprint(content):
    if config.debug_mode == True:
        x = "[Debug Log]: " + str(content).lower()
        file_append('saves/main.log', x)