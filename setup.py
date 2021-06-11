#!/usr/bin/env python
"""
MultiQC plugin to display custom pictures
"""

from setuptools import setup, find_packages

version = '0.1'

setup(
    name = 'custom_images',
    version = version,
    author = 'Cervin Guyomar',
    author_email = 'cervin.guyomar@inrae.fr',
    description = "",
    long_description = __doc__,
    keywords = 'bioinformatics',
    url = '',
    download_url = '',
    license = '',
    packages = find_packages(),
    include_package_data = True,
    install_requires = [
        'multiqc'
    ],
    entry_points = {
        'multiqc.modules.v1': [
            'custom_images = custom_images_mqc_plugin.modules.custom_images:MultiqcModule',
        ],
        'multiqc.hooks.v1': [
            'execution_start = custom_images_mqc_plugin.custom_code:custom_images_mqc_plugin_execution_start'
        ]
    },
    classifiers = [
    ],
)
