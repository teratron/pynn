# @dataclass(slots=True, frozen=True)
# class _Call:
#     # class Callback(NamedTuple):
#     call: Callable[[float], float]
#     initialize: Callable[[Any, Any], None]
#     set_props: Callable[[Any, Any], None]
#     verify: Callable[[Any, Any], float]
#     query: Callable[[Any, Any], list[float]]
#     train: Callable[[Any, Any], tuple[int, float]]
#     and_train: Callable[[Any, Any], tuple[int, float]]
#     write: Callable[[Any, Any], None]


# import inspect
# from functools import partial
# from typing import (
#     Any,
#     Callable,
#     Iterable,
#     List,
#     Optional,
#     Tuple,
#     Type,
#     TypeVar,
#     Union,
#     overload,
# )
#
# T = TypeVar("T")
#
#
# Result = Iterable[Union[Any, Tuple[Any], Tuple[str, Any], Tuple[str, Any, Any]]]
# RichReprResult = Result
#
#
# class ReprError(Exception):
#     """An error occurred when attempting to build a repr."""
#
#
# @overload
# def auto(cls: Optional[Type[T]]) -> Type[T]:
#     ...
#
#
# @overload
# def auto(*, angular: bool = False) -> Callable[[Type[T]], Type[T]]:
#     ...
#
#
# def auto(
#     cls: Optional[Type[T]] = None,
#     *,
#     angular: Optional[bool] = None
# ) -> Union[Type[T], Callable[[Type[T]], Type[T]]]:
#     """Class decorator to create __repr__ from __rich_repr__"""
#
#     def do_replace(cls: Type[T], angular: Optional[bool] = None) -> Type[T]:
#         def auto_repr(self: T) -> str:
#             """Create repr string from __rich_repr__"""
#             repr_str: List[str] = []
#             append = repr_str.append
#
#             angular: bool = getattr(self.__rich_repr__, "angular", False)  # type: ignore[attr-defined]
#             for arg in self.__rich_repr__():  # type: ignore[attr-defined]
#                 if isinstance(arg, tuple):
#                     if len(arg) == 1:
#                         append(repr(arg[0]))
#                     else:
#                         key, value, *default = arg
#                         if key is None:
#                             append(repr(value))
#                         else:
#                             if default and default[0] == value:
#                                 continue
#                             append(f"{key}={value!r}")
#                 else:
#                     append(repr(arg))
#             if angular:
#                 return f"<{self.__class__.__name__} {' '.join(repr_str)}>"
#             else:
#                 return f"{self.__class__.__name__}({', '.join(repr_str)})"
#
#         def auto_rich_repr(self: Type[T]) -> Result:
#             """Auto generate __rich_rep__ from signature of __init__"""
#             try:
#                 signature = inspect.signature(self.__init__)
#                 for name, param in signature.parameters.items():
#                     if param.kind == param.POSITIONAL_ONLY:
#                         yield getattr(self, name)
#                     elif param.kind in (
#                         param.POSITIONAL_OR_KEYWORD,
#                         param.KEYWORD_ONLY,
#                     ):
#                         if param.default == param.empty:
#                             yield getattr(self, param.name)
#                         else:
#                             yield param.name, getattr(self, param.name), param.default
#             except Exception as error:
#                 raise ReprError(
#                     f"Failed to auto generate __rich_repr__; {error}"
#                 ) from None
#
#         if not hasattr(cls, "__rich_repr__"):
#             auto_rich_repr.__doc__ = "Build a rich repr"
#             cls.__rich_repr__ = auto_rich_repr  # type: ignore[attr-defined]
#
#         auto_repr.__doc__ = "Return repr(self)"
#         cls.__repr__ = auto_repr  # type: ignore[assignment]
#         if angular is not None:
#             cls.__rich_repr__.angular = angular  # type: ignore[attr-defined]
#         return cls
#
#     if cls is None:
#         return partial(do_replace, angular=angular)
#     else:
#         return do_replace(cls, angular=angular)
#
#
# @overload
# def rich_repr(cls: Optional[Type[T]]) -> Type[T]:
#     ...
#
#
# @overload
# def rich_repr(*, angular: bool = False) -> Callable[[Type[T]], Type[T]]:
#     ...
#
#
# def rich_repr(
#     cls: Optional[Type[T]] = None,
#     *,
#     angular: bool = False
# ) -> Union[Type[T], Callable[[Type[T]], Type[T]]]:
#     if cls is None:
#         return auto(angular=angular)
#     else:
#         return auto(cls)
#
#
# if __name__ == "__main__":
#
#     @auto
#     class Foo:
#         def __rich_repr__(self) -> Result:
#             yield "foo"
#             yield "bar", {"shopping": ["eggs", "ham", "pineapple"]}
#             yield "buy", "hand sanitizer"
#
#     foo = Foo()
#
#     from rich.console import Console
#
#     console = Console()
#
#     console.rule("Standard repr")
#     console.print(foo)
#     console.print(foo, width=60)
#     console.print(foo, width=30)
#
#     console.rule("Angular repr")
#     Foo.__rich_repr__.angular = True  # type: ignore[attr-defined]
#     console.print(foo)
#     console.print(foo, width=60)
#     console.print(foo, width=30)


####################################################################################


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


####################################################################################
