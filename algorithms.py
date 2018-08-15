# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_algorithms')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_algorithms')
    _algorithms = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_algorithms', [dirname(__file__)])
        except ImportError:
            import _algorithms
            return _algorithms
        try:
            _mod = imp.load_module('_algorithms', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _algorithms = swig_import_helper()
    del swig_import_helper
else:
    import _algorithms
del _swig_python_version_info

try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except __builtin__.Exception:
    class _object:
        pass
    _newclass = 0

import gippy

def acca(arg1, filename, arg3, arg4, arg5=5, arg6=10, arg7=4000):
    """
    acca(GeoImage arg1, std::string filename, float arg3, float arg4, int arg5=5, int arg6=10, int arg7=4000) -> GeoImage

    Parameters
    ----------
    arg1: gip::GeoImage const &
    filename: std::string
    arg3: float
    arg4: float
    arg5: int
    arg6: int
    arg7: int

    """
    return _algorithms.acca(arg1, filename, arg3, arg4, arg5, arg6, arg7)

def fmask(geoimg, filename, arg3=3, arg4=5):
    """
    fmask(GeoImage geoimg, std::string filename, int arg3=3, int arg4=5) -> GeoImage

    Parameters
    ----------
    geoimg: gip::GeoImage const &
    filename: std::string
    arg3: int
    arg4: int

    """
    return _algorithms.fmask(geoimg, filename, arg3, arg4)

def cookie_cutter(*args, **kwargs):
    """
    cookie_cutter(vector_GeoImage geoimgs, std::string filename, GeoFeature feature, bool crop=False, std::string proj, float xres=1.0, float yres=1.0, int interpolation=0, gip::dictionary options) -> GeoImage

    Parameters
    ----------
    geoimgs: std::vector< gip::GeoImage,std::allocator< gip::GeoImage > > const &
    filename: std::string
    feature: gip::GeoFeature
    crop: bool
    proj: std::string
    xres: float
    yres: float
    interpolation: int
    options: gip::dictionary

    """
    return _algorithms.cookie_cutter(*args, **kwargs)

def kmeans(arg1, arg2, classes=5, iterations=5, threshold=1.0, num_random=500):
    """
    kmeans(GeoImage arg1, std::string arg2, unsigned int classes=5, unsigned int iterations=5, float threshold=1.0, unsigned int num_random=500) -> GeoImage

    Parameters
    ----------
    arg1: gip::GeoImage const &
    arg2: std::string
    classes: unsigned int
    iterations: unsigned int
    threshold: float
    num_random: unsigned int

    """
    return _algorithms.kmeans(arg1, arg2, classes, iterations, threshold, num_random)

def indices(*args, **kwargs):
    """
    indices(GeoImage geoimg, svector products, std::string filename) -> GeoImage

    Parameters
    ----------
    geoimg: gip::GeoImage const &
    products: std::vector< std::string,std::allocator< std::string > > const &
    filename: std::string

    """
    return _algorithms.indices(*args, **kwargs)

def linear_transform(geoimg, coef, filename):
    """
    linear_transform(GeoImage geoimg, CImg< float > coef, std::string filename) -> GeoImage

    Parameters
    ----------
    geoimg: gip::GeoImage const &
    coef: CImg< float >
    filename: std::string

    """
    return _algorithms.linear_transform(geoimg, coef, filename)

def pansharp_brovey(*args, **kwargs):
    """
    pansharp_brovey(GeoImage geoimg, GeoImage panimg, CImg< float > weights, std::string filename) -> GeoImage

    Parameters
    ----------
    geoimg: gip::GeoImage const &
    panimg: gip::GeoImage const &
    weights: CImg< float >
    filename: std::string

    """
    return _algorithms.pansharp_brovey(*args, **kwargs)

def rxd(*args, **kwargs):
    """
    rxd(GeoImage geoimg, std::string filename) -> GeoImage

    Parameters
    ----------
    geoimg: gip::GeoImage const &
    filename: std::string

    """
    return _algorithms.rxd(*args, **kwargs)

def spectral_statistics(*args, **kwargs):
    """
    spectral_statistics(GeoImage arg1, std::string filename) -> GeoImage

    Parameters
    ----------
    arg1: gip::GeoImage const &
    filename: std::string

    """
    return _algorithms.spectral_statistics(*args, **kwargs)
# This file is compatible with both classic and new-style classes.


