from odoo import models, fields

class Project(models.Model):
    _inherit = "project.task"

    # Agrega aquí los nuevos campos o modificaciones
    x_collaborator_ids = fields.Many2many(
        "res.users",
        string="Colaboradores"
    )

    x_predeccessor_ids = fields.Many2many(
        "project.project",
        relation="project_predecessor_rel",
        column1="project_id",
        column2="predecessor_id",
        string="Predecesores"
    )

    x_succesor_ids = fields.Many2many(
        "project.project",
        relation="project_successor_rel",
        column1="project_id",
        column2="successor_id",
        string="Sucesores"
    )
