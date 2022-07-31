from datetime import datetime
from functools import wraps


def log_func(log_path=None):
    
    def log_func_decorator(dec_function):
    
        @wraps(dec_function)
        def inner_function(*args, **kwargs):
            func_name = dec_function.__name__
            log_args = args
            log_kwargs = kwargs
            call_time = datetime.now()
            result = dec_function(*args, **kwargs)
            if log_path:
                logfile_path = f'{log_path}\\{func_name}.log'
            else:
                logfile_path = f'{func_name}.log'
            with open(logfile_path, 'w', encoding='utf-8') as logfile:
                logfile.write(f'Function name: {func_name}\n')
                logfile.write(f'Function was called: {call_time}\n')
                if log_args:
                    logfile.write(f'Function args: {log_args}\n')
                else:
                    logfile.write('No args\n')
                if log_kwargs:
                    logfile.write(f'Function kwargs: {log_kwargs}\n')
                else:
                    logfile.write('No kwargs\n')
                logfile.write(f'Function return: {result}\n')
            return result
        
        return inner_function
    
    return log_func_decorator
