# -*- coding: utf-8 -*-
from unittest import TestCase
import os
from nose.tools import with_setup, raises

fifo = "/tmp/mplayercontrol.fifo"

class FifoTestCase(TestCase):
    def setUp(self):
        print 'before test'
    
    def tearDown(self):
        print 'after test'
        
    def fifo_test(self):
        exist = os.path.exists(fifo)
        assert exist 
 
 
