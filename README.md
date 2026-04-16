Build required shared objects:

```bash
git clone https://github.com/FFmpeg/FFmpeg.git
cd FFmpeg
git checkout n8.0.1
./configure --prefix=$(pwd)/build --disable-everything --disable-programs --disable-doc --disable-static --enable-shared --enable-avfilter --enable-avutil --enable-filter=surround --enable-filter=aformat --enable-filter=aresample
make -j$(nproc) && make install
# Retrieve libavfilter.so.11, libavutil.so.60, libswresample.so.6 from ./build/lib
```
