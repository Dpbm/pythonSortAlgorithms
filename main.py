from random import sample, randint


def bubble(data):
    changed = "i"
    while changed != "n":
        changed = "n"
        for index in range(len(data[:-1])):
            if(data[index] > data[index + 1]):
                data[index+1], data[index] = data[index], data[index+1]
                changed = "y"

    return data


def insertion(data):

    def get_insert_index(data, actual_index):
        inner_index = actual_index - 1
        value = data[actual_index]

        while value < data[inner_index] and inner_index >= 0:
            inner_index -= 1

        return inner_index + 1

    for index in range(1, len(data)):

        if(data[index] < data[index - 1]):
            value = data[index]
            data.insert(get_insert_index(data, index), value)
            data.pop(index+1)

    return data


def quick(data):
    if(len(data) == 0):
        return[]
    pivot = data[-1]
    less_then = [value for value in data if value < pivot]
    greater_then = [value for value in data if value > pivot]
    equals = [value for value in data if value == pivot]
    return([*quick(less_then), *equals, *quick(greater_then)])


def bogo(data):

    from random import shuffle

    def is_sorted(values):
        sorted = True
        for index in range(len(values)-1):
            if(values[index] > values[index+1]):
                sorted = False
                break
        return sorted

    while not is_sorted(data):
        shuffle(data)

    return data


def select(data):
    sorted_data = []

    while len(data) > 0:
        smallest = 0

        for index in range(len(data)):
            if data[index] < data[smallest]:
                smallest = index
        sorted_data.append(data[smallest])
        data.pop(smallest)
    return sorted_data


def bucket(data, max_len=101):
    buckets = [[] for _ in range(max_len)]

    for number in data:
        buckets[number].append(number)

    result = []
    for bucket in buckets:
        for element in bucket:
            result.append(element)

    return result


random_sample = [randint(1, 100) for _ in range(80)]
print(random_sample)
print(bucket(random_sample))
