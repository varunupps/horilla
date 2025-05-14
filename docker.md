# Docker

- Built on Python 3.10 image
- Uses PostgreSQL 16 Database
- Creates admin user with default username - 'admin' & password - 'admin'
- Automatically loads demo data when using containerized version

# Docker & Docker compose installation

- [Linux Docker Desktop](https://docs.docker.com/desktop/install/linux-install/)
- [Windows Docker Desktop](https://docs.docker.com/desktop/install/windows-install/)
- [Mac Docker Desktop](https://docs.docker.com/desktop/install/mac-install/)

## Build & Run

- ```docker compose up```

## Running Multiple Branches Simultaneously

To run both the master and baddie branches on the same host, you can use separate directories with project names:

```bash
# In one directory
cd ~/horilla-master
docker compose -p horilla-master up -d

# In another directory
cd ~/horilla-baddie
docker compose -f docker-compose.baddie.yaml -p horilla-baddie up -d
```

This approach ensures that each branch runs with its own isolated containers, networks, and volumes. The `-p` flag specifies a unique project name for each instance.

## Features

- **Auto-loading Demo Data**: When running in Docker, the system automatically loads demo data to help you get started quickly. No need to manually authenticate or load test data.
