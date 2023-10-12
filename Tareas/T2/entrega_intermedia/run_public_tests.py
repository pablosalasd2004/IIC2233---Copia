import unittest
from test_publicos.test_00_validacion_formato import TestValidacionFormato
from test_publicos.test_01_usuario_permitido import TestUsuarioPermitido
from test_publicos.test_02_riesgo_mortal import TestRiesgoMortal
from test_publicos.test_03_usar_item import TestUsarItem
from test_publicos.test_04_calcular_puntaje import TestCalcularPuntaje
from test_publicos.test_05_validar_direccion import TestValidarDireccion
from test_publicos.test_06_serializar_mensaje import TestSerializarMensaje
from test_publicos.test_07_separar_mensaje import TestSepararMensaje
from test_publicos.test_08_encriptar_mensaje import TestEncriptarMensaje
from test_publicos.test_09_codificar_mensaje import TestCodificarMensaje

if __name__ == "__main__":
    unittest.main(verbosity=2)