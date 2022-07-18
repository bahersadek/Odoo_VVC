from odoo import fields, models, api
from odoo.exceptions import AccessError, UserError, RedirectWarning, ValidationError, Warning
from datetime import date
import re
import phonenumbers

class vvc_customers(models.Model):
    _name = "vvc.customers"
    _description = "Customers Data"
    _rec_name = 'Name'

    Name = fields.Char(string='Name', required=True, translate=True)
    Phone = fields.Char(string='Phone', required=True, translate=True)
    email = fields.Char()
    NationalID = fields.Integer()


    @api.onchange('email')
    def validate_mail(self):
        if self.email:
            match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', self.email)
            if match == None:
                raise ValidationError('Not a valid E-mail ID')

    
    @api.onchange('Phone')
    def validate_phone(self):
        if self.Phone:
            z = phonenumbers.parse(self.Phone, None)
            print(z)
            if not phonenumbers.is_possible_number(z) or not phonenumbers.is_valid_number(z):
                raise ValidationError('Not a valid Phone')