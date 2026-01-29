# Git Collaboration Lab - Workflow Documentation

## Assignment Overview
This lab demonstrates Git collaboration with three branches (main, koushik, satya) where different modules are pushed and merged through pull requests.

## Branch Structure

### Main Branch
- Contains the core README and will receive merged changes
- Base branch for all pull requests

### Koushik Branch  
- Contains `koushik_module.py` - User Management System
- Features:
  - User registration and management
  - User authentication
  - User listing and retrieval

### Satya Branch
- Contains `satya_module.py` - Data Processing System
- Features:
  - Data collection and processing
  - Statistical analysis
  - Data type tracking

## Modules Created

### 1. main_module.py
- **Purpose**: Entry point for the application
- **Location**: Should be in main branch
- **Functionality**: Initializes the application and coordinates other modules

### 2. koushik_module.py
- **Purpose**: User management features
- **Location**: Developed in koushik branch
- **Functionality**: 
  - UserManager class for user operations
  - Authentication functions
  - User database management

### 3. satya_module.py
- **Purpose**: Data processing features
- **Location**: Developed in satya branch
- **Functionality**:
  - DataProcessor class for data handling
  - Statistical analysis functions
  - Data type categorization

## Workflow for Assignment

### Step 1: Branch Setup
```bash
# Main branch already exists
git fetch origin main

# Koushik branch - for user management module
git checkout -b koushik origin/main
# Add koushik_module.py here
git add koushik_module.py
git commit -m "Add user management module"
git push origin koushik

# Satya branch - for data processing module
git checkout -b satya origin/main
# Add satya_module.py here
git add satya_module.py
git commit -m "Add data processing module"
git push origin satya
```

### Step 2: Pull Request Workflow
1. Create PR from `koushik` branch to `main`
   - Title: "Add User Management Module"
   - Description: Implements user authentication and management features
   
2. Create PR from `satya` branch to `main`
   - Title: "Add Data Processing Module"
   - Description: Implements data processing and analytics features

3. Review and merge both PRs to main branch

### Step 3: Final Integration
- After merging, main branch will contain all three modules
- Application can be run with all features integrated

## Testing the Modules

### Test Main Module
```bash
python main_module.py
```
Expected output: Welcome message and initialization confirmation

### Test Koushik Module
```bash
python koushik_module.py
```
Expected output: User management operations including adding users and authentication

### Test Satya Module
```bash
python satya_module.py
```
Expected output: Data processing operations including statistics and analysis

## Learning Objectives
- ✅ Creating multiple branches for parallel development
- ✅ Developing isolated features on separate branches
- ✅ Pushing different modules to their respective branches
- ✅ Using pull requests to merge changes
- ✅ Collaborative Git workflow simulation

## Summary
This lab successfully demonstrates:
1. **Branch Management**: Three branches (main, koushik, satya) with different purposes
2. **Module Development**: Three distinct Python modules with different functionalities
3. **Git Workflow**: Push different modules to different branches
4. **Pull Request Process**: Merge branches through PRs (to be completed as part of assignment)
