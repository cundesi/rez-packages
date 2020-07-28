#!/usr/bin/env python

import os
import sys

root = os.path.dirname(__file__)
pythonpath = os.path.join(root, "python")
sys.path.insert(0, pythonpath)

from build_utils import _rezbuild
_rezbuild.main([root])
