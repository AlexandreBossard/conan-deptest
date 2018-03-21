from conans import ConanFile, CMake


class DbConan(ConanFile):
    name = "db"
    version = "0.0.3"
    license = "<Put the package license here>"
    url = "poof"
    description = "test db lib"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"
    exports_sources = "CMakeLists.txt", "include/*", "src/*"


    def requirements(self):
        self.requires("connector/0.0.1@%s/%s" % (self.user, self.channel))

    def build(self):
        cmake = CMake(self)
        cmake.verbose = True
        if self.options.shared:
            cmake.definitions["BUILD_SHARED_LIBS"] = "ON"
        cmake.configure()
        cmake.build()
        cmake.install()

        # Explicit way:
        # self.run('cmake %s/hello %s' % (self.source_folder, cmake.command_line))
        # self.run("cmake --build . %s" % cmake.build_config)

    # def package(self):
        # self.copy("*.h", dst="include", src="hello")
        # self.copy("*hello.lib", dst="lib", keep_path=False)
        # self.copy("*.dll", dst="bin", keep_path=False)
        # self.copy("*.so", dst="lib", keep_path=False)
        # self.copy("*.dylib", dst="lib", keep_path=False)
        # self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["db"]
