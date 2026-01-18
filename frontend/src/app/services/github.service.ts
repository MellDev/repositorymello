import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { ApiConfigService } from './api-config.service';

export interface GitHubRepo {
  id: number;
  name: string;
  full_name: string;
  description: string;
  url: string;
  language: string;
  stars: number;
  forks: number;
  topics: string[];
}

@Injectable({
  providedIn: 'root'
})
export class GithubService {
  private apiUrl: string;

  constructor(
    private http: HttpClient,
    private apiConfig: ApiConfigService
  ) {
    this.apiUrl = `${this.apiConfig.apiUrl}/api/github`;
  }

  getRepos(username?: string): Observable<any> {
    const url = username ? `${this.apiUrl}/repos?username=${username}` : `${this.apiUrl}/repos`;
    return this.http.get(url);
  }

  getRepoDetails(owner: string, repo: string): Observable<any> {
    return this.http.get(`${this.apiUrl}/repos/${owner}/${repo}`);
  }

  getUserStats(username?: string): Observable<any> {
    const url = username ? `${this.apiUrl}/stats?username=${username}` : `${this.apiUrl}/stats`;
    return this.http.get(url);
  }

  getContributions(username?: string): Observable<any> {
    const url = username ? `${this.apiUrl}/contributions?username=${username}` : `${this.apiUrl}/contributions`;
    return this.http.get(url);
  }
}
