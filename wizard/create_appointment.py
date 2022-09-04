from odoo import models, fields, api, _


class CreateAppointmentWizard(models.TransientModel):
     _name = 'create.appointment.wizard'
     _description = 'Create Appointment Wizard'

     date_appointment = fields.Date(string='Date', required=False)
     patient_id = fields.Many2one('hospital.patient', string='Patient', required=True)
     
     def action_create_appointment(self):
          print("create")
          vals = {
               'patient_id': self.patient_id.id,
               'date_appointment': self.date_appointment
          }
          appointment_rec = self.env['hospital.appointment'].create(vals)
          return {
               'name': _('Appointment'),
               'type': 'ir.actions.act_window',
               'view_mode': 'form',
               'res_model': 'hospital.appointment',
               'res_id': appointment_rec.id,
               'target': 'new',
          }
          
     def action_view_appointment(self):
          action = self.env.ref('om_hospital.action_hospital_appointment').read()[0]
          action['domain'] = [('patient_id', '=', self.patient_id.id)]
          return action
    