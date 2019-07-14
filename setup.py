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
I guess everyone and his/her grandmother already wrote a script to
convert an image into a "Polaroid-style"? polaroidme provides basic feature
(scaling and/or cropping, font of your choice, high-res output) and gets the job done
well. It is actively maintained & developed (2019). To see if it fits your needs
take a look at the project's github-repo for some example output.

Please feel free to report bugs, submit featurerequest or contribute!
"""

setuptools.setup(
     name='polaroidme',
     version='0.8.7',
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
