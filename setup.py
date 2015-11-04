# -*- coding: utf-8 -*-
import sys
from setuptools import find_packages, setup


# keep this package private
if set(sys.argv).intersection(['upload', 'register']):
	print('This setup is private and should not be uploaded or registered.')
	sys.exit(-1)


# package settings
setup(
	# info
	name='django-jselog',
	version='0.0.1',
	author=u'Stephen Quebe',
	author_email='squebe@gmail.com',
	url='https://github.com/squebe/django-jselog',
	description='Jselog is a simple Django app that helps log client side javascript errors on the server.',
	long_description=open('README.md').read(),
	license='MIT',

	# include
	packages=find_packages(),
	include_package_data=True,
	install_requires=[],

	# keep this package private
	classifiers=['Private :: Do Not Upload'],
)