cmake_minimum_required(VERSION 3.5...3.18)
project(SimplePyBindExample)

set(CMAKE_MODULE_PATH ${CMAKE_SOURCE_DIR}/cmake_modules ${CMAKE_MODULE_PATH})

set(BUILD_SHARED_LIBS FALSE)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall -ftemplate-depth=2000 -Werror -Wno-error=deprecated-declarations")

if (APPLE)
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wno-error=return-type-c-linkage -fcolor-diagnostics")
    set (CMAKE_SKIP_RPATH FALSE)
    set (CMAKE_SKIP_BUILD_RPATH FALSE)
    set (CMAKE_BUILD_WITH_INSTALL_RPATH FALSE)
    set (CMAKE_INSTALL_RPATH "")
    set (CMAKE_INSTALL_RPATH_USE_LINK_PATH FALSE)
    set (CMAKE_MACOSX_RPATH 1)
    set (CMAKE_SHARED_LINKER_FLAGS "${CMAKE_SHARED_LINKER_FLAGS} -Wl,-undefined -Wl,dynamic_lookup")
    set (CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} -Wl,-undefined -Wl,dynamic_lookup")
else()
    set (CMAKE_SHARED_LINKER_FLAGS "${CMAKE_SHARED_LINKER_FLAGS} -fuse-ld=gold")
    set (CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} -fuse-ld=gold")
endif()

find_package (Python3 COMPONENTS Interpreter Development REQUIRED) # the Development component is required, else we get an error: https://github.com/pybind/pybind11/issues/3996

execute_process(
    COMMAND ${Python3_EXECUTABLE} -m pybind11 --cmakedir
    OUTPUT_VARIABLE PYBIND11_CMAKE_DIR
    OUTPUT_STRIP_TRAILING_WHITESPACE
)
set(pybind11_DIR ${PYBIND11_CMAKE_DIR})

message(STATUS "Using pybind11 found at: ${pybind11_DIR}")
find_package(pybind11 REQUIRED)

# Create Python module
pybind11_add_module(lyric_module SHARED pybind_wrapper.cpp calculator.cpp)

set_target_properties(lyric_module PROPERTIES CXX_STANDARD 11 CXX_STANDARD_REQUIRED ON)

# Needed for importing the "lyric_module" module from the build directory
set(INIT_PY "${CMAKE_CURRENT_BINARY_DIR}/__init__.py")
if(NOT EXISTS ${INIT_PY})
    file(WRITE ${INIT_PY} "")
endif()

add_custom_command(TARGET lyric_module POST_BUILD
    COMMAND ${CMAKE_COMMAND} -E copy
            $<TARGET_FILE_DIR:lyric_module>/$<TARGET_FILE_NAME:lyric_module>
            ${CMAKE_CURRENT_BINARY_DIR}/$<TARGET_FILE_NAME:lyric_module>
)
