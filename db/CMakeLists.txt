cmake_minimum_required(VERSION 3.4)
project(db)
include (${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)

conan_basic_setup(TARGETS)

add_library(db 
  src/db.cpp
)

target_include_directories(db PUBLIC
  $<BUILD_INTERFACE:${PROJECT_SOURCE_DIR}/include>
  $<INSTALL_INTERFACE:include>
)

install(TARGETS db 
  EXPORT db
  LIBRARY DESTINATION lib
  ARCHIVE DESTINATION lib
)

install(DIRECTORY include
  DESTINATION .
)

target_link_libraries(db CONAN_PKG::connector)
