.PHONY: clean virtualenv test  dist venv-install

clean:
	find . -name '*.py[co]' -delete
	find . -name '*.db' -delete

virtualenv:
	python -m venv venv
	venv/bin/pip install -r requirements-dev.txt
	venv/bin/python setup.py develop
	@echo
	@echo "VirtualENV Setup Complete. Now run: source venv/bin/activate"
	@echo

test:
	python -m pytest \
		-v \
		--cov=restaurant \
		--cov-report=term \
		--cov-report=html:coverage-report \
		tests/

venv-install:  dist
	if test -z "$$VIRTUAL_ENV"; \
	then \
  		echo; \
  		echo "Please run this command in a virtual environment."; \
  		echo "See README.md"; \
  		echo; \
  	else \
  	  pip uninstall restaurant;  \
  	  pip install dist/*.whl; \
  	fi

dist: clean
	rm -rf dist/*
	python setup.py sdist
	python setup.py bdist_wheel
