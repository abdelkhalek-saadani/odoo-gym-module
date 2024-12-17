from odoo import models, fields

class ExerciceClass(models.Model):
    _name = "gym.exercice_class"

    name = fields.Char("Exercice Name")
    category_ids = fields.Many2many("gym.category",
                                "exercice_category",
                                "exercice_id",
                                "category_id")
    description = fields.Text("Description")

    """def name_get(self):
        res="name_get in ExerciceClass has an error"
        for rec in self:
            res = rec.name
        return res"""