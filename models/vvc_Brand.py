from odoo import fields, models

class VvcBrand(models.Model):
    _name = "vvc.brand"
    _description = "Car Brand Data"
    _rec_name = 'brand'

    brand = fields.Char(string='Brand Name', required=True, translate=True)
    certificates = fields.One2many(comodel_name='vvc.certificate', inverse_name='Brand')


