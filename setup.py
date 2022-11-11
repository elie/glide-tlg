#!/usr/bin/env python


from setuptools import setup

setup(
    name='Glide tlg',
    version='1.5.0',
    description='tlg themes for Glide.',
    author='Joel Burton',
    author_email='joel@joelburton.com',
    url='https://github.com/elie/glide-tlg',
    packages=['glide_tlg'],
    install_requires=["glide"],
    include_package_data=True,
    entry_points={
        'sphinx.html_themes': [
            'revealjs-tlg = glide_tlg',
            'handouts-tlg = glide_tlg',
        ],
    },
)
