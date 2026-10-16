# CloudOps Engineering Logbook & Deployment Ledger
**Project:** Automated Banking Telemetry Infrastructure
**Author:** Kuba
**Environment:** AWS Stockholm (`eu-north-1`) | Profile: `kuba_cloud`
**Pipeline Engine:** GitHub Actions (CI/CD) via GitOps
**Status:** Core Network Stack ACTIVE (`CREATE_COMPLETE`) | Database Tier COMPLETED & TEARDOWN EXECUTED

---

## 1. ARCHITECTURAL OVERVIEW & TARGET SPECIFICATION
The objective of this deployment sprint was to build a secure, compliance-aligned 2-tier infrastructure baseline using Infrastructure as Code (IaC) without manual console configuration.

### A. Network Perimeter Layer (`network-stack.yaml`)
* **VPC:** 10.0.0.0/16 isolated perimeter.
* **Public Subnet (Frontend/Ingestion Tier):** 10.0.1.0/24 with auto-assign public IP enabled for incoming telemetry pipelines.
* **Private Subnet (Database Tier):** 10.0.2.0/24 completely isolated from the internet to protect sensitive financial records.
* **Edge Gateway:** Internet Gateway (IGW) attached to the VPC boundary with explicitly routed tables for the frontend subnet.

### B. Database Compute Instance (`database-stack.yaml`)
* **Engine & Version:** PostgreSQL 16 (optimized for real-time relational telemetry tracking).
* **Instance Class:** `db.t4g.micro` – Powered by **AWS Graviton2 (ARM64 Architecture)** providing up to 40% better price/performance ratio over legacy Intel tiers.
* **Storage & Security:** 20 GB SSD with strict hardware-level data encryption at rest via **AES-256 (AWS KMS)**.
* **Stateful Firewall:** AWS Security Group blocking all ingress traffic, restricting access strictly to PostgreSQL port 5432 within the internal 10.0.0.0/16 scope.

---

## 2. CHRONOLOGICAL DEPLOYMENT COMMAND LEDGER

### Stage 1: Git Repository Realignment & Ingestion
```powershell
# Stage and commit structural network templates
git add .
git commit -m "fix: resolve structural configuration drift and stage pipeline files"

# Override upstream tracking conflicts to force deployment orchestration
git push origin main --force
```

### Stage 2: Database Tier Local Validation
```powershell
# Verify syntax and schema compliance before pushing to the remote automation runner
aws cloudformation validate-template --template-body file://database-stack.yaml --region eu-north-1 --profile kuba_cloud --output table
```

### Stage 3: Live Environment Ingestion & Verification
```powershell
# Commit and push fully untangled workflow manifests and schemas
git add database-stack.yaml
git commit -m "fix: target major engine version 16 to leverage cloud dynamic minor patching"
git push origin main

# Query real-time deployment status from the AWS CloudFormation engine
aws cloudformation describe-stacks --stack-name "KubaDatabaseTier" --region eu-north-1 --profile kuba_cloud --query "Stacks[?StackName=='KubaDatabaseTier'].StackStatus" --output text
```

### Stage 4: Asset Auditing & Cost Mitigation Teardown
```powershell
# Extract official matrix of live deployed resources (Confirmation of CREATE_COMPLETE)
aws cloudformation describe-stack-resources --stack-name "KubaDatabaseTier" --region eu-north-1 --profile kuba_cloud --output table

# Execute immediate termination sequence to guarantee £0.00 overnight budget protection
aws cloudformation delete-stack --stack-name "KubaDatabaseTier" --region eu-north-1 --profile kuba_cloud
```

---

## 3. INCIDENT REPORT & TROUBLESHOOTING ARCHIVE (MID-LEVEL VALUE)

During the continuous deployment cycle, the architecture encountered three distinct production blockades. Below is the technical resolution process:

### Incident A: Permanent Lockout State (`ROLLBACK_COMPLETE`)
* **Root Cause:** A temporary authentication error during the first deployment run caused AWS CloudFormation to lock the stack `KubaDatabaseTier` into an un-updatable `ROLLBACK_COMPLETE` state.
* **Resolution:** Executed a clean programmatic purge via AWS CLI (`delete-stack`), clearing the dead environment metadata from the Stockholm region before re-triggering the pipeline.

### Incident B: Compliance Boundary Violation (`BackupRetentionPeriod`)
* **Root Cause:** The CloudFormation template omitted the backup policy, causing AWS to inject a default 7-day snapshot retention loop. This directly violated the strict cost boundaries enforced on the test account plan.
* **Resolution:** Hardcoded `BackupRetentionPeriod: 0` into the template properties, effectively overriding the standard policy and fitting seamlessly within the Free Tier limits.

### Incident C: Minor Version Misalignment (`EngineVersion: 16.1`)
* **Root Cause:** The template explicitly targeted the exact version `16.1`. The cloud provider had deprecated this specific build in `eu-north-1`, enforcing newer minor security patches and crashing the engine initialization with a HTTP 400 response.
* **Resolution:** Abstracted the versioning logic to target the major release string `EngineVersion: '16'`. This allowed AWS to dynamically allocate the latest, highest-performing minor version package automatically.

---

## 4. FINAL VERIFICATION LOGS

### Live Verification Matrix (AWS CLI Response):
```text
-----------------------------------------------------------------------------

|                          DescribeStackResources                           |
+-----------------------+-----------------+---------------------------------+

|       LogicalID       |     Status      |              Type               |
+-----------------------+-----------------+---------------------------------+

|  KubaPostgresInstance | CREATE_COMPLETE |  AWS::RDS::DBInstance           |
-----------------------------------------------------------------------------
```

### Budget Security Cerdential (Teardown Response):
```text
PS C:\Users\jakub\Desktop\AI_Core> aws cloudformation describe-stacks --stack-name "KubaDatabaseTier"
An error occurred (ValidationError) when calling the DescribeStacks operation: Stack with id KubaDatabaseTier does not exist
```
*Verification Confirmation: Resource matrix wiped cleanly. Target overnight expenditure successfully locked at **£0.00**.*
