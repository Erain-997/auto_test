import itertools
import string
import random


# 生成杂合字段
def generate_data_all(length):
    # 定义可能的字符集
    letters = string.ascii_letters  # 所有ASCII字母
    digits = string.digits  # 所有数字
    symbols = string.punctuation  # 所有标点符号
    test_input = ""
    # 生成所有可能的组合
    for combo in itertools.product([letters, digits, symbols], repeat=length):
        # ''.join()用于将字符元组转换为字符串
        # random.choice()用于随机选择是否包含大小写字母、数字或符号
        test_input = ''.join(random.choice(combo) for combo in combo)
        # print(test_input)
    return test_input


# 生成的字符总长
def generate_data_choose(num_combinations):
    # 定义可能的字符集
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # 定义每种字符类型要生成的组合数量
    # 生成每种字符类型的组合
    for char_type in [letters, digits, symbols]:
        for _ in range(num_combinations):
            # 随机选择字符集中的字符来生成固定长度的组合
            combination_length = random.randint(1, 16)  # 可以根据需要调整长度范围
            test_input = ''.join(random.choice(char_type) for _ in range(combination_length))
            print(test_input)
