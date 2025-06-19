from setuptools import setup, find_packages

setup(
    name='mkproject',
    version='0.1',
    packages=find_packages(),
    install_requires=['click'],
    entry_points={
        'console_scripts': [
            'mkproject = mkproject.cli:cli',
        ],
    },
    author='LM',
    description='Ferramenta CLI para criar estrutura base de projetos Data Science',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
