# def compare_dictionaries(dict1, dict2) -> bool:
#     if dict1 is None or dict2 is None:
#         return False
#
#     if not isinstance(dict1, dict) or not isinstance(dict2, dict):
#         return False
#
#     shared_keys = set(dict1.keys()) & set(dict2.keys())
#
#     if not (len(shared_keys) == len(dict1.keys()) and len(shared_keys) == len(dict2.keys())):
#         print('Not all keys are shared')
#         return False
#
#     dicts_are_equal = True
#     for key in dict1.keys():
#         if isinstance(dict1[key], dict) or isinstance(dict2[key], dict):
#             dicts_are_equal = dicts_are_equal and compare_dictionaries(dict1[key], dict2[key])
#         else:
#             dicts_are_equal = dicts_are_equal and all(atleast_1d(dict1[key] == dict2[key]))
#
#     return dicts_are_equal


# def dict_compare(
#         d1: dict[str, Any],
#         d2: dict[str, Any]
# ) -> tuple[set[Any], set[Any], dict[str, Any], set[Any]]:
#     print("&keys", set(d1.keys()) & set(d2.keys()))
#     print("&items", set(d1.items()) & set(d2.items()))
#
#     print("^keys", set(d2.keys()) ^ set(d1.keys()))
#     print("^items", set(d2.items()) ^ set(d1.items()))
#
#     print("|keys", set(d2.keys()) | set(d1.keys()))
#     print("|items", set(d2.items()) | set(d1.items()))
#
#     d1_keys = set(d1.keys())
#     d2_keys = set(d2.keys())
#     shared_keys = d1_keys.intersection(d2_keys)
#     _added = d1_keys - d2_keys
#     _removed = d2_keys - d1_keys
#     _modified = {i: (d1[i], d2[i]) for i in shared_keys if d1[i] != d2[i]}
#     _same = set(i for i in shared_keys if d1[i] == d2[i])
#
#     return _added, _removed, _modified, _same
#
#
# if __name__ == "__main__":
#     x = dict(a=1, b=2, c=5, d=3)
#     y = dict(a=2, b=2, d=0)
#     added, removed, modified, same = dict_compare(x, y)
#     print(added, removed, modified, same)