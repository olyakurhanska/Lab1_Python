
import timeit

sizes = [100, 1000, 10000]
repeats = 5

print("Порівняння часу виконання операцій")
print("Час у мілісекундах\n")

print(f"{'n':<8} {'list':<12} {'set':<12} {'dict':<12} {'Унікальні list':<18} {'Унікальні set':<15}")

for n in sizes:
    numbers = list(range(n))
    number_set = set(numbers)
    number_dict = {x: True for x in numbers}
    target = n - 1

    list_time = timeit.timeit(lambda: target in numbers, number=1000) / 1000 * 1000
    set_time = timeit.timeit(lambda: target in number_set, number=1000) / 1000 * 1000
    dict_time = timeit.timeit(lambda: target in number_dict, number=1000) / 1000 * 1000

    data = list(range(n)) + list(range(n // 2))

    def unique_list():
        result = []
        for x in data:
            if x not in result:
                result.append(x)
        return result

    def unique_set():
        result = set()
        for x in data:
            result.add(x)
        return result

    list_unique_time = timeit.timeit(unique_list, number=repeats) / repeats * 1000
    set_unique_time = timeit.timeit(unique_set, number=repeats) / repeats * 1000

    print(f"{n:<8} {list_time:<12.6f} {set_time:<12.6f} {dict_time:<12.6f} {list_unique_time:<18.6f} {set_unique_time:<15.6f}")
