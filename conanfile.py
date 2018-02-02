from conans import ConanFile, CMake, tools
import os


class MiliConan(ConanFile):
    name = "mili"
    version = "17"
    license = "Boost Software License"
    url = "https://bitbucket.org/fudepan/mili"
    description = ("MiLi is a collection of useful C++ libraries, composed only by headers. "
                   "No installation, no makefile, no complications: just KISS. "
                   "Simple solutions for simple problems.")
    no_copy_source = True
    exports_sources = ["LICENSE"]

    def source(self):
        download_url = ("https://storage.googleapis.com/google-code-archive-downloads/v2/"
                        "code.google.com/%s/%s-%s.tgz" % (self.name, self.name, self.version))
        tools.get(download_url)
        os.rename("mili", "sources")

    def package(self):
        self.copy("*LICENSE*.txt", dst="licenses", src="sources")
        self.copy("*mili*.h", dst="include", src="sources")
        self.copy("*mili*.hpp", dst="include", src="sources")
