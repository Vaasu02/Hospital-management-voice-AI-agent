from pydantic import networks
from database import init_db, Appointment, get_db

init_db()

#Step2: Create FastAPI application and endpoints pseudo code
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
app = FastAPI()

import datetime as dt
from pydantic import BaseModel

class AppointmentRequest(BaseModel):
    patient_name: str
    reason: str
    start_time: dt.datetime

class AppointmentResponse (BaseModel):
    id: int
    patient_name: str
    reason: str | None
    start_time: dt.datetime
    canceled: bool
    created_at: dt.datetime

class CancelAppointmentRequest (BaseModel):
    patient_name: str
    date: dt.date

class CancelAppointmentResponse (BaseModel):
    canceled_count: int
    

@app.post("/schedule_appointment/")
def schedule_appointment(request: AppointmentRequest, db: Session=Depends(get_db)):
    if(request.patient_name==None & request.start_time == None):
        raise HTTPException(status_code=400, detail="patient name and date time is required")
    new_appointment = Appointment(
        patient_name=request.patient_name,
        reason=request.reason,
        start_time=request.start_time,
    )
    db.add(new_appointment)
    db.commit()
    db.refresh(new_appointment)
    new_appointment_return_obj = AppointmentResponse(
        id=new_appointment.id,
        patient_name=new_appointment.patient_name,
        reason=new_appointment.reason,
        start_time=new_appointment.start_time,
        canceled=new_appointment.canceled,
        created_at=new_appointment.created_at
    )
    return new_appointment_return_obj
    