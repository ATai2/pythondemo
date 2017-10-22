#!/usr/bin/env python
# -*- coding:utf-8 -*-
import coverage,untitled,server

cov = coverage.coverage(source = ['untitled','server','test'])

cov.start()

#coding

# cov.stop()

cov.report()

cov.html_report(directory='covhtml')



