cmake_minimum_required(VERSION 3.4)
include (${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)

conan_basic_setup(TARGETS)

add_executable(app.bin main.cpp)

target_link_libraries(app.bin CONAN_PKG::db)
