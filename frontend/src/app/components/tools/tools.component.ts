import { Component } from '@angular/core';
import { ScraperService } from '../../services/scraper.service';

@Component({
  selector: 'app-tools',
  templateUrl: './tools.component.html',
  styleUrls: ['./tools.component.scss']
})
export class ToolsComponent {
  showGalleryModal = false;
  downloadUrl = '';
  downloadQuality = 'best';
  includeMetadata = false;
  downloading = false;
  downloadResult: any = null;

  constructor(private scraperService: ScraperService) {}

  scrollToSection(sectionId: string) {
    const element = document.getElementById(sectionId);
    if (element) {
      element.scrollIntoView({ behavior: 'smooth' });
    }
  }

  openGalleryTool() {
    this.showGalleryModal = true;
  }

  closeModal() {
    this.showGalleryModal = false;
    this.downloadResult = null;
  }

  startDownload() {
    if (!this.downloadUrl) {
      alert('Por favor, insira uma URL válida');
      return;
    }

    this.downloading = true;
    this.downloadResult = null;

    const request = {
      url: this.downloadUrl,
      quality: this.downloadQuality as any,
      include_metadata: this.includeMetadata
    };

    this.scraperService.startDownload(request).subscribe({
      next: (response) => {
        this.downloadResult = response;
        this.downloading = false;
        
        // Verificar status após 2 segundos
        setTimeout(() => {
          this.checkDownloadStatus(response.job_id);
        }, 2000);
      },
      error: (error) => {
        console.error('Error starting download:', error);
        alert('Erro ao iniciar download: ' + (error.error?.detail || error.message));
        this.downloading = false;
      }
    });
  }

  checkDownloadStatus(jobId: string) {
    this.scraperService.getDownloadStatus(jobId).subscribe({
      next: (status) => {
        this.downloadResult = { ...this.downloadResult, status };
        
        if (status.status === 'processing' || status.status === 'downloading') {
          // Verificar novamente após 3 segundos
          setTimeout(() => this.checkDownloadStatus(jobId), 3000);
        }
      },
      error: (error) => {
        console.error('Error checking status:', error);
      }
    });
  }
}
