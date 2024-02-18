import sys
import time

def print_and_delete_list(my_list, duration):
    print(my_list, end='', flush=True)
    time.sleep(duration)
    print('\r' + ' ' * len(str(my_list)), end='', flush=True)

# Example usage:
my_list = [1, 2, 3, 4, 5]
display_duration = 3
print_and_delete_list(my_list, display_duration)