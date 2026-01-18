import { Component } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { ContactService } from '../../services/contact.service';

@Component({
  selector: 'app-contact',
  templateUrl: './contact.component.html',
  styleUrls: ['./contact.component.scss']
})
export class ContactComponent {
  contactForm: FormGroup;
  submitting = false;

  constructor(
    private fb: FormBuilder,
    private contactService: ContactService
  ) {
    this.contactForm = this.fb.group({
      name: ['', [Validators.required]],
      email: ['', [Validators.required, Validators.email]],
      phone: [''],
      subject: [''],
      message: ['', [Validators.required]]
    });
  }

  onSubmit() {
    if (this.contactForm.invalid) {
      alert('Por favor, preencha todos os campos obrigatórios');
      return;
    }

    this.submitting = true;
    const message = this.contactForm.value;

    this.contactService.sendMessage(message).subscribe({
      next: (response) => {
        alert('✅ Mensagem enviada com sucesso! Entrarei em contato em breve.');
        this.contactForm.reset();
        this.submitting = false;
      },
      error: (error) => {
        console.error('Error sending message:', error);
        alert('❌ Erro ao enviar mensagem: ' + (error.error?.detail || error.message));
        this.submitting = false;
      }
    });
  }
}
