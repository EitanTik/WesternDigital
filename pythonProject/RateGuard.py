from datetime import datetime
from datetime import timedelta

dictionary = {}
class RateGuard(object):
    def __init__(self, rate_number, rate_time_threshold, indexing_limit_handler):
        """
        :param rate_number - number of times a function is allowed to run:
        :param rate_time_threshold - the time period the rate is restricted to (e.g 30 times in 60 seconds)
        :param indexing_limit_handler - will handle the indexing of the function arguments
        """
        # run over the existing params
        if indexing_limit_handler in dictionary.keys():
            if len(dictionary[indexing_limit_handler]) < rate_number:
                dictionary[indexing_limit_handler].append(datetime.now())
                # get rid of the first argument when reaching the rate limit
                if len(dictionary[indexing_limit_handler]) > rate_number:
                    dictionary[indexing_limit_handler].pop(0)
            elif len(dictionary[indexing_limit_handler]) == rate_number and len(dictionary[indexing_limit_handler]) > 1 and\
                    dictionary[indexing_limit_handler][-1]-dictionary[indexing_limit_handler][0]<timedelta(seconds=rate_time_threshold):
                raise Exception(indexing_limit_handler + " reached the allowed limit")
            else:
                dictionary[indexing_limit_handler].pop(0)
        # for the first element
        else:
            dictionary[indexing_limit_handler] = [datetime.now()]


