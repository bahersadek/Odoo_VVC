from odoo import fields, models

class VvcTrafficDepartment(models.Model):
    _name = "vvc.traffic.department"
    _description = "Traffic Department Data"
    _rec_name = 'dep_name'

    dep_name = fields.Char(string='Department Name', required=True, translate=True)
    #dep_capacity = fields.Integer()
    is_open = fields.Boolean()
    certificates = fields.One2many(comodel_name='vvc.certificate', inverse_name='TrafficDepartment')

    #Patients = fields.One2many(comodel_name='hms.patient', inverse_name='dep_name')
    #doctors = fields.One2many(comodel_name='hms.doctors', inverse_name='dep_name')

