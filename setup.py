from setuptools import setup, find_packages

setup(
    name='music_metrics',
    version='0.1',
    author='Michał Kopeć and Wiktor Pytlewski',
    author_email='wiktor.pytlewski.stud@pw.edu.pl or michal.kopec6.stud@pw.edu.pl',
    description='Comprehensive library aggregating standard and custom music metrics for insightful music analysis',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://gitlab-stud.elka.pw.edu.pl/wpytlew1/zprp-projekt-zespol-16',
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
    python_requires='>=3.10',
)
