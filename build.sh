#!/bin/sh

conan create connector alex/dev --build missing -o '*:shared=True' && 
conan create db alex/dev --build missing -o '*:shared=True' &&
mkdir app/build &&
conan install app/ --build=missing -o '*:shared=True' -if app/build/ &&
cmake -GNinja -B./app/build -H./app &&
ninja -C ./app/build &&
./app/build/bin/app.bin

