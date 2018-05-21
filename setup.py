from distutils.core import setup

setup(
    name='pigg',
    version='0.1',
    description='a machine learning api frame',
    author='zcfrank1st',
    author_email='zhchaos@gmail.com',
    url='https://github.com/zcfrank1st/piggy',
    py_modules=['pigg'],
    packages=['frame', 'serv'],

    install_requires=(
       'tornado==4.5.3',
    ),
)