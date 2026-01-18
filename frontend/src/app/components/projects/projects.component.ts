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
    this.projectService.getProjects().subscribe({
      next: (response) => {
        this.projects = response.projects;
        this.loading = false;
      },
      error: (error) => {
        console.error('Error loading projects:', error);
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
}
