from odoo import models, fields, api


class Exercice(models.Model):
    _name = "gala_gym.exercice"

    name=fields.Char("Name", compute="_compute_name")
    name_id = fields.Many2one("gala_gym.exercice_class",
                           "Name")
    session_id = fields.Many2one("gala_gym.session", "Session")
    set_ids = fields.One2many("gala_gym.set", "exercice_id","Sets")
    index = fields.Integer("Order",default=0)
    note = fields.Text("Notes")

    @api.depends("name_id")
    def _compute_name(self):
        for rec in self:
            rec.name = rec.name_id.name + " x" + str(len(rec.set_ids))