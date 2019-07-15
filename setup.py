import setuptools

from setuptools.command.install import install

# https://blog.niteo.co/setuptools-run-custom-code-in-setup-py/
class CustomInstallCommand(install):
    def run(self):
        print("Hello, developer, how are you? :)")
        install.run(self)


with open('requirements.txt') as f:
    requirements = f.read().splitlines()

long_description_md = """
polaroidme is a simple to use command-line-tool for placing an image into a
Polaroid-like frame. It offers basic features like scaling and/or cropping,
using any (ttf-)font, supports high-res outpu and gets the job just done
well. It is actively maintained & developed (2019). To see if it fits your needs
take a look at the project's github-repo and check out the examples.

Feel free to report bugs, submit featurerequest or contribute!
"""

setuptools.setup(
     name='polaroidme',
     version='0.9.0',
     scripts=['polaroidme/polaroidme'] ,
     author="Sven Hessenmüller",
     author_email="sven.hessenmueller@gmail.com",
     description="converts an image into vintage polaroid style",
     include_package_data=True,
     long_description=long_description_md,
     url="https://github.com/s3h10r/polaroidme",
     packages=setuptools.find_packages(),
     install_requires=requirements,
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
     cmdclass={
        'install': CustomInstallCommand,
     },
)
