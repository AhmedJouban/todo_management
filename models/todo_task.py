from odoo import models, fields, api
from datetime import datetime, timedelta

class Todo_Task(models.Model):  
    _name = 'todo.management'
    _description = 'To-Do'
    _inherit= ['mail.thread', 'mail.activity.mixin']

    name= fields.Char(default='Task Name', required= True, tracking=1)
    creation_date= fields.Datetime(string='Creation Date', default= datetime.now(), tracking=1, required=True)
    assign_to= fields.Many2one('res.users' ,tracking=1, required=True)
    status= fields.Selection([('new', 'New'),('in-progress','In Progress'),('complete','Complete'),('closed','Closed')], default='new', tracking=1)
    phone= fields.Char(string='Phone', default= 'Phone Number', required= True, tracking=1)
    priority = fields.Selection([('0', 'Very Low'), ('1', 'Low'), ('2', 'Normal'), ('3', 'High')], string='Priority', tracking=1)
    des= fields.Char(string="Description", required=True, tracking=1)
    note_ids=fields.One2many('todo.lines', 'todo_id')
    active= fields.Boolean(default= True)
    days_to_complete= fields.Integer(string='Days to Complete', default=5, required=1, tracking=1)
    due_date= fields.Datetime(compute='_due_date_field', string='Due Date')
    is_late= fields.Boolean()


    def in_progress(self):
        for rec in self:
            rec.status="in-progress"

    def complete(self):
        for rec in self:
            rec.status="complete"

    def state_new(self):
        for rec in self:
            rec.status="new"
    
    def closed_state(self):
        for rec in self:
            rec.status= 'closed'

    @api.depends('days_to_complete', 'creation_date')
    def _due_date_field(self):
        for rec in self:
            rec.due_date= rec.creation_date + timedelta(days=rec.days_to_complete)

    def check_due_date(self):
        tasks_ids=self.search([])
        for rec in tasks_ids:
            if rec.due_date <= fields.datetime.now():
                rec.is_late=True
            else:
                rec.is_late=False




class Todo_Lines(models.Model):
    _name= "todo.lines"

    todo_id=fields.Many2one('todo.management')
    note=fields.Char()