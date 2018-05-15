import os
from conans import ConanFile, tools


class MiliConan(ConanFile):
    name = "mili"
    version = "17"
    license = "BSL-1.0"
    url = "https://github.com/conan-community/conan-mili/"
    homepage = "https://bitbucket.org/fudepan/mili"
    description = "A set of minimal libraries composed only by 1 header file each."
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
