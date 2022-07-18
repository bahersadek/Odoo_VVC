from odoo import fields, models
from datetime import datetime

class VvcCertificatePrint(models.Model):
    _name = "vvc.certificate.print"
    _description = "Certificate Print Data"
    _rec_name = 'cert_id'

    cert_id = fields.Many2one(comodel_name='vvc.certificate')
    first_print_flag = fields.Boolean(default=True)
    print_date = fields.Datetime(default=datetime.now())


    #dep_capacity = fields.Integer()
    #is_open = fields.Boolean()
    #Patients = fields.One2many(comodel_name='hms.patient', inverse_name='dep_name')
    #doctors = fields.One2many(comodel_name='hms.doctors', inverse_name='dep_name')

