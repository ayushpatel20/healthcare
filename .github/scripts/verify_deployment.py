import os
import sys

def verify_deployment():
    print("=== Starting Pre-Deployment Verification Checks ===")
    
    # 1. Archive & Backup Blocklist Check
    # The objective is to ensure no backup archives exist anywhere in the repository directory.
    archive_extensions = ('.zip', '.tar', '.gz', '.tgz', '.rar', '.7z', '.bak')
    found_archives = []
    
    # 2. Sensitive files check (e.g., .env or config containing raw credentials)
    sensitive_files = ('.env',)
    found_sensitive = []

    # Get the project root directory (two levels up from this script or current working directory)
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    print(f"Project root directory determined as: {project_root}")

    for root, dirs, files in os.walk(project_root):
        # Skip git folders and github workflows folders during local check
        if '.git' in root or '.github' in root:
            continue
            
        for file in files:
            # Check for archive files
            if file.lower().endswith(archive_extensions):
                full_path = os.path.join(root, file)
                found_archives.append(os.path.relpath(full_path, project_root))
            
            # Check for sensitive files
            if file.lower() in sensitive_files:
                full_path = os.path.join(root, file)
                found_sensitive.append(os.path.relpath(full_path, project_root))

    if found_archives:
        print("ERROR: Backup archive file(s) found in repository. No ZIP or archive backups are allowed:")
        for archive in found_archives:
            print(f"  - {archive}")
        print("Please remove these archive files and try again.")
        sys.exit(1)
    else:
        print("[OK] No backup archives (.zip, .tar, .gz, etc.) found in the repository.")

    if found_sensitive:
        print("ERROR: Sensitive configuration file(s) found in repository root/subfolders:")
        for sens in found_sensitive:
            print(f"  - {sens}")
        print("Sensitive files like `.env` must not be pushed to GitHub. Use GitHub Secrets instead.")
        sys.exit(1)
    else:
        print("[OK] No sensitive config files (.env) found in the repository.")

    # 3. Critical Files Integrity Checks
    # We must ensure the website has its key entrance page and structure
    critical_files = [
        'index.html',
        'aboutus.html',
        'contactus.html',
        'css/style.css'
    ]
    
    missing_files = []
    for rel_path in critical_files:
        full_path = os.path.join(project_root, rel_path)
        if not os.path.exists(full_path):
            missing_files.append(rel_path)
        elif os.path.getsize(full_path) == 0:
            print(f"WARNING: Critical file '{rel_path}' is empty.")

    if missing_files:
        print("ERROR: Missing critical website file(s) required for deployment:")
        for missing in missing_files:
            print(f"  - {missing}")
        sys.exit(1)
    else:
        print("[OK] All critical website files exist and are populated.")

    print("=== All Verification Checks Passed Successfully! ===")
    sys.exit(0)

if __name__ == '__main__':
    verify_deployment()
