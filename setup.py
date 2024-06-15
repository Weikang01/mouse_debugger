from setuptools import setup, find_packages

# Read the requirements from the requirements.txt file
with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="MouseDebugApp",
    version="0.1",
    description="A Tkinter application to monitor mouse status and provide real-time debugging information",
    author="Weikang Liu",
    author_email="wliu.contact@gmail.com",  # Replace with your email
    url="https://github.com/Weikang01",  # Replace with your GitHub URL
    packages=find_packages(),
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'mousestatusapp = mousestatusapp:main',  # Replace with your module and main function
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
