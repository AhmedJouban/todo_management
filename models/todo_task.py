from odoo import models, fields
from datetime import datetime

class Todo_Task(models.Model):  
    _name = 'todo.management'
    _description = 'To-Do'
    _inherit= ['mail.thread', 'mail.activity.mixin']

    name= fields.Char(default='Task Name', required= True, tracking=1)
    due_date= fields.Datetime(string='Due Date', default= datetime.now(), tracking=1, required=True)
    assign_to= fields.Many2one('res.users' ,tracking=1, required=True)
    status= fields.Selection([('new', 'New'),('in-progress','In Progress'),('complete','Complete')], default='new', tracking=1)
    phone= fields.Char(string='Phone', default= 'Phone Number', required= True, tracking=1)
    priority = fields.Selection([('0', 'Very Low'), ('1', 'Low'), ('2', 'Normal'), ('3', 'High')], string='Priority', tracking=1)
    des= fields.Char(string="Description", required=True, tracking=1)
    note_ids=fields.One2many('todo.lines', 'todo_id')

    def in_progress(self):
        for rec in self:
            rec.status="in-progress"

    def complete(self):
        for rec in self:
            rec.status="complete"

    def new(self):
        for rec in self:
            rec.status="new"




class Todo_Lines(models.Model):
    _name= "todo.lines"

    todo_id=fields.Many2one('todo.management')
    note=fields.Char()