# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _flinnengdahl
else:
    import _flinnengdahl

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


class SwigPyIterator(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _flinnengdahl.delete_SwigPyIterator

    def value(self) -> "PyObject *":
        return _flinnengdahl.SwigPyIterator_value(self)

    def incr(self, n: "size_t"=1) -> "swig::SwigPyIterator *":
        return _flinnengdahl.SwigPyIterator_incr(self, n)

    def decr(self, n: "size_t"=1) -> "swig::SwigPyIterator *":
        return _flinnengdahl.SwigPyIterator_decr(self, n)

    def distance(self, x: "SwigPyIterator") -> "ptrdiff_t":
        return _flinnengdahl.SwigPyIterator_distance(self, x)

    def equal(self, x: "SwigPyIterator") -> "bool":
        return _flinnengdahl.SwigPyIterator_equal(self, x)

    def copy(self) -> "swig::SwigPyIterator *":
        return _flinnengdahl.SwigPyIterator_copy(self)

    def next(self) -> "PyObject *":
        return _flinnengdahl.SwigPyIterator_next(self)

    def __next__(self) -> "PyObject *":
        return _flinnengdahl.SwigPyIterator___next__(self)

    def previous(self) -> "PyObject *":
        return _flinnengdahl.SwigPyIterator_previous(self)

    def advance(self, n: "ptrdiff_t") -> "swig::SwigPyIterator *":
        return _flinnengdahl.SwigPyIterator_advance(self, n)

    def __eq__(self, x: "SwigPyIterator") -> "bool":
        return _flinnengdahl.SwigPyIterator___eq__(self, x)

    def __ne__(self, x: "SwigPyIterator") -> "bool":
        return _flinnengdahl.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n: "ptrdiff_t") -> "swig::SwigPyIterator &":
        return _flinnengdahl.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n: "ptrdiff_t") -> "swig::SwigPyIterator &":
        return _flinnengdahl.SwigPyIterator___isub__(self, n)

    def __add__(self, n: "ptrdiff_t") -> "swig::SwigPyIterator *":
        return _flinnengdahl.SwigPyIterator___add__(self, n)

    def __sub__(self, *args) -> "ptrdiff_t":
        return _flinnengdahl.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self

# Register SwigPyIterator in _flinnengdahl:
_flinnengdahl.SwigPyIterator_swigregister(SwigPyIterator)

