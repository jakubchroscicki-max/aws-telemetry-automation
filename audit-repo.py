import os

def audit_all_assets(root_dir="."):
    print("=" * 90)
    print("     CLOUDOPS & MLOPS ENTERPRISE INTEGRATED REPOSITORY AUDIT LEDGER     ")
    print("=" * 90)
    
    # Rozszerzenia tekstowe i skryptowe do pełnej lustracji
    text_extensions = ('.yaml', '.yml', '.ps1', '.py', '.log', '.md')
    
    for root, dirs, files in os.walk(root_dir):
        # Ignorujemy wewnętrzny folder Gita, żeby nie śmiecić
        if '.git' in root:
            continue
            
        for file in files:
            # Omijamy same skrypty audytujące
            if file in ['audit-repo.py', 'audit-all.py']:
                continue
                
            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, root_dir)
            
            # Lustrujemy tylko czytelne pliki tekstowe/skryptowe
            if file.endswith(text_extensions) or file == 'README.md':
                print(f"\n[FILE ASSET] {rel_path}")
                print(f"[SIZE] {os.path.getsize(full_path)} Bytes")
                print("-" * 70)
                try:
                    with open(full_path, "r", encoding="utf-8", errors="ignore") as f:
                        print(f.read().strip() or "(Empty File)")
                except Exception as e:
                    print(f"Could not read data stream: {str(e)}")
                print("-" * 70)
                print("=" * 90)
            
            # Dla binarnego Excela robimy elegancki wpis metadanych
            elif file.endswith('.xlsx'):
                print(f"\n[BINARY DATA ASSET] {rel_path}")
                print(f"[TYPE] MLOps Performance Metrics Spreadsheet (Binary)")
                print(f"[SIZE] {os.path.getsize(full_path)} Bytes")
                print("-" * 70)
                print("-> Compiled Excel Binary. Content structurally cataloged for MLOps audits.")
                print("-" * 70)
                print("=" * 90)

if __name__ == "__main__":
    audit_all_assets()
