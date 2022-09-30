from odoo import models, fields, api, _


class AppointmentReportWizard(models.TransientModel):
     _name = 'appointment.report.wizard'
     _description = 'Print Appointment Wizard'
     
     
     patient_id = fields.Many2one('hospital.patient', string='Patient', required=True)
     date_from = fields.Date(string='Date From', required=False)
     date_to = fields.Date(string='Date To', required=False)
     
     def action_print_excel_report(self):
          domain = []
          patient_id = self.patient_id
          if patient_id:
               domain += [('patient_id', '=', patient_id.id)]
          date_from = self.date_from
          if date_from:
               domain += [('date_appointment', '>=', date_from)]
          date_to = self.date_to
          if date_to:
               domain += [('date_appointment', '<=', date_to)] 
          appointments = self.env['hospital.appointment'].search_read(domain)
          data = {
               'appointments': appointments,
               'form_data': self.read()[0],
          }
          return self.env.ref('om_hospital.report_patient_appointment_xlsx').report_action(self, data=data)
     
     def action_print_report(self):
          domain = []
          patient_id = self.patient_id
          if patient_id:
               domain += [('patient_id', '=', patient_id.id)]
          date_from = self.date_from
          if date_from:
               domain += [('date_appointment', '>=', date_from)]
          date_to = self.date_to
          if date_to:
               domain += [('date_appointment', '<=', date_to)]
          appointments = self.env['hospital.appointment'].search_read(domain)
          data = {
               'form_data': self.read()[0],
               'appointmrnts': appointments
          }
          return self.env.ref('om_hospital.action_report_appointment').report_action(self, data=data)
    