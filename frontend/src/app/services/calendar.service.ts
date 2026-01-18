import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs';
import { ApiConfigService } from './api-config.service';

export interface AvailableSlot {
  date: string;
  available_slots: string[];
  duration: number;
  timezone: string;
}

export interface Appointment {
  name: string;
  email: string;
  phone: string;
  service: string;
  date: string;
  time: string;
  message?: string;
}

@Injectable({
  providedIn: 'root'
})
export class CalendarService {
  private apiUrl: string;

  constructor(
    private http: HttpClient,
    private apiConfig: ApiConfigService
  ) {
    this.apiUrl = `${this.apiConfig.apiUrl}/api/calendar`;
  }

  getAvailableSlots(date: string, duration: number = 60): Observable<AvailableSlot> {
    const params = new HttpParams()
      .set('date', date)
      .set('duration', duration.toString());
    
    return this.http.get<AvailableSlot>(`${this.apiUrl}/available-slots`, { params });
  }

  createAppointment(appointment: Appointment): Observable<any> {
    return this.http.post(`${this.apiUrl}/appointments`, appointment);
  }

  getAppointments(startDate?: string, endDate?: string): Observable<any> {
    let params = new HttpParams();
    if (startDate) params = params.set('start_date', startDate);
    if (endDate) params = params.set('end_date', endDate);
    
    return this.http.get(`${this.apiUrl}/appointments`, { params });
  }

  cancelAppointment(eventId: string): Observable<any> {
    return this.http.delete(`${this.apiUrl}/appointments/${eventId}`);
  }
}
