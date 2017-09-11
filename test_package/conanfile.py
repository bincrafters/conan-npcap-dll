from conans import ConanFile, CMake
import os


class NpcapDllConanTest(ConanFile):
    settings = "compiler", "build_type", "arch"
    generators = "cmake"
    
    def build(self):
        cmake = CMake(self)
        # Current dir is "test_package/build/<build_id>" and CMakeLists.txt is in "test_package"
        cmake.configure(source_dir=self.conanfile_directory, build_dir="./")
        cmake.build()

    def imports(self):
        self.copy("*.lib", dst="bin", src="lib")
        self.copy("*.dylib*", dst="bin", src="lib")
        self.copy("*.dll", dst="bin", src="bin")

    def test(self):
        pass

