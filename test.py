import os

try:
    import cal_num

except ModuleNotFoundError:
    print('cal_num module compiled')
    os.system('python build.py build_ext --inplace')
    import cal_num

print(cal_num.add(5, 10))
