# -*- coding: utf-8 -*-
# [HARPIA PROJECT]
#
#
# S2i - Intelligent Industrial Systems
# DAS - Automation and Systems Department
# UFSC - Federal University of Santa Catarina
# Copyright: 2006 - 2007 Luis Carlos Dill Junges (lcdjunges@yahoo.com.br),
#                        Clovis Peruchi Scotti (scotti@ieee.org),
#                        Guilherme Augusto Rutzen (rutzen@das.ufsc.br),
#                        Mathias Erdtmann (erdtmann@gmail.com)
#                        and S2i (www.s2i.das.ufsc.br)
#            2007 - 2009 Clovis Peruchi Scotti (scotti@ieee.org),
#                        S2i (www.s2i.das.ufsc.br)
#
#
#    This program is free software: you can redistribute it and/or modify it
#    under the terms of the GNU General Public License version 3, as published
#    by the Free Software Foundation.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranties of
#    MERCHANTABILITY, SATISFACTORY QUALITY, or FITNESS FOR A PARTICULAR
#    PURPOSE.  See the GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License along
#    with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#    For further information, check the COPYING file distributed with this
#    software.

import os
import sys
import copy
import inspect  # For module inspect
import pkgutil  # For dynamic package load
import harpia.plugins
from glob import glob  # To load examples
from harpia.control.preferencescontrol import PreferencesControl
from harpia.model.preferences import Preferences


class System(object):

    APP = 'harpia'
    DIR = '/usr/share/harpia/po'

    ZOOM_ORIGINAL = 1
    ZOOM_IN = 2
    ZOOM_OUT = 3

    VERSION = "0.0.1"

    # ----------------------------------------------------------------------
    # An inner class instance to be singleton
    # ----------------------------------------------------------------------
    class __Singleton:
        # ----------------------------------------------------------------------

        def __init__(self):
            os.environ['HARPIA_DATA_DIR'] = "/usr/share/harpia/"
            self.Log = None
            self.properties = Preferences()
            self.generators = {}
            self.blocks = {}
            self.list_of_examples = []
            self.connectors = {}
            self.__load()

        # ----------------------------------------------------------------------
        def __load(self):
            self.__load_blocks()
            examples = glob(os.environ['HARPIA_DATA_DIR'] + "examples/*")
            for example in examples:
                self.list_of_examples.append(example)
            self.list_of_examples.sort()
            PreferencesControl(self.properties).load()

        # ----------------------------------------------------------------------
        def __load_blocks(self):
            from harpia.control.codegenerator import CodeGenerator
            from harpia.model.plugin import Plugin
            for importer, modname, ispkg in pkgutil.walk_packages(
                    harpia.plugins.__path__,
                    harpia.plugins.__name__ + ".",
                    None):
                if ispkg:
                    continue
                module = __import__(modname, fromlist="dummy")
                for name, obj in inspect.getmembers(module):
                    if not inspect.isclass(obj):
                        continue
                    instance = obj()
                    if isinstance(instance, Plugin) and \
                            instance.get_label() != "":
                        obj_type = instance.type
                        language = obj_type.split(".")[2]
                        framework = obj_type.split(".")[3]
                        # Adding a property do class dinamically
                        obj.language = language
                        obj.framework = framework
                        self.blocks[obj_type] = obj
                    if isinstance(instance, CodeGenerator):
                        language = instance.__class__.__module__.split(".")[2]
                        self.generators[language] = obj
                        self.connectors.update(instance.connectors)

    # Instance variable to the singleton
    instance = None

    # ----------------------------------------------------------------------
    def __init__(self):
        if not System.instance:
            System.instance = System.__Singleton()

    # ----------------------------------------------------------------------
    def __new__(cls):  # __new__ always a classmethod
        if System.instance is None:
            System.instance = System.__Singleton()
            # Add properties dynamically
            cls.properties = System.instance.properties
            cls.blocks = System.instance.blocks
            cls.list_of_examples = System.instance.list_of_examples
            cls.connectors = System.instance.connectors
            cls.generators = System.instance.generators

    # ----------------------------------------------------------------------
    @classmethod
    def set_log(cls, Logger):
        try:
            cls.instance.Log = Logger
        except:
            print "Could not set logger"

    # ----------------------------------------------------------------------
    @classmethod
    def log(cls, msg):
        try:
            cls.instance.Log.log(msg)
        except:
            print msg

# ------------------------------------------------------------------------------
