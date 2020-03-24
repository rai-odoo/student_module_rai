from odoo import models, fields,api


class Student(models.Model):                
    _name = 'student.information1'            

    name = fields.Char(string="Student Name", required = True) 
    display_name = fields.Char()
    birth_date = fields.Date(required = True)                
    age = fields.Integer(required = True) 
    sport = fields.Boolean(required = True)
    start_exam = fields.Datetime(required = True)
    percentage = fields.Float(required = True)
    village = fields.Char()
    subject_1 = fields.Integer()
    subject_2 = fields.Integer()
    average = fields.Float(compute="compute_average")

    @api.depends("subject_1","subject_2")
    def compute_average(self):
    	for a in self:
    		a.average = (a.subject_1 + a.subject_2)/2

    
    @api.onchange('name')
    def _onchange_name(self):
        self.display_name = 'Hello' + self.name if self.name else ''