class _StringVector(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self) -> "swig::SwigPyIterator *":
        return _flinnengdahl._StringVector_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self) -> "bool":
        return _flinnengdahl._StringVector___nonzero__(self)

    def __bool__(self) -> "bool":
        return _flinnengdahl._StringVector___bool__(self)

    def __len__(self) -> "std::vector< std::string >::size_type":
        return _flinnengdahl._StringVector___len__(self)

    def __getslice__(self, i: "std::vector< std::string >::difference_type", j: "std::vector< std::string >::difference_type") -> "std::vector< std::string,std::allocator< std::string > > *":
        return _flinnengdahl._StringVector___getslice__(self, i, j)

    def __setslice__(self, *args) -> "void":
        return _flinnengdahl._StringVector___setslice__(self, *args)

    def __delslice__(self, i: "std::vector< std::string >::difference_type", j: "std::vector< std::string >::difference_type") -> "void":
        return _flinnengdahl._StringVector___delslice__(self, i, j)

    def __delitem__(self, *args) -> "void":
        return _flinnengdahl._StringVector___delitem__(self, *args)

    def __getitem__(self, *args) -> "std::vector< std::string >::value_type const &":
        return _flinnengdahl._StringVector___getitem__(self, *args)

    def __setitem__(self, *args) -> "void":
        return _flinnengdahl._StringVector___setitem__(self, *args)

    def pop(self) -> "std::vector< std::string >::value_type":
        return _flinnengdahl._StringVector_pop(self)

    def append(self, x: "std::vector< std::string >::value_type const &") -> "void":
        return _flinnengdahl._StringVector_append(self, x)

    def empty(self) -> "bool":
        return _flinnengdahl._StringVector_empty(self)

    def size(self) -> "std::vector< std::string >::size_type":
        return _flinnengdahl._StringVector_size(self)

    def swap(self, v: "_StringVector") -> "void":
        return _flinnengdahl._StringVector_swap(self, v)

    def begin(self) -> "std::vector< std::string >::iterator":
        return _flinnengdahl._StringVector_begin(self)

    def end(self) -> "std::vector< std::string >::iterator":
        return _flinnengdahl._StringVector_end(self)

    def rbegin(self) -> "std::vector< std::string >::reverse_iterator":
        return _flinnengdahl._StringVector_rbegin(self)

    def rend(self) -> "std::vector< std::string >::reverse_iterator":
        return _flinnengdahl._StringVector_rend(self)

    def clear(self) -> "void":
        return _flinnengdahl._StringVector_clear(self)

    def get_allocator(self) -> "std::vector< std::string >::allocator_type":
        return _flinnengdahl._StringVector_get_allocator(self)

    def pop_back(self) -> "void":
        return _flinnengdahl._StringVector_pop_back(self)

    def erase(self, *args) -> "std::vector< std::string >::iterator":
        return _flinnengdahl._StringVector_erase(self, *args)

    def __init__(self, *args):
        _flinnengdahl._StringVector_swiginit(self, _flinnengdahl.new__StringVector(*args))

    def push_back(self, x: "std::vector< std::string >::value_type const &") -> "void":
        return _flinnengdahl._StringVector_push_back(self, x)

    def front(self) -> "std::vector< std::string >::value_type const &":
        return _flinnengdahl._StringVector_front(self)

    def back(self) -> "std::vector< std::string >::value_type const &":
        return _flinnengdahl._StringVector_back(self)

    def assign(self, n: "std::vector< std::string >::size_type", x: "std::vector< std::string >::value_type const &") -> "void":
        return _flinnengdahl._StringVector_assign(self, n, x)

    def resize(self, *args) -> "void":
        return _flinnengdahl._StringVector_resize(self, *args)

    def insert(self, *args) -> "void":
        return _flinnengdahl._StringVector_insert(self, *args)

    def reserve(self, n: "std::vector< std::string >::size_type") -> "void":
        return _flinnengdahl._StringVector_reserve(self, n)

    def capacity(self) -> "std::vector< std::string >::size_type":
        return _flinnengdahl._StringVector_capacity(self)
    __swig_destroy__ = _flinnengdahl.delete__StringVector

# Register _StringVector in _flinnengdahl:
_flinnengdahl._StringVector_swigregister(_StringVector)

