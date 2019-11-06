from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

setup(
    name='markdown-captions',
    version='2',
    description= 'Turn markdown images into captioned images using <figure>',
    url='https://github.com/evidlo/markdown-captions',
    author='evidlo',
    author_email='evan@evanw.org',
    license='GPL3',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=['markdown_captions'],
    keywords="markdown figures captions subtitles",
    install_requires=['Markdown>=3.0.1'],
    classifiers=[
        'Development Status :: 4 - Beta', 'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent', 'Programming Language :: Python',
        'Topic :: Text Processing :: Markup :: HTML'
    ])
