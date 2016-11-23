#!/usr/bin/env python
# -*- coding: utf-8 -*-

from harpia.GUI.fieldtypes import *
from harpia.plugins.C.openCV.opencvplugin import OpenCVPlugin


class Not(OpenCVPlugin):

    # -------------------------------------------------------------------------
    def __init__(self):
        OpenCVPlugin.__init__(self)

        # Appearance
        self.help = "Realiza a negação lógica de uma imagem. " + \
            "Corresponde à negativa da imagem."
        self.label = "Not"
        self.icon = "images/not.png"
        self.color = "10:180:10:150"
        self.in_types = ["HRP_IMAGE"]
        self.out_types = ["HRP_IMAGE"]
        self.group = "Arithmetic and logical operations"

        # -------------------C/OpenCv code------------------------------------
        self.function_call = \
            'if(block$id$_img_i0){\n' + \
            'block$id$_img_o0 = cvCloneImage(block$id$_img_i0);\n' + \
            'cvNot(block$id$_img_i0, block$id$_img_o0);\n' + \
            '}\n'

# -----------------------------------------------------------------------------
