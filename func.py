import time


def compare_time(l_time):
    start_t = '20160101'
    end_t = '20161011'
    s_time = time.mktime(time.strptime(start_t, '%Y%m%d'))  # get the seconds for specify date

    e_time = time.mktime(time.strptime(end_t, '%Y%m%d'))
    try:
        log_time = time.mktime(time.strptime(l_time, '%Y-%m-%d'))
    except:
        return False
    if (float(log_time) >= float(s_time)) and (float(log_time) <= float(e_time)):
        return True

    return False

