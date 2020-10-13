def decorator(log_fn, fn_version):
    import time
    def inner(func):
        def wapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            stop_time = time.time()
            print("time:{},login_fn:{},fn_version:{}".format(round(stop_time-start_time, 4), log_fn, fn_version))
            return result
        return wapper
    return inner

@decorator('log','1,4')
def funcs():
    print("yes")