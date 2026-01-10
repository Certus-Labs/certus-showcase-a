# Contributing to Showcase-A-Batch

Thank you for your interest! 🎉

## Development Setup

1. **Prerequisites**: Python 3.12+, [uv](https://github.com/astral-sh/uv)
2. **Setup**: Run `./scripts/setup_env.sh` or `make dev`
3. **Activate venv**: `source .venv/bin/activate`

## Code Standards

### Linting & Formatting

- **Linter**: `ruff check src/ tests/`
- **Formatter**: `ruff format src/ tests/`
- **Auto-fix**: `ruff check --fix src/ tests/`

All code must pass `ruff check` before commit.

### Testing

- **Run all tests**: `make test`
- **Unit tests only**: `make test-unit`
- **With coverage**: `make test-coverage`

Target: 80%+ code coverage for `src/`.

### Commit Messages

Use clear, descriptive messages:

```txt
Add: DVF data loader with schema validation
Fix: API rate limit handling in enrichment
Update: Quality check framework with new validators
```

## Pull Request Process

1. **Create branch**: `git checkout -b feature/your-feature`
2. **Make changes**: Follow code standards
3. **Run checks**: `make lint && make format && make test`
4. **Commit**: Clear commit messages
5. **Submit PR**: Describe what changed and why

## Questions?

Open an issue or contact the maintainers.

---

Thank you for contributing! 🙌
