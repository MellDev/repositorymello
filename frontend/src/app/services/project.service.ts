import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { ApiConfigService } from './api-config.service';

export interface Project {
  id: string;
  name: string;
  description: string;
  technologies: string[];
  status: string;
  category: string;
}

@Injectable({
  providedIn: 'root'
})
export class ProjectService {
  private apiUrl: string;

  constructor(
    private http: HttpClient,
    private apiConfig: ApiConfigService
  ) {
    this.apiUrl = `${this.apiConfig.apiUrl}/projects/`;
  }

  getProjects(category?: string, status?: string, limit?: number): Observable<any> {
    let url = this.apiUrl;
    const params: string[] = [];
    
    if (category) params.push(`category=${category}`);
    if (status) params.push(`status=${status}`);
    if (limit) params.push(`limit=${limit}`);
    
    if (params.length > 0) {
      url += '?' + params.join('&');
    }
    
    console.log('Fetching projects from:', url);
    return this.http.get(url);
  }

  getProjectById(id: string): Observable<any> {
    return this.http.get(`${this.apiUrl}/${id}`);
  }
}
