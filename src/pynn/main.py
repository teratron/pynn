# import os
# import sys
#
# print(os.environ['SECRET'])
# print(os.environ['CONFIG_PATH'])
#
#
# def say_hello(name='World'):
#     return f'Hello {name}!'
#
#
# def add_one(number: int) -> int:
#     return number + 1
#
#
# def main():
#     name = ''
#     try:
#         name = sys.argv[1]
#     except IndexError:
#         name = input(f'Please enter your name:')
#     finally:
#         print(say_hello(name))
#
#
# if __name__ == '__main__':
#     main()
