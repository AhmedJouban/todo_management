from odoo import models, fields
from datetime import datetime

class Todo_Task(models.Model):  
    _name = 'todo.management'
    _description = 'To-Do'
    _inherit= ['mail.thread', 'mail.activity.mixin']

    name= fields.Char(default='Task Name', required= True, tracking=1)
    due_date= fields.Datetime(string='Due Date', default= datetime.now(), tracking=1)
    assign_to= fields.Many2one('res.users' ,tracking=1)
    status= fields.Selection([('new', 'New'),('in-progress','In Progress'),('complete','Complete')], default='new', tracking=1)
    phone= fields.Char(string='Phone', default= 'Phone Number', required= True, tracking=1)
    priority = fields.Selection([('0', 'Very Low'), ('1', 'Low'), ('2', 'Normal'), ('3', 'High')], string='Priority', tracking=1)
    des= fields.Char(string="Description", required=True, tracking=1)