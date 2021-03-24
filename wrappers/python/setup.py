from setuptools import setup, find_packages
from setuptools.dist import Distribution

# _version.py should be generated by running find_librs_version.py and copied to pyrealsense2 folder
from pyrealsense2._version import __version__

import os
import io

package_name = "pyrealsense2"
package_data = {}

print("version = ", __version__)

def load_readme():
     with io.open('README.rst', encoding="utf-8") as f:
        return f.read()

if os.name == 'posix':
    package_data[package_name] = ['*.so']
else:
    package_data[package_name] = ['*.pyd', '*.dll']


# This creates a list which is empty but returns a length of 1.
# Should make the wheel a binary distribution and platlib compliant.
class EmptyListWithLength(list):
    def __len__(self):
        return 1


setup(
    name=package_name,
    version=__version__,
    author='Intel(R) RealSense(TM)',
    author_email='realsense@intel.com',
    url='https://github.com/IntelRealSense/librealsense',
    scripts=['examples/align-depth2color.py',
            'examples/export_ply_example.py',
            'examples/opencv_viewer_example.py',
            'examples/python-rs400-advanced-mode-example.py',
            'examples/python-tutorial-1-depth.py'
    ],
    license='Apache License, Version 2.0',
    description='Python Wrapper for Intel Realsense SDK 2.0.',
    long_description=load_readme(),
    install_requires=[],
          classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Multimedia :: Video',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Human Machine Interfaces',
        'Topic :: Scientific/Engineering :: Image Recognition',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries :: Application Frameworks'
        ],
    packages=find_packages(exclude=['third_party', 'docs', 'examples']),
    include_package_data=True,
    ext_modules=EmptyListWithLength(),
    package_data=package_data
)
