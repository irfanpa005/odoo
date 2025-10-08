# -*- coding: utf-8 -*-
# from odoo import http


# class IrfCustomers(http.Controller):
#     @http.route('/irf_customers/irf_customers', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/irf_customers/irf_customers/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('irf_customers.listing', {
#             'root': '/irf_customers/irf_customers',
#             'objects': http.request.env['irf_customers.irf_customers'].search([]),
#         })

#     @http.route('/irf_customers/irf_customers/objects/<model("irf_customers.irf_customers"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('irf_customers.object', {
#             'object': obj
#         })

