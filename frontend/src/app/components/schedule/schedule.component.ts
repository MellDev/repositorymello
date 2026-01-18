import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { CalendarService } from '../../services/calendar.service';

@Component({
  selector: 'app-schedule',
  templateUrl: './schedule.component.html',
  styleUrls: ['./schedule.component.scss']
})
export class ScheduleComponent implements OnInit {
  appointmentForm: FormGroup;
  availableSlots: string[] = [];
  loadingSlots = false;
  submitting = false;
  minDate: string;

  constructor(
    private fb: FormBuilder,
    private calendarService: CalendarService
  ) {
    const today = new Date();
    this.minDate = today.toISOString().split('T')[0];

    this.appointmentForm = this.fb.group({
      name: ['', [Validators.required]],
      email: ['', [Validators.required, Validators.email]],
      phone: ['', [Validators.required]],
      service: ['', [Validators.required]],
      date: ['', [Validators.required]],
      time: ['', [Validators.required]],
      message: ['']
    });
  }

  ngOnInit() {
    // Carregar slots quando a data mudar
    this.appointmentForm.get('date')?.valueChanges.subscribe(date => {
      if (date) {
        this.loadAvailableSlots(date);
      }
    });
  }

  loadAvailableSlots(date: string) {
    this.loadingSlots = true;
    this.availableSlots = [];
    this.appointmentForm.patchValue({ time: '' });

    this.calendarService.getAvailableSlots(date).subscribe({
      next: (response) => {
        this.availableSlots = response.available_slots;
        this.loadingSlots = false;
      },
      error: (error) => {
        console.error('Error loading slots:', error);
        this.loadingSlots = false;
        alert('Erro ao carregar horários disponíveis');
      }
    });
  }

  onSubmit() {
    if (this.appointmentForm.invalid) {
      alert('Por favor, preencha todos os campos obrigatórios');
      return;
    }

    this.submitting = true;
    const appointment = this.appointmentForm.value;

    this.calendarService.createAppointment(appointment).subscribe({
      next: (response) => {
        alert('✅ Agendamento realizado com sucesso! Você receberá uma confirmação por email.');
        this.appointmentForm.reset();
        this.submitting = false;
      },
      error: (error) => {
        console.error('Error creating appointment:', error);
        alert('❌ Erro ao criar agendamento: ' + (error.error?.detail || error.message));
        this.submitting = false;
      }
    });
  }
}
