#!/bin/sh

export PYTHONPATH=/usr/local/lib/python2.7/site-packages/
export LD_LIBRARY_PATH=/usr/local/lib
export PKG_CONFIG_PATH=/usr/local/lib/pkgconfig

python $1
