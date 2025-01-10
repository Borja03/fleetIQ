from odoo import fields, models, api
from odoo.exceptions import ValidationError

class Vehiculo(models.Model):
    _name = "fleetiq.vehiculo"

    vehiculo_id = fields.Integer(string="ID", readonly=True, default=lambda self: self._get_next_vehiculo_id())
    fecha_itv = fields.Datetime(string="Fecha de ITV")
    fecha_matriculacion = fields.Datetime(string="Fecha de Matriculación")
    matricula = fields.Char(string="Matrícula", required=True)
    active = fields.Boolean(string="Activo", default=True)
    capacidad = fields.Integer(string="Capacidad del vehículo", required=True)
    modelo = fields.Char(string="Modelo", required=True)

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
        return 1  # Si no hay registros previos, empieza desde 1

    @api.onchange('fecha_itv', 'fecha_matriculacion')
    def _onchange_fechas(self):
        """
        Valida y maneja los cambios en las fechas de ITV y matriculación.
        """
        for record in self:
            if record.fecha_itv and record.fecha_matriculacion and record.fecha_itv < record.fecha_matriculacion:
                raise ValidationError("La fecha de ITV no puede ser anterior a la fecha de matriculación.")

    @api.constrains('fecha_itv', 'fecha_matriculacion')
    def _check_fechas(self):
        """
        Validaciones adicionales para asegurar la coherencia de las fechas.
        """
        for record in self:
            if record.fecha_itv and record.fecha_matriculacion and record.fecha_itv < record.fecha_matriculacion:
                raise ValidationError("La fecha de ITV no puede ser anterior a la fecha de matriculación.")

    @api.constrains('capacidad')
    def _check_capacidad(self):
        """
        Valida que la capacidad del vehículo sea positiva.
        """
        for record in self:
            if record.capacidad <= 0:
                raise ValidationError("La capacidad del vehículo debe ser mayor a 0.")
