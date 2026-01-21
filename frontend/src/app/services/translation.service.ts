import { Injectable } from '@angular/core';
import { BehaviorSubject, Observable } from 'rxjs';

export type Language = 'pt' | 'en' | 'es';

@Injectable({
  providedIn: 'root'
})
export class TranslationService {
  private currentLanguage = new BehaviorSubject<Language>('pt');
  public language$: Observable<Language> = this.currentLanguage.asObservable();

  private translations: Record<Language, any> = {
    pt: {
      // Navbar
      nav: {
        home: 'Home',
        projects: 'Projetos',
        tools: 'Ferramentas',
        schedule: 'Agendar',
        contact: 'Contato'
      },
      // Hero
      hero: {
        title: 'Anderson Mello',
        subtitle: 'Data Engineer & Software Engineer',
        description: 'Transformando dados em soluções inteligentes | Desenvolvimento web moderno, automações e integrações com IA',
        btnProjects: 'Ver Projetos',
        btnSchedule: 'Agendar Reunião',
        btnResume: 'Baixar Currículo'
      },
      // Projects
      projects: {
        title: 'Projetos',
        description: 'Confira alguns dos meus trabalhos recentes',
        contact: 'Entrar em Contato',
        loading: 'Carregando projetos...',
        error: 'Erro ao carregar projetos'
      },
      // Tools
      tools: {
        title: 'Ferramentas',
        description: 'Utilitários para facilitar seu dia a dia',
        tryIt: 'Experimentar',
        viewProjects: 'Ver Projetos',
        gallery: {
          title: 'Gallery Downloader',
          description: 'Baixe mídias de diversas plataformas com facilidade'
        },
        schedule: {
          title: 'Sistema de Agendamento',
          description: 'Demonstração do sistema de agendamento com Google Calendar'
        },
        github: {
          title: 'GitHub Integration',
          description: 'Veja meus repositórios e estatísticas do GitHub'
        },
        scraper: {
          title: 'Scraper de Mídia',
          description: 'Baixe vídeos e imagens de diversas plataformas',
          placeholder: 'https://exemplo.com/media',
          btnDownload: 'Baixar Mídia',
          downloading: 'Baixando...',
          success: 'Download iniciado com sucesso!',
          error: 'Erro ao baixar mídia'
        }
      },
      // Schedule
      schedule: {
        title: 'Agendar Reunião',
        description: 'Escolha um horário disponível para conversarmos',
        form: {
          name: 'Nome',
          email: 'Email',
          date: 'Data',
          time: 'Horário',
          message: 'Mensagem (opcional)',
          btnSubmit: 'Agendar',
          submitting: 'Agendando...'
        },
        success: 'Reunião agendada com sucesso!',
        error: 'Erro ao agendar reunião',
        validation: 'Por favor, preencha todos os campos obrigatórios'
      },
      // Contact
      contact: {
        title: 'Entre em Contato',
        description: 'Vamos trabalhar juntos? Entre em contato comigo',
        info: {
          email: 'Email',
          whatsapp: 'WhatsApp',
          github: 'GitHub',
          linkedin: 'LinkedIn'
        },
        cta: {
          title: 'Pronto para começar?',
          description: 'Entre em contato agora mesmo e vamos discutir seu projeto!',
          button: 'Enviar Email'
        }
      },
      // Footer
      footer: {
        rights: 'Todos os direitos reservados.'
      }
    },
    en: {
      // Navbar
      nav: {
        home: 'Home',
        projects: 'Projects',
        tools: 'Tools',
        schedule: 'Schedule',
        contact: 'Contact'
      },
      // Hero
      hero: {
        title: 'Anderson Mello',
        subtitle: 'Data Engineer & Software Engineer',
        description: 'Transforming data into intelligent solutions | Modern web development, automation and AI integrations',
        btnProjects: 'View Projects',
        btnSchedule: 'Schedule Meeting',
        btnResume: 'Download Resume'
      },
      // Projects
      projects: {
        title: 'Projects',
        description: 'Check out some of my recent work',
        contact: 'Get in Touch',
        loading: 'Loading projects...',
        error: 'Error loading projects'
      },
      // Tools
      tools: {
        title: 'Tools',
        description: 'Utilities to make your day easier',
        tryIt: 'Try it',
        viewProjects: 'View Projects',
        gallery: {
          title: 'Gallery Downloader',
          description: 'Download media from multiple platforms with ease'
        },
        schedule: {
          title: 'Scheduling System',
          description: 'Scheduling system demonstration with Google Calendar'
        },
        github: {
          title: 'GitHub Integration',
          description: 'View my repositories and GitHub statistics'
        },
        scraper: {
          title: 'Media Scraper',
          description: 'Download videos and images from various platforms',
          placeholder: 'https://example.com/media',
          btnDownload: 'Download Media',
          downloading: 'Downloading...',
          success: 'Download started successfully!',
          error: 'Error downloading media'
        }
      },
      // Schedule
      schedule: {
        title: 'Schedule Meeting',
        description: 'Choose an available time to talk',
        form: {
          name: 'Name',
          email: 'Email',
          date: 'Date',
          time: 'Time',
          message: 'Message (optional)',
          btnSubmit: 'Schedule',
          submitting: 'Scheduling...'
        },
        success: 'Meeting scheduled successfully!',
        error: 'Error scheduling meeting',
        validation: 'Please fill in all required fields'
      },
      // Contact
      contact: {
        title: 'Get in Touch',
        description: "Let's work together? Contact me",
        info: {
          email: 'Email',
          whatsapp: 'WhatsApp',
          github: 'GitHub',
          linkedin: 'LinkedIn'
        },
        cta: {
          title: 'Ready to start?',
          description: 'Get in touch now and let\'s discuss your project!',
          button: 'Send Email'
        }
      },
      // Footer
      footer: {
        rights: 'All rights reserved.'
      }
    },
    es: {
      // Navbar
      nav: {
        home: 'Inicio',
        projects: 'Proyectos',
        tools: 'Herramientas',
        schedule: 'Agendar',
        contact: 'Contacto'
      },
      // Hero
      hero: {
        title: 'Anderson Mello',
        subtitle: 'Data Engineer & Software Engineer',
        description: 'Transformando datos en soluciones inteligentes | Desarrollo web moderno, automatizaciones e integraciones con IA',
        btnProjects: 'Ver Proyectos',
        btnSchedule: 'Agendar Reunión',
        btnResume: 'Descargar CV'
      },
      // Projects
      projects: {
        title: 'Proyectos',
        description: 'Vea algunos de mis trabajos recientes',
        contact: 'Contactar',
        loading: 'Cargando proyectos...',
        error: 'Error al cargar proyectos'
      },
      // Tools
      tools: {
        title: 'Herramientas',
        description: 'Utilidades para facilitar tu día a día',
        tryIt: 'Probar',
        viewProjects: 'Ver Proyectos',
        gallery: {
          title: 'Gallery Downloader',
          description: 'Descarga medios de varias plataformas con facilidad'
        },
        schedule: {
          title: 'Sistema de Agendamiento',
          description: 'Demostración del sistema de agendamiento con Google Calendar'
        },
        github: {
          title: 'GitHub Integration',
          description: 'Ve mis repositorios y estadísticas de GitHub'
        },
        scraper: {
          title: 'Scraper de Medios',
          description: 'Descarga videos e imágenes de varias plataformas',
          placeholder: 'https://ejemplo.com/media',
          btnDownload: 'Descargar Media',
          downloading: 'Descargando...',
          success: '¡Descarga iniciada con éxito!',
          error: 'Error al descargar media'
        }
      },
      // Schedule
      schedule: {
        title: 'Agendar Reunión',
        description: 'Elige un horario disponible para conversar',
        form: {
          name: 'Nombre',
          email: 'Email',
          date: 'Fecha',
          time: 'Horario',
          message: 'Mensaje (opcional)',
          btnSubmit: 'Agendar',
          submitting: 'Agendando...'
        },
        success: '¡Reunión agendada con éxito!',
        error: 'Error al agendar reunión',
        validation: 'Por favor, complete todos los campos requeridos'
      },
      // Contact
      contact: {
        title: 'Ponte en Contacto',
        description: '¿Trabajamos juntos? Contáctame',
        info: {
          email: 'Email',
          whatsapp: 'WhatsApp',
          github: 'GitHub',
          linkedin: 'LinkedIn'
        },
        cta: {
          title: '¿Listo para empezar?',
          description: '¡Ponte en contacto ahora y discutamos tu proyecto!',
          button: 'Enviar Email'
        }
      },
      // Footer
      footer: {
        rights: 'Todos los derechos reservados.'
      }
    }
  };

  constructor() {
    // Carregar idioma salvo ou usar navegador
    const savedLang = localStorage.getItem('language') as Language;
    const browserLang = navigator.language.split('-')[0] as Language;
    const defaultLang = savedLang || (this.isValidLanguage(browserLang) ? browserLang : 'pt');
    this.setLanguage(defaultLang);
  }

  private isValidLanguage(lang: string): lang is Language {
    return ['pt', 'en', 'es'].includes(lang);
  }

  setLanguage(lang: Language): void {
    this.currentLanguage.next(lang);
    localStorage.setItem('language', lang);
  }

  getCurrentLanguage(): Language {
    return this.currentLanguage.value;
  }

  translate(key: string): string {
    const lang = this.currentLanguage.value;
    const keys = key.split('.');
    let value: any = this.translations[lang];
    
    for (const k of keys) {
      value = value?.[k];
    }
    
    return value || key;
  }

  t(key: string): string {
    return this.translate(key);
  }
}
