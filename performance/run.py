import sys

from perf_desc_without_wkd import run_test_1
from perf_desc import run_test_2
from perf_plain import run_test_3
from perf_property import run_test_4
from perf_setattr import run_test_5

def get_avr(total_dict, iters):
    for key, value in total_dict.items():
        total_dict[key] /= iters
    
    return total_dict

def main():
    totals = {
        'desc_without_wkd': 0,
        'desc': 0,
        'plain': 0,
        'property': 0,
        'setattr': 0
    }

    iterations = 1000000

    for i in range(int(sys.argv[-1])):
        print(i)
        totals['desc_without_wkd'] += run_test_1(iterations)
        print('.', end='', flush=True)
        totals['desc'] += run_test_2(iterations)
        print('.', end='', flush=True)
        totals['plain'] += run_test_3(iterations)
        print('.', end='', flush=True)
        totals['property'] += run_test_4(iterations)
        print('.', end='', flush=True)
        totals['setattr'] += run_test_5(iterations)
        print('.')
        
        print('T:', totals)

    print('Final total:', totals)
    print('Final Avr:', get_avr(totals, int(sys.argv[-1])))

if __name__ == '__main__': main()
