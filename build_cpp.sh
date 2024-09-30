rm -rf cpp/build
# Create a debug build
cmake -S cpp -B cpp/build -D CMAKE_BUILD_TYPE=Debug

# Make the Build
cmake --build cpp/build -j

mkdir -p mylyric/lib/
# Copy the generated shared object file into the python module so that it can be packaged in wheel
cp cpp/build/lyric_module.* mylyric/lib/

# python setup.py bdist_wheel

# python setup.py clean --all 