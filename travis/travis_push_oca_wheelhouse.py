#!/usr/bin/env python

# setuptools-odoo-make-default -d .
# for each setup/addon
#    cd setup/addon
#    rm -fr build dist '*.egg-info'
#    python setup.py bdist_wheel
#    scp dist/*.whl wheelhouse.odoo-community.org:/var/www/wheelhouse/oca
