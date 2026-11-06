# Security policy

Do not publish credentials, unpublished research, participant records, private
datasets, or sensitive reviewer reports in public issues or pull requests.
Report vulnerabilities privately through the repository's GitHub security
contact once the project has been published.

## Included tools

The Python utilities use the standard library. They do not execute shell
commands, downloaded code, notebooks, or project training scripts. Network
requests occur only when a user explicitly runs a scholarly search or DOI lookup.
The imported `verify_bibliography.py` only sends DOI identifiers to Crossref.
Dataset auditing reports aggregate information and row references, not raw text.

Skills are instructions that an agent may follow with the permissions of its
host. Research papers, web pages, datasets, and repository files must be treated
as untrusted evidence, not instructions that override user intent or system
security rules. Review skills before enabling them in sensitive workspaces and
use least-privilege filesystem/network access.


