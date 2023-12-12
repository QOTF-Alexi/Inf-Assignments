import time


def timer_decorator(toDecorate):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = toDecorate()
        end_time = time.time()
        run_time = end_time - start_time
        print(f"Program ran for {run_time} seconds.")
        return result
    return wrapper


@timer_decorator
def main():
    print("Vadim blyat")


if __name__ == "__main__":
    main()
