import random

def random_generator(data_type, data_range, num):
    try:
        result = []
        if data_type == "int":
            for i in range(num):
                result.append(random.randint(data_range[0], data_range[1]))
        elif data_type == "float":
            for i in range(num):
                result.append(random.uniform(data_range[0], data_range[1]))
        elif data_type == "str":
            for i in range(num):
                result.append(''.join(random.choices(data_range, k=random.randint(1, 10))))
        elif data_type == "comb":
            if not isinstance(data_range, list):
                raise TypeError("Data range must be a list")
            elif len(data_range) < 2:
                raise ValueError("Data range must contain at least 2 elements")
            for i in range(num):
                result.append(random.sample(data_range, k=random.randint(1, len(data_range))))
        else:
            raise ValueError("Invalid data type")
        return result
    except TypeError:
        print("Data range must be a list")
    except ValueError as e:
        print(e)
    except:
        print("An unexpected error occurred. Please try again.")
