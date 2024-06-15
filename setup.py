from setuptools import setup, find_packages

setup(
    name='groqy',
    version='0.1.0',
    description='A command-line interface (CLI) tool for interacting with AI language models using the Groq API',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/MemeFormer/Groqy',
    packages=find_packages(),
    install_requires=[
        'requests',
        'rich',
        'inquirer',
        'halo',
        'python-dotenv',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    entry_points={
        'console_scripts': [
            'groqy=groqy.__main__:main',
        ],
    },
)