# Local Setup

# Create the virtual env. I have used 3.12 but one could use 3.10 as well depending on what python you have

## virtualenv -p 3.12 ./venv
## source ./venv/bin/activate
## pip install -r requirements.txt

# Install cmake 
brew install cmake

# Generate makefiles etc. This one is for creating Debug build to enable debugging
## rm -rf build
# Create a debug build
## cmake -Scpp -Bcpp/build -D CMAKE_BUILD_TYPE=Debug

# Make the Build
## cmake --build cpp/build -j

## mkdir -p mylyric/lib/
# Copy the generated shared object file into the python module so that it can be packaged in wheel
## cp cpp/build/lyric_module.* mylyric/lib/


# In vscode for ddebugging with debugpy use this
## python -Xfrozen_modules=off script.py


# Building Dockerfile 
## docker build -t lyric_py_cpp:1.0 -f Dockerfile .
# Running the container
# docker run -v ./:/app/src --cap-add=SYS_PTRACE --security-opt seccomp:unconfined -it lyric_py_cpp:1.0 bash

# Building the project inside container.
## cd src