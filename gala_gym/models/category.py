from odoo import models, fields


class Category(models.Model):
    _name = "gala_gym.category"

    name = fields.Char("Name")
    exercice_class_ids = fields.Many2many("gala_gym.exercice_class",
                                "exercice_category",
                                "category_id",
                                "exercice_id")
    description = fields.Text("Description")