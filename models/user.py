from odoo import models, fields, api
from enum import Enum, auto

class TipoEnum(Enum):
    ADMIN = auto()
    TRABAJADOR = auto()

class User(models.Model):
    _name = 'fleetiq.user'
    _description = 'User Model'

    user_id = fields.Integer(string='ID', required=True)
    email = fields.Char(string='Email', required=True)
    passwd = fields.Char(string='Password', required=True)
    name = fields.Char(string='Name', required=True)
    street = fields.Char(string='Street')
    city = fields.Char(string='City')
    zip = fields.Char(string='Zip Code')
    active = fields.Boolean(string='Active', default=True)
    #enum
    tipo = fields.Selection([
        (TipoEnum.ADMIN.name, 'Admin'),
        (TipoEnum.TRABAJADOR.name, 'Trabajador')
    ], string='Tipo', required=True)

    # N-to-M relationship with Envio
    envio_ids = fields.Many2many('envio.model', string='Envios')