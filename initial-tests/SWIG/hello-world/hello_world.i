%module Hello_world
%{
#define SWIG_FILE_WITH_INIT
#include "hello_world.h"
%}

%include "hello_world.h"
