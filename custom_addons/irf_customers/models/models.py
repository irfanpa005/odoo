# -*- coding: utf-8 -*-

from odoo import models, fields, api


class irf_customers(models.Model):
    _name = 'irf_customers.irf_customers'
    _description = 'irf_customers.irf_customers'

    name = fields.Char(string="Customer Name")
    value = fields.Integer(string="Value Amount")
    value2 = fields.Float(string="Calculated Value", compute="_value_pc", store=True)
    description = fields.Text(string="Description")


    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100

