#!/usr/bin/env python
# -*- coding: utf-8 -*-

from harpia.GUI.fieldtypes import *
from harpia.plugins.C.openCV.opencvplugin import OpenCVPlugin


class Sobel(OpenCVPlugin):

    # -------------------------------------------------------------------------
    def __init__(self):
        OpenCVPlugin.__init__(self)
        self.masksize = 3
        self.xorder = 1
        self.yorder = 1

        # Appearance
        self.help = "Operação de filtragem que utiliza uma máscara " + \
            "Sobel para realçar cantos e bordas da imagem."
        self.label = "Sobel"
        self.icon = "images/sobel.png"
        self.color = "250:180:80:150"
        self.in_types = ["HRP_IMAGE"]
        self.out_types = ["HRP_IMAGE"]
        self.group = "Gradients, Edges and Corners"

        self.properties = {
            "xorder": {
                "name": "X Axis Derivate Order",
                "type": HARPIA_INT,
                "lower": 0,
                "upper": 6,
                "step": 1
            },
            "yorder": {
                "name": "Y Axis Derivate Order",
                "type": HARPIA_INT,
                "lower": 0,
                "upper": 6,
                "step": 1
            },
            "masksize": {
                "name": "Mask Size",
                "type": HARPIA_INT,
                "lower": 1,
                "upper": 7,
                "step": 2
            }
        }

        # -------------------C/OpenCv code------------------------------------
        self.vars = \
            'IplImage * block$id$_img_i0 = NULL;\n' + \
            'IplImage * block$id$_img_o0 = NULL;\n' + \
            'IplImage * block$id$_img_t = NULL;\n'

        self.function_call = \
            '\nif(block$id$_img_i0){\n' + \
            'CvSize size$id$ = cvGetSize(block$id$_img_i0);\n' + \
            'block$id$_img_o0 = cvCreateImage(size$id$, ' + \
            'IPL_DEPTH_32F,block$id$_img_i0->nChannels);\n' + \
            'cvSobel(block$id$_img_i0, block$id$_img_o0, ' + \
            '$xorder$, $yorder$, $masksize$);\n' + \
            '}\n'

        self.dealloc = \
            'cvReleaseImage(&block$id$_img_o0);\n' + \
            'cvReleaseImage(&block$id$_img_i0);\n' + \
            'cvReleaseImage(&block$id$_img_t);\n'

# -----------------------------------------------------------------------------
