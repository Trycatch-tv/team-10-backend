from rolepermissions.roles import AbstractUserRole

class Profesor(AbstractUserRole):
    available_permissions = {
        'create_medical_record': True,
    }

class Estudiante(AbstractUserRole):
    available_permissions = {
        'edit_patient_file': True,
    }