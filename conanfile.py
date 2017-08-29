from conans import ConanFile, tools, os


class NpcapDllConan(ConanFile):
    name = "npcap-dll"
    version = "0.93"
    license = "NPCAP License"
    url = "https://github.com/bincrafters/conan-npcap"
    source_url = "https://github.com/nmap/npcap"
    settings = "arch", "compiler", "build_type"
    options = {
        "configuration": 
            [
                "OEM Release No NetMon and AirPcap(WinPcap Mode)",
                "Debug No NetMon and AirPcap(WinPcap Mode)",
                "Release No NetMon and AirPcap(WinPcap Mode)",
                "Release No NetMon LOG_TO_FILE",
                "OEM Release No NetMon and AirPcap",
                "Debug",
                "Release",
                "Debug No NetMon and AirPcap",
                "Release LOG_TO_FILE",
                "Debug No NetMon",
                "Release No NetMon",
                "Release No NetMon and AirPcap"
            ] 
    }

    default_options = "configuration=OEM Release No NetMon and AirPcap(WinPcap Mode)"
    lib_short_name = "npcap"

    def source(self):
        tools.get("{0}/archive/v{1}.zip".format(self.source_url, self.version))

    def build(self):
        #vcvars_2013 = r'"C:\Program Files (x86)\Microsoft Visual Studio 12.0\VC\vcvarsall.bat"'
        vcvars = tools.vcvars_command(self.settings)
        self.run(vcvars)
        unzip_dir = "{0}-{1}".format(self.lib_short_name, self.version)
        sln_file = "Packet.sln"
        sln_path = os.path.join(unzip_dir, "packetWin7", "Dll", "Project", sln_file)
        build_command = tools.msvc_build_command(self.settings, sln_path,  targets=["Build"])
        final_build_command = build_command.replace("Release", '"{0}"'.format(str(self.options.configuration)))
        print(final_build_command)
        self.run(final_build_command)

    def package(self):
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["npcap"]
        self.cpp_info.libs = self.collect_libs()
