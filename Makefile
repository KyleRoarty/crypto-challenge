pycrypto := venv/lib/python3.5/site-packages/Crypto/

.PHONY: work

work: $(pycrypto)

venv:
		python3 -m venv venv; . venv/bin/activate; pip install --upgrade pip

$(pycrypto): venv
		. venv/bin/activate; pip install pycrypto
