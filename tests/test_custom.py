#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 18:19:47 2020
@author: nedeleg
"""


from unittest import TestCase
from pywpipe import *

class ComeCoreSampleTest(TestCase):
    def test_basic_custom(self):
        pserver = pywpipe.Server('testpipe', pywpipe.Mode.Slave, maxclients=100)
        pserver.shutdown()
        self.assertEqual(0, pserver.getclientcount())