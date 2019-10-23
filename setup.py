import setuptools

with open("README.rst", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="calendar-view",
    version="1.0.0",
    author="Oleksandr Sakhnevych",
    author_email="o.sakhnevych@gmail.com",
    description="Library provides a graphical view of the calendar.",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://github.com/sakhnevych/CalendarView",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
