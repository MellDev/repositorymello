import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { ChatService, ChatMessage } from '../../services/chat.service';

@Component({
  selector: 'app-chat',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './chat.component.html',
  styleUrls: ['./chat.component.scss']
})
export class ChatComponent implements OnInit {
  isOpen = false;
  isMinimized = false;
  message = '';
  messages: ChatMessage[] = [];
  isTyping = false;
  messagesRemaining = 3;
  limitReached = false;

  constructor(private chatService: ChatService) {}

  ngOnInit() {
    // Load conversation history from localStorage
    this.messages = this.chatService.getConversationHistory();
  }

  toggleChat() {
    this.isOpen = !this.isOpen;
    if (this.isOpen) {
      this.isMinimized = false;
      setTimeout(() => this.scrollToBottom(), 100);
    }
  }

  minimizeChat() {
    this.isMinimized = !this.isMinimized;
  }

  closeChat() {
    this.isOpen = false;
  }

  async sendMessage() {
    if (!this.message.trim() || this.limitReached) return;

    const userMessage: ChatMessage = {
      role: 'user',
      content: this.message
    };

    this.messages.push(userMessage);
    this.chatService.addMessage(userMessage);
    this.message = '';
    this.isTyping = true;
    this.scrollToBottom();

    try {
      const response = await this.chatService.sendMessage(
        userMessage.content,
        this.messages.slice(0, -1) // Exclude the just-added user message
      ).toPromise();

      if (response) {
        const assistantMessage: ChatMessage = {
          role: 'assistant',
          content: response.response
        };

        this.messages.push(assistantMessage);
        this.chatService.addMessage(assistantMessage);
        this.messagesRemaining = response.messages_remaining;
        this.limitReached = response.limit_reached;
      }
    } catch (error) {
      console.error('Error sending message:', error);
      const errorMessage: ChatMessage = {
        role: 'assistant',
        content: 'Desculpe, ocorreu um erro. Por favor, tente novamente.'
      };
      this.messages.push(errorMessage);
    } finally {
      this.isTyping = false;
      this.scrollToBottom();
    }
  }

  resetSession() {
    this.chatService.resetSession();
    this.chatService.clearHistory();
    this.messages = [];
    this.messagesRemaining = 3;
    this.limitReached = false;
  }

  private scrollToBottom() {
    setTimeout(() => {
      const messagesContainer = document.querySelector('.chat-messages');
      if (messagesContainer) {
        messagesContainer.scrollTop = messagesContainer.scrollHeight;
      }
    }, 100);
  }
}
