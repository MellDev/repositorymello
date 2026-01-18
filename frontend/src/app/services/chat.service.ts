import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from '../../environments/environment';

export interface ChatMessage {
  role: 'user' | 'assistant';
  content: string;
}

export interface ChatResponse {
  response: string;
  session_id: string;
  messages_remaining: number;
  limit_reached: boolean;
}

@Injectable({
  providedIn: 'root'
})
export class ChatService {
  private apiUrl = `${environment.apiUrl}/chat`;
  private sessionId: string;

  constructor(private http: HttpClient) {
    this.sessionId = this.getOrCreateSessionId();
  }

  private getOrCreateSessionId(): string {
    let sessionId = localStorage.getItem('chat_session_id');
    if (!sessionId) {
      sessionId = this.generateSessionId();
      localStorage.setItem('chat_session_id', sessionId);
    }
    return sessionId;
  }

  private generateSessionId(): string {
    return `session_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`;
  }

  sendMessage(message: string, conversationHistory: ChatMessage[]): Observable<ChatResponse> {
    return this.http.post<ChatResponse>(this.apiUrl, {
      message,
      session_id: this.sessionId,
      conversation_history: conversationHistory
    });
  }

  getSessionStatus(): Observable<any> {
    return this.http.get(`${this.apiUrl}/status/${this.sessionId}`);
  }

  resetSession(): void {
    this.sessionId = this.generateSessionId();
    localStorage.setItem('chat_session_id', this.sessionId);
    localStorage.removeItem('chat_history');
  }

  getConversationHistory(): ChatMessage[] {
    const history = localStorage.getItem('chat_history');
    return history ? JSON.parse(history) : [];
  }

  saveConversationHistory(history: ChatMessage[]): void {
    localStorage.setItem('chat_history', JSON.stringify(history));
  }

  addMessage(message: ChatMessage): void {
    const history = this.getConversationHistory();
    history.push(message);
    this.saveConversationHistory(history);
  }

  clearHistory(): void {
    localStorage.removeItem('chat_history');
  }
}
