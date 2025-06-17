class PacienteNoEncontradoException(Exception):
    pass


class MedicoNoEncontradoException(Exception):
    pass


class MedicoNoDisponibleException(Exception):
    pass


class TurnoOcupadoException(Exception):
    pass


class RecetaInvalidaException(Exception):
    pass


# estas las agregue por que considero que son importantes
class PacienteDuplicadoException(Exception):
    pass


class MedicoDuplicadoException(Exception):
    pass


class EspecialidadDuplicadaException(Exception):
    pass


class DatosInvalidosException(Exception):
    pass
