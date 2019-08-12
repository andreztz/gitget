
release: 
	python setup.py sdist bdist_wheel
	twine upload --repository-url https://upload.pypi.org/legacy/ dist/*

release-test:
	python setup.py sdist bdist_wheel
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*