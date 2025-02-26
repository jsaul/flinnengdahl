%module flinnengdahl

%{
#include <exception>
#include "fe.h"
%}

%include <exception.i>
%include <std_except.i>
%include <std_string.i>
%include <std_vector.i>
%include <std_map.i>

namespace std {
        %template(_StringVector) vector<string>;
        %template(_StringVectorMap) map<string, vector<string>>;
}


%exception {
  try {
    $action
  }
  catch ( const std::out_of_range &e) {
    SWIG_exception(SWIG_ValueError, e.what());
  }
  catch ( const std::invalid_argument &e) {
    SWIG_exception(SWIG_ValueError, e.what());
  }
  catch ( const std::runtime_error &e) {
    SWIG_exception(SWIG_RuntimeError, e.what());
  }
  catch ( const std::exception &e) {
    SWIG_exception(SWIG_RuntimeError, e.what());
  }
  catch ( ... ) {
    SWIG_exception(SWIG_UnknownError, "C++ anonymous exception");
  }
}

%include "fe.h"
