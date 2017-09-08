from conan.packager import ConanMultiPackager


if __name__ == "__main__":
    builder = ConanMultiPackager()
    builder.add({"arch": "x86", "build_type": "Release"}, {"configuration": "Release No NetMon"})
    builder.add({"arch": "x86", "build_type": "Debug"}, {"configuration": "Debug No NetMon"})
    builder.add({"arch": "x86", "build_type": "Release"}, {"configuration": "Release No NetMon and AirPcap"})
    builder.add({"arch": "x86", "build_type": "Debug"}, {"configuration": "Debug No NetMon and AirPcap"})
    builder.add({"arch": "x86_64", "build_type": "Release"}, {"configuration": "Release No NetMon"})
    builder.add({"arch": "x86_64", "build_type": "Debug"}, {"configuration": "Debug No NetMon"})
    builder.add({"arch": "x86_64", "build_type": "Release"}, {"configuration": "Release No NetMon and AirPcap"})
    builder.add({"arch": "x86_64", "build_type": "Debug"}, {"configuration": "Debug No NetMon and AirPcap"})
    builder.run()
