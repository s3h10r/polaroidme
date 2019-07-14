# https://dzone.com/articles/executable-package-pip-install
import setuptools
long_description_md = ""
setuptools.setup(
     name='polaroidme',
     version='0.8.4',
     scripts=['polaroidme'] ,
     author="Sven Hessenmüller",
     author_email="sven.hessenmueller@gmail.com",
     description="converts an image into vintage polaroid style",
     long_description=long_description_md,
     long_description_content_type="text/markdown",
     url="https://github.com/s3h10r/polaroidme",
     packages=setuptools.find_packages('Pillow'),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],

)
