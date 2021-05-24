import RateGuard
import time


def a_decorator_passing_arbitrary_arguments(function_to_decorate):
    def a_wrapper_accepting_arbitrary_arguments(*args):
        RateGuard.RateGuard(3,5,str(args))
        function_to_decorate(*args)

    return a_wrapper_accepting_arbitrary_arguments


@a_decorator_passing_arbitrary_arguments
def get_users(account_id: str, service_name: str) -> list[dict]:
    print(account_id)
    print(service_name)

@a_decorator_passing_arbitrary_arguments
def set_it_up() -> list[dict]:
    print(4)
    print("LA")

@a_decorator_passing_arbitrary_arguments
def get_stuff(account_id: str, service_name: str, page_size: int) -> list[dict]:
    print(account_id)
    print(service_name)
    print(page_size)


if __name__ == '__main__':

    for i in range(5):
        time.sleep(3)
        get_stuff('12345a','google',16)
        set_it_up()

    for i in range(5):
        time.sleep(3)
        set_it_up()

    for i in range(10):
        get_users('12345a','google')





