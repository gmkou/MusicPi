# -*- coding: utf-8 -*-
import os
from nose.tools import with_setup, raises

fifo = "/tmp/mplayercontrol"
 
def fifo_test():
    exist = os.path.exists(fifo)
    assert exist 
 
 
