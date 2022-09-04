from odoo import models, fields, api, _


class HospitalDoctor(models.Model):
     _name = 'hospital.doctor'
     _inherit = ["mail.thread","mail.activity.mixin"]
     _description = 'Hospital Doctor'
     _rec_name = 'doctor_name'

     doctor_name = fields.Char(string='Name', tracking=True, required=True)
     age = fields.Integer(string='Age', tracking=True)
     gender = fields.Selection([('male','Male'),('female','Female'),('other','Other')], tracking=True, required=True, default='male')
     note = fields.Text(string='Description', tracking=True)
     image = fields.Binary(string='Doctor Image')
     
     