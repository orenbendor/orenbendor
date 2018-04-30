from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(
    name='pylabcontrol',
    version='0.1.0',
    package_dir={'pylabcontrol': ''},
    packages=['pylabcontrol'],
    url='https://github.com/LISE-B26/pylabcontrol',
    license='GPL',
    author='Arthur Safira, Jan Gieseler, and Aaron Kabcenell',
    author_email='',
    long_description=readme(),
    description='Python Laboratory Control Software',
    keywords='laboratory control',
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Development Status :: 4 - Beta',
        'Environment :: Win32 (MS Windows)',
        'Intended Audience :: Science/R]',
        ],
    install_requires=[
        'matplotlib',
        'pandas',
        'numpy',
        'scipy'
    ],
    test_suite='nose.collector',
    tests_require=['nose'],
    entry_points={
        'console_scripts': ['launch_pylabcontrol = pylabcontrol.src.gui.run_gui:run_gui']
    }
)
