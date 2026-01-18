import { Injectable } from '@angular/core';
import { environment } from '../../environments/environment';

export interface ApiConfig {
  baseUrl: string;
}

@Injectable({
  providedIn: 'root'
})
export class ApiConfigService {
  private config: ApiConfig = {
    baseUrl: environment.apiUrl
  };

  get apiUrl(): string {
    return this.config.baseUrl;
  }

  setBaseUrl(url: string): void {
    this.config.baseUrl = url;
  }
}
