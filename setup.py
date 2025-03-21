from setuptools import setup, find_packages

setup(
    name="mutationtracker",
    version="1.0.1",
    packages=find_packages(),
    install_requires=[],
    author="Jaime Derrez",
    author_email="mail@redmanlabs.nl",
    description="Saving users from debug-hell by conveniently keeping track of mutations in objects and logging them",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/RedmanLabs/mutationtracker",
    keywords=[
        "mutation tracked object",
        "mutationtrackedobject",
        "mutation",
        "mutations",
        "mutation tracker",
        "object tracker",
        "object mutations",
        "changelog",
        "change tracker",
        "object changes",
        "observer pattern",
        "object observer",
        "change observer",
        "mutation observer",
        "log changes",
        "mutation log",
        "log mutations",
        "trace change",
        "attribute value",
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Topic :: Software Development :: Libraries",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
