from conan.packager import ConanMultiPackager, os


if __name__ == "__main__":
    builder = ConanMultiPackager()
    builder.add_common_builds()
    builder.run()