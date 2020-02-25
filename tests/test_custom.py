#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 18:19:47 2020
@author: nedeleg
"""


from unittest import TestCase
from pywpipe import * as wpipe

class ComeCoreSampleTest(TestCase):
    def test_basic_custom(self):
        pserver = wpipe.Server('testpipe', wpipe.Mode.Slave, maxclients=100)
        pserver.shutdown()
        self.assertEqual(0, pserver.getclientcount())