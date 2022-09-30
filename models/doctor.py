from odoo import models, fields, api, _


class HospitalDoctor(models.Model):
     _name = 'hospital.doctor'
     _inherit = ["mail.thread","mail.activity.mixin"]
     _description = 'Hospital Doctor'
     _rec_name = 'doctor_name'

     doctor_name = fields.Char(string='Name', tracking=True, required=True)
     age = fields.Integer(string='Age', tracking=True, copy=False)
     gender = fields.Selection([('male','Male'),('female','Female'),('other','Other')], tracking=True, required=True, default='male')
     note = fields.Text(string='Description', tracking=True)
     image = fields.Binary(string='Doctor Image')
     appointment_count = fields.Integer(string='Appointment Count', compute='_compute_appointment_count')
     active = fields.Boolean(string='Active', default=True)
     
     def copy(self, default=None):
          print("Successfully Overided")
          if default is None:
               default = {}
          if default.get('doctor_name'):
               default['doctor_name'] = _("%s (Copy)", self.doctor_name)
          default['note'] = "copied record"
          return super(HospitalDoctor, self).copy(default)
     
     def _compute_appointment_count(self):
          for rec in self:
               appointment_count = self.env['hospital.appointment'].search_count([('doctor_id', '=', rec.id)])
               rec.appointment_count = appointment_count
     
     