from odoo import fields, models, api

class Vehiculo(models.Model):
    _name = "fleetiq.vehiculo"

    vehiculo_id = fields.Integer(string="ID")
    fecha_itv = fields.Datetime(string="Fecha de ITV")
    fecha_matriculacion = fields.Datetime(string="Fecha de Matriculación")
    matricula = fields.Char(string="Matrícula")
    active = fields.Boolean(string="Activo")
    capacidad = fields.Integer(string="Capacidad del vehiculo")
    modelo = fields.Char(string="Modelo")

    # Relación Many2one con el envío
    envio_id = fields.Many2one('fleetiq.envio', string="Envío")

    # Relación Many2one con la ruta
    ruta_id = fields.Many2one('fleetiq.ruta', string="Ruta")

    @api.model
    def _get_next_vehiculo_id(self):
        """
        Obtiene el siguiente ID de vehiculo incrementando el último registrado.
        """
        last_vehiculo = self.search([], order="vehiculo_id desc", limit=1)
        if last_vehiculo:
            return last_vehiculo.vehiculo_id + 1
        return 1  # Si no hay envíos previos, empieza desde 1
