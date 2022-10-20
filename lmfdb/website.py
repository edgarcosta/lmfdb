# -*- coding: utf-8 -*-
# LMFDB - L-function and Modular Forms Database web-site - www.lmfdb.org
# Copyright (C) 2010-2012 by the LMFDB authors
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Library General Public
# License as published by the Free Software Foundation; either
# version 2 of the License, or (at your option) any later version.
"""
start this via $ sage -python website.py --port <portnumber>
add --debug if you are developing (auto-restart, full stacktrace in browser, ...)
"""

from .lmfdb_database import db
from .homepage import random
from . import maass_forms
from .groups import glnC
from .groups import glnQ
from .groups import abstract
from . import groups
from . import cluster_pictures
from . import hecke_algebras
from . import rep_galois_modl
from . import modlmf
from .abvar import fq
from . import abvar
from . import higher_genus_w_automorphisms
from . import lattice
from . import riemann
from . import motives
from . import hypergm
from . import permutations
from . import crystals
from . import zeros
from . import tensor_products
from . import artin_representations
from . import galois_groups
from . import local_fields
from . import characters
from . import knowledge
from . import users
from . import sato_tate_groups
from . import genus2_curves
from . import lfunctions
from . import number_fields
from . import ecnf
from . import elliptic_curves
from . import siegel_modular_forms
from . import half_integral_weight_forms
from . import hilbert_modular_forms
from . import bianchi_modular_forms
from . import belyi
import os
# Needs to be done first so that other modules and gunicorn can use logging
from .logger import info
from .app import app, set_running  # So that we can set it running below

# Importing the following top-level modules adds blueprints
# to the app and imports further modules to make them functional
# Note that this necessarily includes everything, even code in still in an
# alpha state
from . import api
assert api
#from . import api2
#assert api2
assert belyi
assert bianchi_modular_forms
assert hilbert_modular_forms
assert half_integral_weight_forms
assert siegel_modular_forms
# from . import modular_forms
# assert modular_forms
assert elliptic_curves
assert ecnf
assert number_fields
assert lfunctions
assert genus2_curves
assert sato_tate_groups
assert users
assert knowledge
assert characters
assert local_fields
assert galois_groups
assert artin_representations
assert tensor_products
assert zeros
assert crystals
assert permutations
assert hypergm
assert motives
assert riemann
assert lattice
assert higher_genus_w_automorphisms
assert abvar
assert fq
assert modlmf
assert rep_galois_modl
assert hecke_algebras
assert cluster_pictures
assert groups
assert abstract
assert glnQ
assert glnC
assert maass_forms
assert random

if db.is_verifying:
    raise RuntimeError(
        "Cannot start website while verifying (SQL injection vulnerabilities)")


def main():
    info("main: ...done.")
    from .utils.config import Configuration

    flask_options = Configuration().get_flask()
    flask_options['threaded'] = False

    if "profiler" in flask_options and flask_options["profiler"]:
        info("Profiling!")
        from werkzeug.middleware.profiler import ProfilerMiddleware

        app.wsgi_app = ProfilerMiddleware(
            app.wsgi_app, restrictions=[30], sort_by=(
                "cumulative", "time", "calls"))
        del flask_options["profiler"]

    if "COCALC_PROJECT_ID" in os.environ:
        from .utils.cocalcwrap import CocalcWrap
        # we must accept external connections
        flask_options["host"] = "0.0.0.0"
        app.wsgi_app = CocalcWrap(app.wsgi_app)
        stars = "\n" + "*" * 80
        info(stars +
             "\n\033[1mCocalc\033[0m environment detected!\n" +
             "Visit" +
             "\n  \033[1m https://cocalc.com" +
             app.wsgi_app.app_root +
             " \033[0m" +
             "\nto access this LMFDB instance" +
             stars
             )

    set_running()
    app.run(**flask_options)
