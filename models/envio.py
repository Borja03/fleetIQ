from odoo import models, fields, api
from datetime import datetime


class Envio(models.Model):
    _name = "fleetiq.envio"

    envio_id = fields.Integer(string="ID", readonly=True, default=lambda self: self._get_next_envio_id())
    fecha_envio = fields.Datetime(string="Fecha de Envio")
    fecha_entrega = fields.Datetime(string="Fecha de Entrega")
    num_paquetes = fields.Integer(string="Número de Paquetes")
    estado = fields.Selection([
        ('pendiente', 'Pendiente'),
        ('en_reparto', 'En Reparto'),
        ('finalizado', 'Finalizado')
    ], string="Estado del Envío", compute="_compute_estado", store=True)

    # Relación Many2one con el vehículo
    vehiculo_id = fields.Many2one('fleetiq.vehiculo', string="Vehículo")

    # Relacionar con la matrícula del vehículo, usando el campo related
    vehiculo_matricula = fields.Char(
        string="Matrícula del Vehículo",
        related="vehiculo_id.matricula",  # Aquí accedemos correctamente al campo 'matricula' del vehículo
        store=True
    )

    # Campo calculado para la ruta
    ruta_id = fields.Char(
        string="Ruta",
        compute="_compute_ruta",
        store=True
    )

    # Campo para seleccionar el usuario asignado
    usuario_id = fields.Many2one(
        'res.users',
        string='Creador del envio',
        domain=[('active', '=', True)],  # Solo usuarios activos
        required=True,  # Hace que sea obligatorio seleccionar un usuario
    )

    @api.model
    def _get_next_envio_id(self):
        """
        Obtiene el siguiente ID de envio incrementando el último registrado.
        """
        last_envio = self.search([], order="envio_id desc", limit=1)
        if last_envio:
            return last_envio.envio_id + 1
        return 1  # Si no hay envíos previos, empieza desde 1

    @api.depends('fecha_envio', 'fecha_entrega')
    def _compute_estado(self):
        for record in self:
            # Validar que la fecha_envio es anterior a la fecha_entrega
            if record.fecha_envio and record.fecha_entrega and record.fecha_envio > record.fecha_entrega:
                raise ValidationError("La fecha de envío no puede ser posterior a la fecha de entrega.")

            # Determinar el estado basado en las fechas
            if not record.fecha_envio or record.fecha_envio > fields.Datetime.now():
                record.estado = 'pendiente'
            elif record.fecha_envio <= fields.Datetime.now() and (
                    not record.fecha_entrega or record.fecha_entrega > fields.Datetime.now()):
                record.estado = 'en_reparto'
            elif record.fecha_entrega and record.fecha_entrega <= fields.Datetime.now():
                record.estado = 'finalizado'
            else:
                record.estado = 'pendiente'  # Si no cumple ninguna de las condiciones anteriores

    def _compute_ruta(self):
        for record in self:
            if record.ruta_id:
                ruta = self.env['fleetiq.ruta'].search([
                    ('id', '=', record.ruta_id)
                ], limit=1)
                if ruta:
                    origen_code = ruta.origen[:3] if ruta.origen else ''
                    destino_code = ruta.destino[:3] if ruta.destino else ''
                    record.ruta_id = f"{origen_code}-{destino_code}"
                else:
                    record.ruta_id = ''
            else:
                record.ruta_id = ''
