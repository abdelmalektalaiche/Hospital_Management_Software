from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class HospitalAppointment(models.Model):
     _name = 'hospital.appointment'
     _inherit = ["mail.thread","mail.activity.mixin"]
     _description = 'Hospital Appointment'
     _order = "name desc"

     name = fields.Char(string='Order Reference', tracking=True, required=True, copy=False, readonly=True, default=lambda self: _('New'))
     patient_id = fields.Many2one('hospital.patient', string='Patient', required=True)
     patient_name_id = fields.Many2one('hospital.patient', string='Patient Name', required=True)  
     age = fields.Integer(string='Age', related='patient_id.age', tracking=True)
     doctor_id = fields.Many2one('hospital.doctor', string='Doctor', required=True)
     gender = fields.Selection([('male','Male'),('female','Female'),('other','Other')])
     state = fields.Selection([('draft','Draft'), ('confirm','confirmed'), ('done','Done'), ('cancel','Cancelled')], default='draft', tracking=True, string='status')
     note = fields.Text(string='Description', tracking=True)
     date_appointment = fields.Date(string="Date")
     date_checkup = fields.Datetime(string="Check up time")
     prescription = fields.Text(string='Prescription', tracking=True)
     prescription_line_ids = fields.One2many('appointment.prescription.lines', 'appointment_id', string='Prescription Lines')
     
     def action_confirm(self):
          self.state = 'confirm'
          
     def action_done(self):
          self.state = 'done'
          
     def action_draft(self):
          self.state = 'draft'
          
     def action_cancel(self):
          self.state = 'cancel'
          
     @api.model 
     def create(self, vals):
          if not vals.get('note'):
               vals['note'] = 'New Patient'
          if vals.get('name', _('New')) == _('New'):
               vals['name'] = self.env['ir.sequence'].next_by_code('hospital.appointment') or _('New')
          res = super(HospitalAppointment, self).create(vals)
          return res
     
     @api.onchange('patient_id')
     def onchange_patient_id(self):
          if self.patient_id:
               if self.patient_id.gender:
                    self.gender = self.patient_id.gender
               if self.patient_id.note:
                    self.note = self.patient_id.note
          else:
               self.gender = ''
               self.note = ''
               
     def unlink(self):
          if self.state == 'done':
               raise ValidationError(_("you cannot delete %s as it is in done state"% self.name))
          return super(HospitalAppointment, self).unlink()
     
     def action_url(self):
          return{
              'type': 'ir.actions.act_url',
              'target': 'new',
              'url': 'https://github.com/abdelmalektalaiche/Hospital_Management_Software',
          }
          
               

class AppointmentPrescriptionLines(models.Model):
     _name = 'appointment.prescription.lines'
     _description = 'Appointment Prescription Lines'
     
     name = fields.Char(string="Medecine", required=True)
     qty = fields.Integer(string="Quantity")
     appointment_id = fields.Many2one('hospital.appointment', string="Appointment")