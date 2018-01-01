# -*- coding: utf-8 -*-
# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe                   
import json
import sys
import time
from frappe import _    
from frappe.utils.background_jobs import enqueue

@frappe.whitelist()
def sync_etsy(etsy_shop_name):
        #"Enqueue longjob for syncing shopify"
	#print >> sys.stderr, "XXXXX {0} {1}".format('hello','world')
	print >> sys.stderr, etsy_shop_name
	settings = frappe.get_doc("Etsy Profile",etsy_shop_name)
	#settings = json.loads(settings)	
	#for key, value in settings.iteritems() :
	#	print >> sys.stderr, "Dict: {0} = {1}".format(key, value)
	#print >> sys.stderr, "etsy_shop_name: {0}".format(settings['etsy_shop_name'])

	#frappe.msgprint(_("Got: {0}"), [settings.etsy_shop_name])
        #frappe.msgprint(_("Queued for syncing. It may take a few minutes."))
	frappe.msgprint('Starting sync in background...')
        enqueue("erpnext_etsy.api.sync_etsy_resources", queue='short', timeout=1500, job_name=etsy_shop_name, settings=settings)



@frappe.whitelist()
def sync_etsy_resources(settings):
	print >> sys.stderr, "Starting sync"
	time.sleep(5)
	print >> sys.stderr, "Client key: {0}".format(settings.client_key)
	time.sleep(5)
	print >> sys.stderr, "Client secret: {0}".format(settings.client_secret)



