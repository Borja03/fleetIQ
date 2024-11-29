from odoo import fields, models

class Vehiculo(models.Model):
    _name="fleetiq.vehiculo"

    vehiculo_id = fields.Integer(string="ID")
    fecha_itv = fields.Datetime(string="Fecha de ITV")
    fecha_matriculacion = fields.Datetime(string="Fecha de Matriculacion")
    matricula = fields.Char(string="Número de Paquetes")
    active = fields.Boolean(string="Activo")
    capacidad = fields.Integer(string="Capacidad del vehiculo")
    modelo = fields.Char(string="Modelo")