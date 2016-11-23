#!/usr/bin/env python
# -*- coding: utf-8 -*-

from harpia.GUI.fieldtypes import *
from harpia.plugins.C.openCV.opencvplugin import OpenCVPlugin


class NewDouble(OpenCVPlugin):

    # -------------------------------------------------------------------------
    def __init__(self):
        OpenCVPlugin.__init__(self)
        self.doubleVal = 1

        # Appearance
        self.help = "Creates new literal value (Double)."
        self.label = "New Double"
        self.icon = "images/newDouble.png"
        self.color = "50:50:200:150"
        self.out_types = ["HRP_DOUBLE"]
        self.group = "Basic Data Type"

        self.properties = {
            "doubleVal": {
                "name": "Value",
                "type": HARPIA_FLOAT,
                "lower": 0,
                "upper": 65535,
                "step": 1
            }
        }

        # -------------------C/OpenCv code------------------------------------
        self.vars = 'double block$id$_double_o0 = ' + \
            '$doubleVal$; // New Double Out\n'

# -----------------------------------------------------------------------------
