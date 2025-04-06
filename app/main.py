from app.cita_manager import CitaManager
from app.historial_cita import HistorialCita
from app.resultados import Resultados
from app.alertas import Alertas

# Crear instancias
cm = CitaManager()
hc = HistorialCita()
rs = Resultados()
al = Alertas()

# Agendar cita
cm.agendar_cita("Ana", "Dr. López", "2025-04-10")

# Registrar diagnóstico
hc.registrar_diagnostico("Ana", "2025-04-10", "Hipertensión")

# Agregar resultados
rs.agregar_resultado("Ana", "glucosa", 115)
rs.agregar_resultado("Ana", "presion", 150)

# Verificar alertas
res = rs.obtener_resultados("Ana")
alertas = al.generar_alertas(res)

print("Diagnóstico:", hc.obtener_diagnostico("Ana", "2025-04-10"))
print("Alertas:", alertas)