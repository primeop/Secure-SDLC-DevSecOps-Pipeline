# Custom enrichment script (pseudo)
# Maps findings with CWE, severity, and adds remediation

def enrich(finding):
    cwe_map = {
        "http://": {"CWE": "CWE-319", "Severity": "High", "Fix": "Use HTTPS"},
    }
    for pattern, info in cwe_map.items():
        if pattern in finding['code']:
            finding.update(info)
    return finding
