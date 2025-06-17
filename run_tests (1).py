#!/usr/bin/env python3
"""
Script para ejecutar todas las pruebas unitarias del Sistema de Gestión Clínica.
"""

import unittest
import sys
import os

# Agregar el directorio del proyecto al path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def main():
    """Ejecuta todas las pruebas unitarias."""
    print("Ejecutando Pruebas Unitarias del Sistema de Gestión Clínica")
    print("=" * 70)
    
    # Descubrir y ejecutar todas las pruebas en el directorio tests
    loader = unittest.TestLoader()
    start_dir = 'tests'
    suite = loader.discover(start_dir, pattern='test_*.py')
    
    # Ejecutar las pruebas
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    print("\n" + "=" * 70)
    print("RESUMEN DE PRUEBAS")
    print("=" * 70)
    print(f"Pruebas ejecutadas: {result.testsRun}")
    print(f"Errores: {len(result.errors)}")
    print(f"Fallos: {len(result.failures)}")
    
    if result.wasSuccessful():
        print("Todo ok")
        return 0
    else:
        print("fallo")
        return 1

if __name__ == "__main__":
    sys.exit(main()) 