class _StringVectorMap(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self) -> "swig::SwigPyIterator *":
        return _flinnengdahl._StringVectorMap_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self) -> "bool":
        return _flinnengdahl._StringVectorMap___nonzero__(self)

    def __bool__(self) -> "bool":
        return _flinnengdahl._StringVectorMap___bool__(self)

    def __len__(self) -> "std::map< std::string,std::vector< std::string > >::size_type":
        return _flinnengdahl._StringVectorMap___len__(self)
    def __iter__(self):
        return self.key_iterator()
    def iterkeys(self):
        return self.key_iterator()
    def itervalues(self):
        return self.value_iterator()
    def iteritems(self):
        return self.iterator()

    def __getitem__(self, key: "std::map< std::string,std::vector< std::string > >::key_type const &") -> "std::map< std::string,std::vector< std::string > >::mapped_type const &":
        return _flinnengdahl._StringVectorMap___getitem__(self, key)

    def __delitem__(self, key: "std::map< std::string,std::vector< std::string > >::key_type const &") -> "void":
        return _flinnengdahl._StringVectorMap___delitem__(self, key)

    def has_key(self, key: "std::map< std::string,std::vector< std::string > >::key_type const &") -> "bool":
        return _flinnengdahl._StringVectorMap_has_key(self, key)

    def keys(self) -> "PyObject *":
        return _flinnengdahl._StringVectorMap_keys(self)

    def values(self) -> "PyObject *":
        return _flinnengdahl._StringVectorMap_values(self)

    def items(self) -> "PyObject *":
        return _flinnengdahl._StringVectorMap_items(self)

    def __contains__(self, key: "std::map< std::string,std::vector< std::string > >::key_type const &") -> "bool":
        return _flinnengdahl._StringVectorMap___contains__(self, key)

    def key_iterator(self) -> "swig::SwigPyIterator *":
        return _flinnengdahl._StringVectorMap_key_iterator(self)

    def value_iterator(self) -> "swig::SwigPyIterator *":
        return _flinnengdahl._StringVectorMap_value_iterator(self)

    def __setitem__(self, *args) -> "void":
        return _flinnengdahl._StringVectorMap___setitem__(self, *args)

    def asdict(self) -> "PyObject *":
        return _flinnengdahl._StringVectorMap_asdict(self)

    def __init__(self, *args):
        _flinnengdahl._StringVectorMap_swiginit(self, _flinnengdahl.new__StringVectorMap(*args))

    def empty(self) -> "bool":
        return _flinnengdahl._StringVectorMap_empty(self)

    def size(self) -> "std::map< std::string,std::vector< std::string > >::size_type":
        return _flinnengdahl._StringVectorMap_size(self)

    def swap(self, v: "_StringVectorMap") -> "void":
        return _flinnengdahl._StringVectorMap_swap(self, v)

    def begin(self) -> "std::map< std::string,std::vector< std::string > >::iterator":
        return _flinnengdahl._StringVectorMap_begin(self)

    def end(self) -> "std::map< std::string,std::vector< std::string > >::iterator":
        return _flinnengdahl._StringVectorMap_end(self)

    def rbegin(self) -> "std::map< std::string,std::vector< std::string > >::reverse_iterator":
        return _flinnengdahl._StringVectorMap_rbegin(self)

    def rend(self) -> "std::map< std::string,std::vector< std::string > >::reverse_iterator":
        return _flinnengdahl._StringVectorMap_rend(self)

    def clear(self) -> "void":
        return _flinnengdahl._StringVectorMap_clear(self)

    def get_allocator(self) -> "std::map< std::string,std::vector< std::string > >::allocator_type":
        return _flinnengdahl._StringVectorMap_get_allocator(self)

    def count(self, x: "std::map< std::string,std::vector< std::string > >::key_type const &") -> "std::map< std::string,std::vector< std::string > >::size_type":
        return _flinnengdahl._StringVectorMap_count(self, x)

    def erase(self, *args) -> "void":
        return _flinnengdahl._StringVectorMap_erase(self, *args)

    def find(self, x: "std::map< std::string,std::vector< std::string > >::key_type const &") -> "std::map< std::string,std::vector< std::string > >::iterator":
        return _flinnengdahl._StringVectorMap_find(self, x)

    def lower_bound(self, x: "std::map< std::string,std::vector< std::string > >::key_type const &") -> "std::map< std::string,std::vector< std::string > >::iterator":
        return _flinnengdahl._StringVectorMap_lower_bound(self, x)

    def upper_bound(self, x: "std::map< std::string,std::vector< std::string > >::key_type const &") -> "std::map< std::string,std::vector< std::string > >::iterator":
        return _flinnengdahl._StringVectorMap_upper_bound(self, x)
    __swig_destroy__ = _flinnengdahl.delete__StringVectorMap

# Register _StringVectorMap in _flinnengdahl:
_flinnengdahl._StringVectorMap_swigregister(_StringVectorMap)

class FlinnEngdahl(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self):
        _flinnengdahl.FlinnEngdahl_swiginit(self, _flinnengdahl.new_FlinnEngdahl())

    def read(self, filename: "char const *") -> "bool":
        return _flinnengdahl.FlinnEngdahl_read(self, filename)

    def setCategory(self, c: "char const *") -> "void":
        return _flinnengdahl.FlinnEngdahl_setCategory(self, c)

    def number(self, lat: "double", lon: "double") -> "int":
        return _flinnengdahl.FlinnEngdahl_number(self, lat, lon)

    def name(self, *args) -> "std::string const &":
        return _flinnengdahl.FlinnEngdahl_name(self, *args)
    __swig_destroy__ = _flinnengdahl.delete_FlinnEngdahl

# Register FlinnEngdahl in _flinnengdahl:
_flinnengdahl.FlinnEngdahl_swigregister(FlinnEngdahl)


def many(runs: "size_t"=100000) -> "void":
    return _flinnengdahl.many(runs)

cvar = _flinnengdahl.cvar

