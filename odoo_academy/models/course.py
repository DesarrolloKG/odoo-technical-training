# -*- coding: utf-8 -*-

from email.policy import default
from odoo import models, fields, api

class Course(models.Model):
    
    _name = 'academy.course'
    _description = 'Course info' 

    name = fields.Char(string = 'Title', required = true)
    description = fields.Text(string = 'Description')

    level = fields.Selection(string = 'Leven', selection = [
        ('beginner', 'Beginner'), 
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced')
    ], copy = False)

    active = fields.Boolean(string = 'Active', default = True)
    