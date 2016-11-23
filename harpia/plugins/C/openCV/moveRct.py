#!/usr/bin/env python
# -*- coding: utf-8 -*-

from harpia.GUI.fieldtypes import *
from harpia.plugins.C.openCV.opencvplugin import OpenCVPlugin


class MoveRct(OpenCVPlugin):

    # -------------------------------------------------------------------------
    def __init__(self):
        OpenCVPlugin.__init__(self)
        self.offset_x = 0
        self.offset_y = 0

        # Appearance
        self.help = "Move Rectangle`s (0,0) point to input point"
        self.label = "Move Rectangle"
        self.icon = "images/moveRct.png"
        self.color = "50:50:200:150"
        self.in_types = ["HRP_RECT", "HRP_POINT"]
        self.out_types = ["HRP_RECT"]
        self.group = "Experimental"

        self.properties = {
            "offset_x": {
                "name": "Offset x",
                "type": HARPIA_INT,
                "lower": 0,
                "upper": 65535,
                "step": 1
            },
            "offset_y": {
                "name": "Offset Y",
                "type": HARPIA_INT,
                "lower": 0,
                "upper": 65535,
                "step": 1
            }
        }
        # --------------------C/OpenCv code--------------------------------
        self.vars = \
            'CvRect block$id$_rect_i0;\n' + \
            'CvPoint block$id$_point_i1;\n' + \
            'CvRect block$id$_rect_o0;\n'

        self.function_call = \
            'block$id$_rect_o0 = block$id$_rect_i0;\n' + \
            'block$id$_rect_o0.x = block$id$_point_i1.x + $offset_x$;\n' + \
            'block$id$_rect_o0.y = block$id$_point_i1.y + $offset_y$;\n'

# ------------------------------------------------------------------------------
