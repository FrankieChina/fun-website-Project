# import time
import datetime
# import random
# import json
import requests

quote_api_url = "https://api.quotable.io/quotes/random"
response = requests.get(quote_api_url)
response_json = response.json()
quote = response_json[0]["content"]
print(quote)

# current_time = time.time()
# print(current_time)
#
#
# def speed_calc_decorator(function):
#     def speed_calc():
#         start_time = time.time()
#         function()
#         time_difference = time.time() - start_time
#         print(f"Speed calculation took {time_difference} for {function.__name__}")
#
#     return speed_calc
#
#
# @speed_calc_decorator
# def fast_function():
#     for i in range(1000000):
#         i * i
#
#
# @speed_calc_decorator
# def slow_function():
#     for i in range(10000000):
#         i * i
# fast_function()
# slow_function()

# def delay_decorator(function):
#     def wrapper_function():
#         time.sleep(3)
#         function()
#
#     return wrapper_function
#
#
# @delay_decorator
# def say_hello():
#     print("Hello")
#
#
# def say_goodbye():
#     print("Goodbye")
#
#
# def say_greetings():
#     print("How are you?")
#
# inputs = eval(input())
#
#
# def decorator_function(function):
#     def wrapper(*args):
#         print(f"{function.__name__}{args}")
#         result = function(args[0], args[1], args[2])
#         print(f"It return: {result}")
#     return wrapper
#
#
# @decorator_function
# def a_function(a, b, c):
#     return a * b * c
#
#
# a_function(inputs[0], inputs[1], inputs[2])
