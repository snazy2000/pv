__author__ = 'adam'

import pv
import serial
import sys

pv.debug()
pv.debug_color()
try:
	port = serial.Serial('/dev/tty.usbserial', timeout = 10, write_timeout = 5)

	from pv import cms
	inv = cms.Inverter(port)

	inv.reset()
	sn = inv.discover()
	if sn is None:
		print "Inverter is not connected."
		sys.exit(1)
	ok = inv.register(sn)		# Associates the inverter and assigns default address
	if not ok:
		print "Inverter registration failed."
		sys.exit(1)

	print inv.version()

	param_layout = inv.param_layout()
	parameters = inv.parameters(param_layout)
	for field in parameters:
		print "%-10s: %s" % field

	status_layout = inv.status_layout()
	status = inv.status(status_layout)
	for field in status:
		print "%-10s: %s" % field

	port.close()

except:
        print("Serial connection did not answer");