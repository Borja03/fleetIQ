from odoo import models, fields, api
from datetime import datetime

class Paquete(models.Model):
    _name = "fleetiq.paquete"
    _description = 'Modelo de Paquete'

    # Numeric ID (will be automatically created by Odoo)
    paquete_id = fields.Integer(string="ID")

    # Peso (Weight) attribute
    peso = fields.Float(string='Peso', required=True)

    # Tamano as a Selection field
    tamano = fields.Selection([
        ('pequeno', 'Pequeño'),
        ('mediano', 'Mediano'),
        ('grande', 'Grande')
    ], string='Tamaño', required=True)

    # Enviador (Sender) attribute
    enviador = fields.Char(string='Enviador', required=True)

    # Reciver (Receiver) attribute
    receptor = fields.Char(string='Receptor', required=True)

    # Fecha de Creación attribute
    fecha_creacion = fields.Datetime(string='Fecha de Creación', default=fields.Datetime.now)

    # One2many relationship with Envio
    envio_id = fields.Many2one('envio.model', string='Envío')

    # Optional: Constraint to validate weight
    @api.constrains('peso')
    def _check_peso(self):
        for record in self:
            if record.peso <= 0:
                raise models.ValidationError('El peso debe ser mayor que cero')