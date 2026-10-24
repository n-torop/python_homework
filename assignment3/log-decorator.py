

import logging

logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log","a"))
# @logger_decorator
def logger_decorator (func):
    def wrapper(*args, **kwargs):
        
        logger.info(f"function:{func.__name__}")
        logger.info(f"positional parameters: {args if args else "none"}")

        result=func(*args, **kwargs)
        logger.info(f"keyword parameters: {kwargs if kwargs else "none"}")
        # logger.log(logging.INFO, "this string would be logged")
        logger.info(f"return: {result} ")
            # return result


    return wrapper

@logger_decorator
def simple_function():
    print ("Hello, World!")



@logger_decorator
def bool_func(*args):
    return True


@logger_decorator
def func_no_arg(**kwargs):
    return logger_decorator


simple_function()
bool_func(5, 10, "str")
func_no_arg(name="Natasha")