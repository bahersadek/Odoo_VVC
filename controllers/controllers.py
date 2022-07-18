# -*- coding: utf-8 -*-
# from odoo import http


# class Vvc(http.Controller):
#     @http.route('/vvc/vvc', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vvc/vvc/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('vvc.listing', {
#             'root': '/vvc/vvc',
#             'objects': http.request.env['vvc.vvc'].search([]),
#         })

#     @http.route('/vvc/vvc/objects/<model("vvc.vvc"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vvc.object', {
#             'object': obj
#         })
