from setuptools import setup, find_packages

setup(
    name="my_custom_tools", # имя пакета, как оно будет отображаться в PyPI
    version="0.1.0", # версия пакета
    author="Усюгова 2.273",
    author_email="my_email@gmail.com",
    description="Мой первый пользовательский пакет с утилитами",
    packages=find_packages(), # автоматически находит все пакеты
    python_requires=">=3.6", # минимальная требуемая версия Python
)
