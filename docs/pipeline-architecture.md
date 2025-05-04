# 🏗️ DevSecOps CI/CD Architecture

- PR triggers pipeline
- Semgrep + SonarQube perform static scans
- ZAP performs DAST against a live URL
- Trivy scans Docker image layers for CVEs
- SBOM is generated via Syft
- Findings are enriched with CWE + Fix guidance
- Results are annotated on PR and stored as artifacts
