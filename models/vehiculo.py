from odoo import fields, models

class Vehiculo(models.Model):
    _name="fleetiq.vehiculo"

    vehiculo_id = fields.Integer(string="ID")
    fecha_itv = fields.Datetime(string="Fecha de ITV")
    fecha_matriculacion = fields.Datetime(string="Fecha de Matriculacion")
    matricula = fields.Char(string="Matrícula")
    active = fields.Boolean(string="Activo")
    capacidad = fields.Integer(string="Capacidad del vehiculo")
    modelo = fields.Char(string="Modelo")

    # Relación Many2one con el envío
    envio_id = fields.Many2one('fleetiq.envio', string="Envío")

    # Relación Many2one con la ruta
    ruta_id = fields.Many2one('fleetiq.ruta', string="Ruta")
