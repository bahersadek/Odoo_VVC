from odoo import fields, models

class VvcCertificateType(models.Model):
    _name = "vvc.certificate.type"
    _description = "Certificate Type Data"
    _rec_name = 'cert_name'

    cert_name = fields.Char(string='Certificate Type Name', required=True, translate=True)
    certificates = fields.One2many(comodel_name='vvc.certificate', inverse_name='CertificateType')
    #dep_capacity = fields.Integer()
    #is_open = fields.Boolean()
    #Patients = fields.One2many(comodel_name='hms.patient', inverse_name='dep_name')
    #doctors = fields.One2many(comodel_name='hms.doctors', inverse_name='dep_name')

