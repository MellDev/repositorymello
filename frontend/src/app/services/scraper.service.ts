import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { ApiConfigService } from './api-config.service';

export interface DownloadRequest {
  url: string;
  quality: 'best' | '1080p' | '720p' | '480p';
  include_metadata: boolean;
}

@Injectable({
  providedIn: 'root'
})
export class ScraperService {
  private apiUrl: string;

  constructor(
    private http: HttpClient,
    private apiConfig: ApiConfigService
  ) {
    this.apiUrl = `${this.apiConfig.apiUrl}/api/scraper`;
  }

  startDownload(request: DownloadRequest): Observable<any> {
    return this.http.post(`${this.apiUrl}/download`, request);
  }

  getDownloadStatus(jobId: string): Observable<any> {
    return this.http.get(`${this.apiUrl}/status/${jobId}`);
  }

  getSupportedPlatforms(): Observable<any> {
    return this.http.get(`${this.apiUrl}/platforms`);
  }
}
