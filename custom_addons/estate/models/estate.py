# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models

class EstateProperties(models.Model):
    _name = "estate.property"
    _description = "Real Estate properties"
    _order = "id"
    _log_access = True  # Enable automatic logging of create/write timestamps and user

    name = fields.Char(string="Name")
    description = fields.Text(string="Description")
    postcode = fields.Char(string="Postcode")
    date_availability = fields.Date(string="Date Availability")
    expected_price = fields.Float(string="Expected Price")
    selling_price = fields.Float(string="Selling Price")
    bedrooms = fields.Integer(string="Bedrooms")
    living_area = fields.Integer(string="Living Area (sq.m)")
    facades = fields.Integer(string="Facades")
    garage = fields.Boolean(string="Garage")
    garden = fields.Boolean(string="Garden")
    garden_area = fields.Integer(string="Garden Area")
    garden_orientation = fields.Char(string="Garden Orientation")

    create_uid = fields.Many2one('res.users', string="Created by", readonly=True)
    create_date = fields.Datetime(string="Creation Date", readonly=True)
    write_uid = fields.Many2one('res.users', string="Last Updated by", readonly=True)
    write_date = fields.Datetime(string="Last Update Date", readonly=True)
