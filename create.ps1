# Define the root project directory
$rootDir = "factory_management"

# Define the subdirectories to create
$subDirs = @(
    "app",
    "app/api",
    "app/api/blueprints",
    "app/api/utils",
    "app/extensions",
    "app/schemas",
    "tests",
    "instance"
)

# Define the files to create with their paths
$files = @(
    ".env",
    ".gitignore",
    "config.py",
    "factory.py",
    "models.py",
    "requirements.txt",
    "run.py",
    "app/__init__.py",
    "app/api/__init__.py",
    "app/api/blueprints/__init__.py",
    "app/api/blueprints/employee.py",
    "app/api/blueprints/product.py",
    "app/api/blueprints/order.py",
    "app/api/blueprints/customer.py",
    "app/api/blueprints/production.py",
    "app/api/utils/__init__.py",
    "app/api/utils/helpers.py",
    "app/extensions/__init__.py",
    "app/extensions/limiter.py",
    "app/schemas/__init__.py",
    "app/schemas/employee.py",
    "app/schemas/product.py",
    "app/schemas/order.py",
    "app/schemas/customer.py",
    "app/schemas/production.py",
    "tests/__init__.py",
    "tests/conftest.py",
    "tests/test_employee.py",
    "tests/test_product.py",
    "tests/test_order.py",
    "tests/test_customer.py",
    "tests/test_production.py",
    "instance/factory.db"
)

# Create the root directory if it does not exist
if (-not (Test-Path -Path $rootDir)) {
    New-Item -ItemType Directory -Path $rootDir -Force
}

# Create the subdirectories if they do not exist
foreach ($subDir in $subDirs) {
    $fullPath = Join-Path -Path $rootDir -ChildPath $subDir
    if (-not (Test-Path -Path $fullPath)) {
        New-Item -ItemType Directory -Path $fullPath -Force
    }
}

# Create the files if they do not exist
foreach ($file in $files) {
    $fullPath = Join-Path -Path $rootDir -ChildPath $file
    if (-not (Test-Path -Path $fullPath)) {
        New-Item -ItemType File -Path $fullPath -Force
    }
}

Write-Output "Project directory structure and files created successfully!"
