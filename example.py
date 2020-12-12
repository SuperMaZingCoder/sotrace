from sotrace import open_link


dict_1 = {}
try:
    print(dict_1[1])
except Exception as e:
    open_link(e, 2)
