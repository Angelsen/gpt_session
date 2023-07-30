from setuptools import setup, find_packages

setup(
    name="GPT-Session",
    version="0.1",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "guide-session = gpt_session.terminal_handler:main",
        ],
    },

    install_requires=[
        "openai",
        "python-dotenv"

    ],
)