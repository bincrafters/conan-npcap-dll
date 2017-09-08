from conan.packager import ConanMultiPackager


if __name__ == "__main__":
    builder = ConanMultiPackager()
    builder.add_common_builds()
    
    for settings, options, env_vars, build_requires in builder.builds:
        if settings["arch"] == "x86":
             settings.arch = "Win32"
    builder.run()
