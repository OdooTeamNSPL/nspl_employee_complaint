from email.policy import default

from odoo import models, fields, api
from datetime import date


class ComplaintType(models.Model):
    _name = 'complaint.type'
    _description = 'Complain Type'
    _rec_name = 'complaint_name'

    complaint_name = fields.Char(string='Name')


class EmployeeComplaintForm(models.Model):
    _name = 'employee.complaint'
    _description = 'Employee Complaint'
    _rec_name = 'name'

    name = fields.Char(string='Complaint Name')
    employee_id = fields.Many2one('hr.employee', string='Employee')
    complaint_name = fields.Many2one('complaint.type', string='Complain Type')
    issue = fields.Text(string='Issue')
    action_taken_from_company = fields.Many2one('res.company', string='Action Taken From Company',
                                                default=lambda self: self.env.company)
    issue_date = fields.Date(string='Date', default=fields.Date.context_today)
    resolved_date = fields.Date(string='Resolved Date', readonly=True)
    has_effect_on_work = fields.Boolean(string='Has Effect on Work Efficiency?')
    has_financial_effect = fields.Boolean(string='Has Financial Effect?')
    suggestion = fields.Text(string='Suggested Action')

    state = fields.Selection([
        ('pending', 'Pending'),
        ('resolved', 'Resolved'),

    ], string='Status', default='pending', tracking=True)

    def action_set_resolved(self):
        today = date.today()
        for record in self:
            record.write({
                'state': 'resolved',
                'resolved_date': today,
            })

    def action_set_pending(self):
        for record in self:
            record.write({
                'state': 'pending',
                'resolved_date': False,
            })


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    complaint_ids = fields.One2many('employee.complaint', 'employee_id', string="Complaint Details")
