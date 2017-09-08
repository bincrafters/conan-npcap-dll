from conans import ConanFile, tools, os


class NpcapDllConan(ConanFile):
    name = "npcap-dll"
    version = "0.93"
    license = "NPCAP License"
    url = "https://github.com/bincrafters/conan-npcap"
    source_url = "https://github.com/nmap/npcap"
    settings = "arch", "compiler", "build_type"
    lib_parent_name = "npcap"
    sln_path = os.path.join("packetWin7", "Dll", "Project", "Packet.sln")
    default_options = "configuration=Release No NetMon and AirPcap"
    options = {
        "configuration": 
            [
                "Release",
                "Debug",
                "Release No NetMon",
                "Debug No NetMon",
                "Release No NetMon and AirPcap",
                "Debug No NetMon and AirPcap",
                "Release No NetMon and AirPcap(WinPcap Mode)",
                "Debug No NetMon and AirPcap(WinPcap Mode)",
                "Release LOG_TO_FILE",
                "Release No NetMon LOG_TO_FILE",
                "OEM Release No NetMon and AirPcap",
                "OEM Release No NetMon and AirPcap(WinPcap Mode)"
            ] 
    }

    def source(self):
        tools.get("{0}/archive/v{1}.zip".format(self.source_url, self.version))

    def build(self):
        vcvars = tools.vcvars_command(self.settings)
        print("vcvars = " + vcvars)
        self.run(vcvars)
        unzip_dir = "{0}-{1}".format(self.lib_parent_name, self.version)
        sln_path_full = os.path.join(unzip_dir, self.sln_path)
        print("sln_path_full = " + sln_path_full)

        print("sln_path_full exists? " + os.path.isfile(fname))

        build_command = tools.msvc_build_command(
            self.settings, 
            sln_path_full,  
            targets=["Build"], 
            upgrade_project=False,
            build_type=str('"' + str(self.options.configuration) + '"'))

        print(" build_command = " + build_command)

        if self.settings.arch == "x86":
            self.run(build_command.replace('"x86"', '"Win32"'))
        else:
            self.run(build_command)
        
    def package(self):
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = self.collect_libs()
