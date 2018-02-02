# conan-mili

![conan-mili image](/images/conan-mili.png)

[![Download](https://api.bintray.com/packages/conan-community/conan/mili%3Aconan/images/download.svg?version=5.13.0%3Astable)](https://bintray.com/conan-community/conan/mili%3Aconan/5.13.0%3Astable/link)
[![Build Status](https://travis-ci.org/danimtb/conan-mili.svg?branch=stable%2F5.13.0)](https://travis-ci.org/danimtb/conan-mili)

[Conan.io](https://conan.io) package for [MiLi](https://bitbucket.org/fudepan/mili/overview) project.

The packages generated with this *conanfile.py* can be found in [Bintray](https://bintray.com/conan-community/conan/mili%3Aconan).

## Basic setup

    $ conan install mili/17@conan/stable

## Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*:

    [requires]
    mili/17@conan/stable

    [generators]
    txt
    cmake

## License

[MIT License](LICENSE)