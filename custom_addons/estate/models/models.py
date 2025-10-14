# -*- coding: utf-8 -*-

from odoo import models, fields, api

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

    # address fields
    street = fields.Char()
    street2 = fields.Char()
    zip = fields.Char(change_default=True)
    city = fields.Char()
    country_id = fields.Many2one('res.country')
    state_id = fields.Many2one(
        "res.country.state", 
        string='State', 
        domain="[('country_id', '=?', country_id)]"
    )
    country_code = fields.Char(related='country_id.code', string="Country Code")
    partner_latitude = fields.Float(string='Geo Latitude', digits=(10, 7))
    partner_longitude = fields.Float(string='Geo Longitude', digits=(10, 7))

    create_uid = fields.Many2one('res.users', string="Created by", readonly=True)
    create_date = fields.Datetime(string="Creation Date", readonly=True)
    write_uid = fields.Many2one('res.users', string="Last Updated by", readonly=True)
    write_date = fields.Datetime(string="Last Update Date", readonly=True)
