from setuptools import setup, find_packages

setup(
    name="formfiller",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "click",
        "openai",
        "python-dotenv",
        "PyPDF2",
        "reportlab"
    ],
    entry_points={
        "console_scripts": [
            "formfiller=formfiller.cli:main"
        ]
    },
    author="Kelly Chen",
    description="A GPT-powered CLI tool that fills out forms using your resume and a job description.",
    long_description=open("README.md").read() if open("README.md", "r").readable() else "",
    long_description_content_type="text/markdown",
    python_requires=">=3.7"
)
