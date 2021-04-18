# -*- coding: utf-8 -*-
# Part of swerp. See LICENSE file for full copyright and licensing details.

""" Addons module.

This module serves to contain all swerp addons, across all configured addons
paths. For the code to manage those addons, see swerp.modules.

Addons are made available under `swerp.addons` after
swerp.tools.config.parse_config() is called (so that the addons paths are
known).

This module also conveniently reexports some symbols from swerp.modules.
Importing them from here is deprecated.

"""
# make swerp.addons a namespace package, while keeping this __init__.py
# present, for python 2 compatibility
# https://packaging.python.org/guides/packaging-namespace-packages/
__path__ = __import__('pkgutil').extend_path(__path__, __name__)
