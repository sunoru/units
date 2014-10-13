#!/bin/env python
# -*- coding:utf-8 -*-
# filename: units/console.py
# by Xero Essential

from code import InteractiveConsole
import re
from .value_type import genValue as V

class UnitConsole(InteractiveConsole):
	def __init__(self):
		InteractiveConsole.__init__(self)
		self.reg=re.compile(r'(\d+[a-zA-Z+-/*^]+)')
	
	def warp_unit(self, s):
		return self.reg.sub(r"V('\1')", s)

	def interact(self):
		self.push('from units.api import V')
		while True:
			s = self.raw_input('\(^o^)/~ ~ ')
			s = self.warp_unit(s)
			if s == 'end()' :
				break
			self.push(s)


def start():
	con = UnitConsole()
	con.interact()

#start()

