from odoo import models, fields, api
from datetime import datetime

from odoo.exceptions import ValidationError


class Workout(models.Model):
    _name = "gala_gym.workout"

    name = fields.Char("Workout Name", default="Workout el Abtal")
    session_ids = fields.One2many("gala_gym.session","workout_id",
                                  "Sessions")
    start_date = fields.Date("Start Date", default=datetime.now())
    end_date = fields.Date("End Date")
    number_of_sessions = fields.Integer("Number of sessions",compute="_compute_number_of_sessions")
    duration = fields.Char("Duration", compute="_compute_duration")
    @api.constrains('end_date')
    def _check_end_date(self):
        for record in self:
            if record.end_date < record.start_date:
                raise ValidationError("The end date cannot be set in the past")

    @api.depends("session_ids")
    def _compute_number_of_sessions(self):
        for workout in self:
            workout.number_of_sessions = len(workout.session_ids)

    @api.depends("start_date","end_date")
    def _compute_duration(self):
        for workout in self:
            workout.duration = str((workout.end_date - workout.start_date).days) + " Days"