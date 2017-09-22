from conans import ConanFile, CMake
import os


class TestPackage(ConanFile):
    settings = "compiler", "build_type", "arch"
    generators = "cmake"
    
    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
        
    def imports(self):
        self.copy("*.lib", dst="bin", src="lib")
        self.copy("*.dylib*", dst="bin", src="lib")
        self.copy("*.dll", dst="bin", src="bin")
       
    def test(self):
        self.run(os.path.join("bin","test_package"))

