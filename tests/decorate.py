import time


def take_up_time(func):

    def wrapper(*args, **kwargs):
        import time
        start = time.time()
        result = func(*args, **kwargs)
        print(f"Time taken: {time.time() - start}")
        return result

    return wrapper


@take_up_time
def test():
    for i in range(2):
        time.sleep(1)


class Person:
    name = 'tailiang'
    age = 19

    def __init__(self, name=None):
        self.name = name

    def keys(self):
        return ['name', 'age']

    def __getitem__(self, item):
        return getattr(self, item)


if __name__ == "__main__":
    print(dict(Person("兜底户")))
    # test()
