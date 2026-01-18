import { Component } from '@angular/core';
import { TranslationService, Language } from '../../services/translation.service';
import { ThemeService, Theme } from '../../services/theme.service';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.scss']
})
export class NavbarComponent {
  isMenuOpen = false;
  currentLanguage: Language = 'pt';
  currentTheme: Theme = 'dark';

  constructor(
    private translationService: TranslationService,
    private themeService: ThemeService
  ) {
    this.currentLanguage = this.translationService.getCurrentLanguage();
    this.translationService.language$.subscribe(lang => {
      this.currentLanguage = lang;
    });

    this.currentTheme = this.themeService.getCurrentTheme();
    this.themeService.theme$.subscribe(theme => {
      this.currentTheme = theme;
    });
  }

  toggleMenu() {
    this.isMenuOpen = !this.isMenuOpen;
  }

  scrollToSection(sectionId: string) {
    const element = document.getElementById(sectionId);
    if (element) {
      element.scrollIntoView({ behavior: 'smooth' });
      this.isMenuOpen = false;
    }
  }

  changeLanguage(lang: Language) {
    this.translationService.setLanguage(lang);
  }

  toggleTheme() {
    this.themeService.toggleTheme();
  }
}
