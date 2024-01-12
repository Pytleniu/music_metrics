from setuptools import setup, find_packages

setup(
    name='music_metrics',
    version='0.1',
    author='Your Name',
    author_email='your.email@example.com',
    description='A brief description of your project',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/music_metrics',
    packages=find_packages(include=['music_metrics', 'music_metrics.*']),
    install_requires=[
        'muspy',
        'pypianoroll',
        'pretty_midi',
        'prettytable',
        'matplotlib',
        'numpy'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
