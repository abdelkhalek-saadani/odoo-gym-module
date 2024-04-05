from odoo import models, fields, api
from datetime import datetime




class Session(models.Model):
    _name = "gala_gym.session"

    name = fields.Char("Session Name", default="Session of the free will man")
    workout_id = fields.Many2one("gala_gym.workout",
                                 "Workout")
    exercice_ids = fields.One2many("gala_gym.exercice","session_id",
                                   "Exercices")
    date = fields.Date("Date", default=datetime.now())
    duration = fields.Integer("Duration in minutes")
    note = fields.Text("Notes")

    formatted_date = fields.Char(string="Day", compute='_compute_formatted_date')

    @api.depends("date")
    def _compute_formatted_date(self):
        for session in self:
            formatted_date = session.date.strftime("%a %d %B %Y")
            session.formatted_date = formatted_date
