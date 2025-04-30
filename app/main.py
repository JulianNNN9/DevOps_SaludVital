from fastapi import FastAPI, HTTPException
from app.cita_manager import CitaManager
from app.historial_cita import HistorialCita
from app.resultados import Resultados
from app.alertas import Alertas

app = FastAPI(title="VitalApp API")

# Crear instancias
cm = CitaManager()
hc = HistorialCita()
rs = Resultados()
al = Alertas()

@app.get("/")
def read_root():
    return {"status": "active", "message": "VitalApp API is running"}

@app.post("/citas")
def crear_cita(paciente: str, medico: str, fecha: str):
    try:
        cm.agendar_cita(paciente, medico, fecha)
        return {"message": "Cita creada exitosamente"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/diagnosticos/{paciente}/{fecha}")
def obtener_diagnostico(paciente: str, fecha: str):
    try:
        diagnostico = hc.obtener_diagnostico(paciente, fecha)
        return {"diagnostico": diagnostico}
    except Exception as e:
        raise HTTPException(status_code=404, detail="Diagnóstico no encontrado")

@app.get("/alertas/{paciente}")
def obtener_alertas(paciente: str):
    try:
        res = rs.obtener_resultados(paciente)
        alertas = al.generar_alertas(res)
        return {"alertas": alertas}
    except Exception as e:
        raise HTTPException(status_code=404, detail="No se encontraron alertas")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=10000)