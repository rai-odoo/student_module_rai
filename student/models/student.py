from odoo import models, fields,api
from datetime import datetime, timedelta

class Student(models.Model):                
    _name = 'student.information1'        


    name = fields.Char(string="Student Name", required = True)
    birth_date = fields.Date()                
    age = fields.Integer(compute="compute_age") 
    sport_enthusiastic = fields.Boolean(string = "Sport Enthusiastic?")
    # sport_membership = fields.Selection([("game1","Cricket"),("game2","Vollyball")])
    start_exam = fields.Datetime(required = True)
    village = fields.Char()
    gender = fields.Selection([("male","Male"),("female","Female")])
    subject_1 = fields.Integer()
    subject_2 = fields.Integer()
    average = fields.Float(compute="compute_average",store=True)
    display_name = fields.Char()
    display_name1 = fields.Char()
    college_name_id = fields.Many2one('student.college')
    college_lines = fields.One2many('student.college.lines','student_id')
    description = fields.Char()
    student_subject = fields.Many2many('student.subject')

    @api.depends("birth_date") # birthdate to age
    def compute_age(self):
        for b in self:
            if b.birth_date is not False:
                b.age = (datetime.today().date() - b.birth_date) // timedelta(365)  #// floor division 

    @api.depends("subject_1","subject_2") # average
    def compute_average(self):
        for a in self:
            a.average = (a.subject_1 + a.subject_2)/2

    @api.onchange('name')    # display_name  
    def _onchange_name(self):
        self.display_name = 'Hello' + self.name if self.name else ''   

    @api.onchange('age')    #display_name1
    def _onchange_age(self):
        self.display_name1 = 'Your age is: %s' % (self.age if self.age else '')         
           
class College(models.Model):  #Many2one
    _name = 'student.college'

    name = fields.Char(string='College Name')
    college_address = fields.Char()
    taluka = fields.Char()
    distict = fields.Char()

class College1(models.Model):  #One2many
    _name = 'student.college.lines'

    name = fields.Char(string = 'College Name')
    college_address = fields.Char()
    taluka = fields.Char()
    distict = fields.Char()  
    student_id = fields.Many2one('student.information1') 

class Subject(models.Model):  #Many2many
    _name = 'student.subject'

    name = fields.Char()




