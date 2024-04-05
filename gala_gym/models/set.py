from odoo import models, fields, api


class Set(models.Model):
    _name = "gala_gym.set"
    _order = 'index asc'

    name = fields.Char(compute="_compute_name")
    exercice_id = fields.Many2one("gala_gym.exercice", "Exercice")
    index = fields.Integer("Order", default=0)
    reps = fields.Integer("Repetitions", default =0)
    weight = fields.Integer("Weight in KG", default=0)
    time = fields.Integer("Time", default=0)

    @api.depends("reps","weight","time")
    def _compute_name(self):
        for set in self:
            if set.reps != 0:
                set.name = str(set.reps) + " reps"
                if set.weight != 0:
                    set.name += " with " + str(set.weight) + "KG"
            elif set.time != 0:
                set.name = str(set.time) + " secondes"
                if set.weight != 0:
                    set.name += " with " + str(set.weight) + "KG"
            else:
                set.name = "*"