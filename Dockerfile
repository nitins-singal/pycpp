# Build this dockerfile by invoking=>  docker build -t lyric_py_cpp:1.0 -f Dockerfile .
FROM python:3.10-slim

WORKDIR /app

# Enable C++ builds
RUN apt-get update && \
    apt-get -y install g++ cmake vim gdb && \
    rm -rf /var/lib/apt/lists/*
	

COPY ./requirements.txt requirements.txt
#COPY ./.vscode/launch.json /app/.vscode/
# Use mount eventually for local env
# COPY src/ src/

RUN pip3 install -r requirements.txt --no-cache-dir

# BEST PRACTICE: Mount the source from repo and use. 
# Some of the arguments are needed to enable C++ debuging inside container
# docker run -v ./:/app/src -v ./.vscode:/app/.vscode --cap-add=SYS_PTRACE --security-opt seccomp:unconfined -it lyric_py_cpp:1.0 bash

# Issue the following command inside container to build it and install it.
## cd src; ./build_script.sh ; pip install -e .

#WORKDIR /app/src
#RUN rm -rf build
# Create a debug build
#RUN cmake -S. -Bbuild -D CMAKE_BUILD_TYPE=Debug

# Make the Build
#RUN cmake --build build -j

# ENV LD_LIBRARY_PATH /app/src/build/
# python script.py

# Expose a few ports.
# EXPOSE 8999 8888

