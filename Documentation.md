
# OTP Authentication System – Documentation

## Overview

This project implements a **RESTful OTP-based Authentication System** using Django and Django REST Framework. It allows users to authenticate via their **mobile number** using a **One-Time Password (OTP)**. The system uses **PostgreSQL** as the database, **Redis** for rate limiting, and is fully **Dockerized** for consistent deployment.

## Features

-  OTP login/registration
-  Rate limiting for OTP requests
-  JWT-based authentication
-  Swagger (OpenAPI) documentation
-  Dockerized
-  PostgreSQL as primary DB

## Why PostgreSQL over MongoDB?

While MongoDB can work for simple JSON-like storage, PostgreSQL is a **better choice for authentication systems** because:

### Strong Reasons to Prefer PostgreSQL:
1. **ACID compliance**: Ensures consistent user data (critical for authentication).
2. **Relational integrity**: Foreign keys, constraints — perfect for managing users and OTPs.
3. **Native support in Django**: Django was built for relational DBs like PostgreSQL, not NoSQL.
4. **Better performance for auth queries**: RDBMS indexing and JOINs are ideal for quick lookups.
5. **Tooling and migrations**: Easier schema migrations using `makemigrations` / `migrate`.

### Step 1: Request OTP

**Endpoint:** `POST /api/request-otp/`

```json
{
  "mobile": "09123456789"
}
```

### Step 2: Verify OTP

**Endpoint:** `POST /api/verify-otp/`

```json
{
  "mobile": "09123456789",
  "code": "123456"
}
```

**Response (on success):**

```json
{
  "access": "eyJ0eXAiOiJKV1QiLCJhbGci...",
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGci..."
}
```

## Swagger UI

Once the project is running, access:

```
http://localhost:8000/swagger/
```

## Running the App

```bash
docker-compose up --build
```

- App runs at: `http://localhost:8000/`
- Swagger UI: `http://localhost:8000/swagger/`
