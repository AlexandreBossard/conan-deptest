from conans import ConanFile, CMake


class ConnectorConan(ConanFile):
    name = "connector"
    version = "0.0.1"
    license = "<Put the package license here>"
    url = "paf"
    description = "connector test lib"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"
    exports_sources = "src/*", "include/*", "CMakeLists.txt"

    def build(self):
        cmake = CMake(self)
        if self.options.shared:
            cmake.definitions["BUILD_SHARED_LIBS"] = "ON"
        cmake.configure()
        cmake.build()
        cmake.install()

        # Explicit way:
        # self.run('cmake %s/src %s' % (self.source_folder, cmake.command_line))
        # self.run("cmake --build . %s" % cmake.build_config)

    # def package(self):
        # self.copy("*.h", dst="include", src="src")
        # self.copy("*.lib", dst="lib", keep_path=False)
        # self.copy("*.dll", dst="bin", keep_path=False)
        # self.copy("*.dylib*", dst="lib", keep_path=False)
        # self.copy("*.so", dst="lib", keep_path=False)
        # self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["connector"]
