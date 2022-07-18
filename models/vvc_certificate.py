from odoo import fields, models, api
from odoo.exceptions import AccessError, UserError, RedirectWarning, ValidationError, Warning
from datetime import datetime
from dateutil import relativedelta
import re

class vvc_certificate(models.Model):
    _name = "vvc.certificate"
    _description = "Certificate Data"
    _rec_name = 'SerialNumber'

    SerialNumber = fields.Char(string='Serial Number', readonly=True, required=True, copy=False, default='New')
    CertificateType = fields.Many2one(comodel_name='vvc.certificate.type')
    TrafficDepartment = fields.Many2one(comodel_name='vvc.traffic.department')
    VehicleType = fields.Selection([('car','Car'),
                                   ('bus','Bus'),
                                   ('minibus','MiniBus'),
                                   ('microbus','MicroBus')])
    Customer = fields.Many2one(comodel_name='res.partner')
    CarModel = fields.Selection(selection='_get_selection', string='Car Model')
    Brand = fields.Many2one(comodel_name='vvc.brand')
    Price = fields.Float()
    MotorNumber = fields.Char()
    ChasisNumber = fields.Char()
    allow_reprint =  fields.Boolean(default=False)
    print_logs = fields.One2many(comodel_name='vvc.certificate.print', inverse_name='cert_id', readonly=True)

    
    def _get_selection(self):
        yrs_ago = datetime.today().year - 20
        current_year = datetime.now().year        
        return ([((str(r)), (str(r))) for r in range(yrs_ago, current_year)])


    def print_report(self):
        #flag = self.pool.get('res.users').has_group(cr, uid, 'vvc.vvc_supervisors_group') 
        flag = self.env['res.users'].has_group('vvc.vvc_supervisors_group')
        print_flag = self.env['vvc.certificate.print'].search([('cert_id', '=', self.id)], limit=1).first_print_flag
        if flag or self.allow_reprint or print_flag:
            print_vals = {
            'cert_id': self.id,
            'first_print_flag': False,
            }
            oo = self.env['vvc.certificate.print'].write(print_vals)
            return self.env.ref('vvc.vvc_certificate_report_action').report_action(self)
        else:
            raise ValidationError('Not Allowed for Printing')
    

    def allow_print(self):
        print_vals = {        
            'allow_reprint': True,
            }
        result = super().write(print_vals)
        return result



    @api.model
    def create(self, vals):
        if vals.get('SerialNumber', 'New') == 'New':
            vals['SerialNumber'] = str(self.env['ir.sequence'].next_by_code('certificates.id')) or 'New' ##Adding plus 1
        print("Hello this is sequ   ",vals['SerialNumber'])        
        result = super().create(vals)
        print_vals = {
            'cert_id': result.id,
            'first_print_flag': False,
        }
        oo = self.env['vvc.certificate.print'].create(print_vals)
        return result