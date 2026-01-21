import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from '../../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class ResumeService {
  private apiUrl = environment.apiUrl;

  constructor(private http: HttpClient) {}

  downloadResume(): void {
    const url = `${this.apiUrl}/api/resume/download`;
    window.open(url, '_blank');
  }

  viewResume(): void {
    const url = `${this.apiUrl}/api/resume/view`;
    window.open(url, '_blank');
  }
}
