from github import Github
from github.GithubException import GithubException
import logging
from typing import Optional

from app.config import settings

logger = logging.getLogger(__name__)


class GitHubService:
    def __init__(self):
        self.username = settings.github_username
        if settings.github_token:
            self.client = Github(settings.github_token)
        else:
            self.client = Github()  # Sem autenticação (rate limit menor)
            logger.warning("GitHub token not configured - using unauthenticated access")

    async def get_user_repos(self, username: Optional[str] = None) -> dict:
        """Retorna repositórios do usuário"""
        try:
            user = self.client.get_user(username or self.username)
            repos = []

            for repo in user.get_repos(sort='updated'):
                repos.append({
                    "id": repo.id,
                    "name": repo.name,
                    "full_name": repo.full_name,
                    "description": repo.description,
                    "url": repo.html_url,
                    "homepage": repo.homepage,
                    "language": repo.language,
                    "stars": repo.stargazers_count,
                    "forks": repo.forks_count,
                    "watchers": repo.watchers_count,
                    "open_issues": repo.open_issues_count,
                    "created_at": repo.created_at.isoformat() if repo.created_at else None,
                    "updated_at": repo.updated_at.isoformat() if repo.updated_at else None,
                    "topics": repo.get_topics(),
                    "is_private": repo.private,
                    "is_fork": repo.fork
                })

            return {
                "username": username or self.username,
                "repos": repos,
                "count": len(repos)
            }

        except GithubException as e:
            logger.error(f"GitHub API error: {e}")
            raise
        except Exception as e:
            logger.error(f"Error getting repos: {e}")
            raise

    async def get_repo_details(self, owner: str, repo_name: str) -> dict:
        """Retorna detalhes de um repositório"""
        try:
            repo = self.client.get_repo(f"{owner}/{repo_name}")

            # Buscar linguagens
            languages = repo.get_languages()

            # Buscar contributors
            contributors = []
            for contrib in repo.get_contributors()[:10]:
                contributors.append({
                    "login": contrib.login,
                    "contributions": contrib.contributions,
                    "avatar_url": contrib.avatar_url
                })

            return {
                "repository": {
                    "id": repo.id,
                    "name": repo.name,
                    "full_name": repo.full_name,
                    "description": repo.description,
                    "url": repo.html_url,
                    "language": repo.language,
                    "languages": languages,
                    "stars": repo.stargazers_count,
                    "forks": repo.forks_count,
                    "watchers": repo.watchers_count,
                    "open_issues": repo.open_issues_count,
                    "topics": repo.get_topics(),
                    "contributors": contributors,
                    "created_at": repo.created_at.isoformat() if repo.created_at else None,
                    "updated_at": repo.updated_at.isoformat() if repo.updated_at else None
                }
            }

        except GithubException as e:
            logger.error(f"GitHub API error: {e}")
            raise
        except Exception as e:
            logger.error(f"Error getting repo details: {e}")
            raise

    async def get_user_stats(self, username: Optional[str] = None) -> dict:
        """Retorna estatísticas do usuário"""
        try:
            user = self.client.get_user(username or self.username)
            repos = list(user.get_repos())

            # Calcular estatísticas
            total_stars = sum(repo.stargazers_count for repo in repos)
            total_forks = sum(repo.forks_count for repo in repos)

            # Linguagens dos top repos
            languages = {}
            for repo in sorted(repos, key=lambda r: r.stargazers_count, reverse=True)[:10]:
                for lang, bytes_count in repo.get_languages().items():
                    languages[lang] = languages.get(lang, 0) + bytes_count

            return {
                "user": {
                    "username": user.login,
                    "name": user.name,
                    "avatar": user.avatar_url,
                    "bio": user.bio,
                    "company": user.company,
                    "location": user.location,
                    "email": user.email,
                    "blog": user.blog,
                    "public_repos": user.public_repos,
                    "public_gists": user.public_gists,
                    "followers": user.followers,
                    "following": user.following,
                    "created_at": user.created_at.isoformat() if user.created_at else None
                },
                "stats": {
                    "total_stars": total_stars,
                    "total_forks": total_forks,
                    "total_repos": len(repos),
                    "languages": languages
                }
            }

        except GithubException as e:
            logger.error(f"GitHub API error: {e}")
            raise
        except Exception as e:
            logger.error(f"Error getting user stats: {e}")
            raise

    async def get_contributions(self, username: Optional[str] = None) -> dict:
        """Retorna contribuições do usuário"""
        try:
            user = self.client.get_user(username or self.username)
            events = list(user.get_events()[:100])

            contribution_types = {}
            for event in events:
                contribution_types[event.type] = contribution_types.get(event.type, 0) + 1

            recent_activity = []
            for event in events[:10]:
                recent_activity.append({
                    "type": event.type,
                    "repo": event.repo.name,
                    "created_at": event.created_at.isoformat() if event.created_at else None
                })

            return {
                "username": username or self.username,
                "recent_activity": recent_activity,
                "contribution_types": contribution_types,
                "total_events": len(events)
            }

        except GithubException as e:
            logger.error(f"GitHub API error: {e}")
            raise
        except Exception as e:
            logger.error(f"Error getting contributions: {e}")
            raise
