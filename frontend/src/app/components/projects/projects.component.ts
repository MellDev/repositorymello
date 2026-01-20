import { Component, OnInit } from '@angular/core';
import { ProjectService, Project } from '../../services/project.service';

@Component({
  selector: 'app-projects',
  templateUrl: './projects.component.html',
  styleUrls: ['./projects.component.scss']
})
export class ProjectsComponent implements OnInit {
  projects: any[] = [];
  loading = true;
  error: string | null = null;

  constructor(private projectService: ProjectService) {}

  ngOnInit() {
    this.loadProjects();
  }

  loadProjects() {
    this.loading = true;
    console.log('Loading projects...');
    this.projectService.getProjects().subscribe({
      next: (response) => {
        console.log('Projects loaded successfully:', response);
        this.projects = response.projects;
        this.loading = false;
      },
      error: (error) => {
        console.error('Error loading projects:', error);
        console.error('Error details:', {
          message: error.message,
          status: error.status,
          statusText: error.statusText,
          url: error.url
        });
        this.error = 'Erro ao carregar projetos';
        this.loading = false;
      }
    });
  }

  getIcon(category: string): string {
    const icons: any = {
      'web': 'fa-globe',
      'automation': 'fa-robot',
      'ai': 'fa-brain',
      'mobile': 'fa-mobile-alt'
    };
    return icons[category] || 'fa-code';
  }

  scrollToContact(event: Event) {
    event.preventDefault();
    const contactSection = document.getElementById('contact');
    if (contactSection) {
      contactSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  }
}
