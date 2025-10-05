# Template Versioning Strategy

## Overview

This document defines the versioning strategy for templates in the unified workflow system, ensuring consistent template management, compatibility, and evolution across all template packs.

## Template Structure

### Manifest Format
Each template must include a `template.manifest.json` file with the following structure:

```json
{
  "name": "template-name",
  "type": "frontend|backend|database|devex|cicd|policy-dsl",
  "version": "1.0.0",
  "variants": ["base", "advanced", "minimal"],
  "engines": {
    "node": ">=18",
    "python": ">=3.8"
  },
  "dependencies": {
    "external": ["react", "nextjs"],
    "internal": ["common-utils"]
  },
  "compatibility": {
    "unified-workflow": ">=1.0.0",
    "project-generator": ">=2.0.0"
  },
  "metadata": {
    "author": "Template Author",
    "description": "Brief description",
    "tags": ["react", "typescript", "production-ready"]
  }
}
```

## Versioning Scheme

### Semantic Versioning (SemVer)
Templates follow [Semantic Versioning 2.0.0](https://semver.org/) principles:

- **MAJOR** (X.y.z): Breaking changes that require code modifications
- **MINOR** (x.Y.z): New features that are backward compatible
- **PATCH** (x.y.Z): Bug fixes that don't change functionality

### Version Components
- **X (Major)**: Breaking changes in template structure, dependencies, or output
- **Y (Minor)**: New template variants, optional features, or configuration options
- **Z (Patch)**: Bug fixes, security updates, or minor improvements

## Template Types and Categories

### Core Types
1. **frontend**: React, Vue, Angular, Next.js, Nuxt.js applications
2. **backend**: FastAPI, Django, NestJS, Go, Node.js services
3. **database**: PostgreSQL, MongoDB, Firebase, Redis configurations
4. **devex**: Development tooling, linting, formatting configurations
5. **cicd**: CI/CD pipelines, deployment configurations
6. **policy-dsl**: Security policies, compliance rules, governance

### Variant Classification
- **base**: Minimal, essential template with core functionality
- **advanced**: Full-featured template with additional capabilities
- **minimal**: Stripped-down version for specific use cases
- **enterprise**: Production-ready with advanced security and monitoring

## Version Compatibility Matrix

### Unified Workflow Compatibility
Templates must specify compatible unified-workflow versions:

```json
{
  "compatibility": {
    "unified-workflow": ">=1.0.0",
    "project-generator": ">=2.0.0"
  }
}
```

### Template Dependencies
Templates can depend on other templates:

```json
{
  "dependencies": {
    "internal": ["common-frontend-components", "shared-backend-utils"],
    "external": ["react@^18.0.0", "typescript@^4.9.0"]
  }
}
```

## Template Registry Integration

### Discovery Process
1. **Scan**: Recursively scan `template-packs/` for `template.manifest.json` files
2. **Validate**: Check manifest format and required fields
3. **Register**: Add valid templates to registry with metadata
4. **Index**: Create searchable index by type, name, and tags

### Template Selection Algorithm
```
Priority Order:
1. Exact version match (if specified)
2. Latest compatible version
3. Fallback to base variant
4. Error if no compatible template found
```

## Version Management Workflow

### Template Development
1. **Create**: New template with initial version 0.1.0
2. **Develop**: Increment patch versions for fixes (0.1.1, 0.1.2)
3. **Feature**: Increment minor version for new features (0.2.0)
4. **Release**: Increment major version for breaking changes (1.0.0)

### Template Updates
1. **Patch Updates**: Bug fixes, security patches
2. **Minor Updates**: New features, performance improvements
3. **Major Updates**: Breaking changes, architecture updates

### Deprecation Process
1. **Announce**: Mark template as deprecated in manifest
2. **Migrate**: Provide migration guide for users
3. **Support**: Maintain for 6 months after deprecation
4. **Remove**: Remove from registry after support period

## Quality Assurance

### Validation Gates
- **Manifest Validation**: JSON schema compliance
- **Dependency Check**: All dependencies resolve correctly
- **Integration Test**: Template generates valid projects
- **Performance Test**: Generation completes within time limits

### Template Testing
```bash
# Validate template manifest
python scripts/validate_template_manifest.py --template path/to/template

# Test template generation
python scripts/test_template_generation.py --template frontend/nextjs --output /tmp/test

# Performance benchmark
python scripts/benchmark_template_generation.py --template backend/fastapi
```

## Migration Strategy

### Version Upgrades
1. **Identify Impact**: Analyze breaking changes
2. **Update Dependencies**: Modify dependent templates
3. **Test Compatibility**: Validate all integrations
4. **Deploy**: Roll out updated templates

### Rollback Procedures
1. **Identify Issue**: Determine root cause
2. **Revert Version**: Roll back to previous version
3. **Fix Forward**: Address issue in development
4. **Redeploy**: Deploy corrected version

## Monitoring and Analytics

### Template Usage Metrics
- **Download Count**: Track template popularity
- **Success Rate**: Monitor generation success/failure
- **Performance**: Track generation time and resource usage
- **Error Rates**: Monitor template-specific errors

### Version Adoption
- **Usage by Version**: Track which versions are most used
- **Migration Patterns**: Monitor upgrade patterns
- **Deprecated Usage**: Track usage of deprecated templates

## Best Practices

### Template Authors
1. **Semantic Versioning**: Follow SemVer strictly
2. **Clear Documentation**: Document all changes and migrations
3. **Backward Compatibility**: Maintain compatibility where possible
4. **Testing**: Include comprehensive tests for all variants

### Template Consumers
1. **Pin Versions**: Specify exact versions when possible
2. **Test Updates**: Validate templates before production use
3. **Monitor Changes**: Stay informed about template updates
4. **Report Issues**: Provide feedback for template improvements

## Examples

### Version Evolution
```
v0.1.0: Initial template release
v0.1.1: Fix security vulnerability
v0.2.0: Add TypeScript support
v1.0.0: Complete rewrite with new architecture
v1.1.0: Add GraphQL API support
v1.1.1: Performance optimizations
v2.0.0: Breaking change to configuration format
```

### Template Selection
```json
{
  "template": "frontend/nextjs",
  "version": ">=1.0.0",
  "variant": "base",
  "engines": {
    "node": ">=18"
  }
}
```

## Support and Maintenance

### Long-term Support (LTS)
- **LTS Versions**: Maintain for 12 months
- **Security Updates**: Provide security patches
- **Bug Fixes**: Address critical bugs
- **Documentation**: Keep documentation current

### Community Contributions
- **Contribution Guidelines**: Clear process for template contributions
- **Review Process**: Peer review for all submissions
- **Quality Standards**: Consistent quality across all templates
- **Attribution**: Credit contributors appropriately

---

*Last Updated: 2025-10-05*
*Version: 1.0.0*

