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

    # Fragile attribute
    fragil = fields.Boolean(string='Frágil', default=False)

    # Fecha de Creación attribute
    fecha_creacion = fields.Datetime(string='Fecha de Creación', default=lambda self: fields.Datetime.now())

    # One2many relationship with Envio
    envio_id = fields.Many2one('envio.model', string='Envío')

    # Constraint to validate weight
    @api.constrains('peso')
    def _check_peso(self):
        for record in self:
            if record.peso <= 0:
                raise models.ValidationError('El peso debe ser mayor que cero')

            # Additional weight constraints based on package size
            if record.tamano == 'pequeno' and record.peso > 5:
                raise models.ValidationError('Un paquete pequeño no puede pesar más de 5 kg')
            elif record.tamano == 'mediano' and record.peso > 20:
                raise models.ValidationError('Un paquete mediano no puede pesar más de 20 kg')
            elif record.tamano == 'grande' and record.peso > 50:
                raise models.ValidationError('Un paquete grande no puede pesar más de 50 kg')

    # Onchange method for package size
    @api.onchange('tamano')
    def _onchange_tamano(self):
        if self.tamano == 'pequeno':
            self.peso = min(self.peso, 5) if self.peso else 0
        elif self.tamano == 'mediano':
            self.peso = min(self.peso, 20) if self.peso else 0
        elif self.tamano == 'grande':
            self.peso = min(self.peso, 50) if self.peso else 0