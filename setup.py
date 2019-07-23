import setuptools

from setuptools.command.install import install

# https://blog.niteo.co/setuptools-run-custom-code-in-setup-py/
class CustomInstallCommand(install):
    def run(self):
        print("Hello, how are you? :)")
        install.run(self)

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

long_description_md = """
polaroidme - vintage polaroid style + generative art
====================================================

polaroidme is a simple command-line-tool & python-library for placing an image
into a Polaroid-like frame and optionally put a title / description or meta infos
out of EXIF-data on the bottom. The default font mimics scribbled handwriting
but any (ttf-)font which suits your taste is supported. The tool offers basic
features like auto-scaling up-/downwards and/or cropping, using any (ttf-)font,
supports high-res output and gets it's job done well.

Starting as `a script for making high-res contactsheets which make the beholder's eyes not bleed <https://github.com/s3h10r/fokus>`_ recently polaroidme gets phonky by providing:

* generative-art-"generators" which are fun to play with
* chainable filters (`--filter f1,f2,...,fN`)
* reading EXIF-data
* lightweight plugin-framework - makes it simple to use (and write) additional filters & generators
* support for templates
* `--help`-option :)

The author's main usecase for polaroidme is doing minimalistic artworks in
printing quality with it - and learning and mixing fun to use technologies
full-stack around it (raspi, webapis, flutter). :D

To see if it could be usefull for your needs take a look at the project's
github-repo and check out the `examples`_

polaroidme is actively maintained & developed (2019).

Contributions are welcome, and they are greatly appreciated!

Please feel free to send pull-requests an use the `issue tracker <https://github.com/s3h10r/polaroidme/issues>`_.

Have fun!

_`examples`: https://github.com/s3h10r/polaroidme/blob/master/README.md
"""

setuptools.setup(
     name='polaroidme',
     version='0.9.39',
     scripts=['cli/polaroidme', 'cli/pom','cli/contactsheet'] ,
     author="Sven Hessenmüller",
     author_email="sven.hessenmueller@gmail.com",
     description="converts an image into vintage polaroid style - and can do some phonky stuff. :D",
     include_package_data=True,
     long_description=long_description_md,
     url="https://github.com/s3h10r/polaroidme",
     packages=setuptools.find_packages(),
     install_requires=requirements,
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
         "Development Status :: 4 - Beta",
         "Environment :: Console",
         "Topic :: Multimedia :: Graphics",
         "Topic :: Utilities",
     ],
     cmdclass={
        'install': CustomInstallCommand,
     },
)
