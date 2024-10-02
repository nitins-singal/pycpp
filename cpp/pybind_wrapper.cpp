#include <pybind11/pybind11.h>
#include "calculator.h"

int simple_cpp_function(int a, int b) { 
    Calculator *c= new Calculator();
    return c->addnum(a,b);
    //return a + b; 
    }

namespace py = pybind11;
PYBIND11_MODULE(lyric_module, lyric_cpp)
{
    lyric_cpp.def("simple_cpp_function", &simple_cpp_function);

    py::class_<Calculator>(lyric_cpp, "Calculator")
    .def(py::init<>())  // Constructor
    .def("addnum", &Calculator::addnum, "A function that adds two numbers")
    .def("multnum", &Calculator::multnum, "A function that multiplies two numbers");
}
