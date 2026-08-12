#非字母排序列表
places = ['barcelona', 'zurich', 'madrid', 'los angeles','milano']
print(places)
#验证sorted函数不改变列表原有顺序
print(sorted(places))
print(places)

places_sorted = sorted(places)
places_sorted.reverse()
print(places_sorted)
print(places)

places.reverse()
print(places)

places.reverse()
print(places)

places.sort()
print(places)

places.sort(reverse = True)
print(places)