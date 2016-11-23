#!/usr/bin/env python
# -*- coding: utf-8 -*-

from harpia.GUI.fieldtypes import *
from harpia.plugins.javascript.webaudio.webaudioplugin import WebaudioPlugin


class Button(WebaudioPlugin):

    # -------------------------------------------------------------------------
    def __init__(self):
        WebaudioPlugin.__init__(self)
        self.value = 1
        self.label = "Label"

        # Appearance
        self.help = "Button"
        self.label = "Button"
        self.icon = "images/show.png"
        self.color = "50:150:250:150"
        self.out_types = ["HRP_WEBAUDIO_FLOAT"]
        self.group = "Interface"

        self.vars = """
// block_$id$ = Button
var block_$id$_value = $value$;
var block_$id$_o0 = [];
"""

        self.function_call = """
function click_$id$(){
    value = document.getElementById("block_$id$").value;
    for (var i = 0; i < block_$id$_o0.length ; i++){
        block_$id$_o0[i](value);
    }
};
"""

        self.dealloc = """
<button type="button" value="$value$" onClick="click_$id$();"
id="block_$id$">$label$</button><br>
"""

        self.properties = {"value": {"name": "Value",
                                     "type": HARPIA_FLOAT,
                                     "lower": 0,
                                     "upper": 20000,
                                     "step": 1
                                     },
                           "label": {"name": "Label",
                                     "type": HARPIA_STRING
                                     }
                           }
