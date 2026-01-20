<!--
Sync Impact Report:
- Version change: N/A → 1.0.0
- Modified principles: N/A (new constitution)
- Added sections: All sections from user input
- Removed sections: Template placeholder sections
- Templates requiring updates:
  - ✅ plan-template.md: Updated Constitution Check section
  - ✅ spec-template.md: Updated scope/requirements alignment
  - ✅ tasks-template.md: Updated task categorization
- Follow-up TODOs:
  - TODO(RATIFICATION_DATE): Original adoption date unknown
-->

# Todo Project Constitution

## 1. Purpose & Vision
The purpose of this project is to incrementally evolve a simple Todo application into a production-grade, AI-powered, cloud-native system using Spec-Kit Plus and Claude Code.

The system must demonstrate:
- Progressive complexity across phases
- Clear architectural evolution
- Spec-driven development discipline
- AI-assisted task management through natural language
- Cloud-native deployment practices

Each phase must be functional, reviewable, and independently valuable.

---

## 2. Core Principles (Non-Negotiable)

### 2.1 Spec-Driven Development
Every feature MUST be preceded by:
- `sp.constitution` (once, global)
- `sp.specify` (per phase / feature)
- `sp.plan` (per phase / feature)
No implementation without an approved spec.
All development must be spec-driven using Claude Code and Spec-Kit Plus.

### 2.2 Progressive Enhancement
Each phase must **extend**, not replace, the previous phase.
- Core Todo functionality must remain consistent across all phases.
- New capabilities must layer cleanly on top of existing ones.

### 2.3 Minimalism with Justified Complexity
- The simplest viable solution must always be preferred.
- Any added complexity must be:
  - Explicitly justified
  - Traceable to a requirement
  - Documented in the spec

### 2.4 Clear Separation of Concerns
- Business logic, persistence, AI orchestration, and infrastructure concerns must be separated.
- No phase may tightly couple unrelated responsibilities.
- Each layer must be replaceable without rewriting the entire system.

### 2.5 Technology Stack Adherence
- Phase II must use: Next.js 16+ (App Router), Python FastAPI, SQLModel, Neon Serverless PostgreSQL
- Authentication must be implemented using Better Auth with JWT tokens
- MCP tools must be used for AI integration in Phase III and beyond
- Containerization and orchestration must use Docker, Kubernetes, and Helm for Phases IV and V

---

## 3. Functional Invariants (Must Always Hold)

These invariants apply across **all phases**:

1. A Todo item has:
   - A unique identifier
   - A title
   - A completion status
2. Users must be able to:
   - Add tasks
   - View tasks
   - Update tasks
   - Delete tasks
   - Mark tasks as complete or incomplete
3. Task state must always be internally consistent.
4. Invalid operations must fail safely with clear feedback.
5. User authentication and authorization must be enforced where applicable.

---

## 4. Phase Evolution Constraints

### 4.1 Phase I – Console Application
- Data must be stored **in memory only**
- No database, no networking, no AI
- All interactions occur via CLI
- Focus is correctness and clarity, not persistence

### 4.2 Phase II – Full-Stack Web Application
- Persistence must be introduced using SQLModel and Neon DB
- Frontend and backend must be logically separated
- REST API becomes the single source of truth
- Console-only logic must be refactored, not duplicated
- Authentication must be implemented using Better Auth with JWT tokens
- API endpoints must follow the specified patterns:
  - GET /api/{user_id}/tasks - List all tasks
  - POST /api/{user_id}/tasks - Create a new task
  - GET /api/{user_id}/tasks/{id} - Get task details
  - PUT /api/{user_id}/tasks/{id} - Update a task
  - DELETE /api/{user_id}/tasks/{id} - Delete a task
  - PATCH /api/{user_id}/tasks/{id}/complete - Toggle completion
- All API endpoints must require valid JWT tokens for authentication
- Database schema must include tasks table with user_id foreign key relationship

### 4.3 Phase III – AI-Powered Todo Chatbot
- AI interaction must be implemented using:
  - OpenAI ChatKit
  - OpenAI Agents SDK
  - Official MCP SDK
- AI must act as an **assistant**, not a replacement for core logic
- All AI actions must map to existing Todo operations
- AI must never bypass validation or persistence layers
- MCP server must expose standardized tools for task operations (add_task, list_tasks, complete_task, delete_task, update_task)

### 4.4 Phase IV – Local Kubernetes Deployment
- Application must be containerized
- Must deploy locally using Minikube
- Helm charts must define deployments
- Observability and repeatability are mandatory
- Docker AI Agent (Gordon) and kubectl-ai/Kagent must be utilized for deployment operations

### 4.5 Phase V – Cloud-Native Deployment
- System must be deployable on DigitalOcean Kubernetes (DOKS)
- Kafka and Dapr must be used for asynchronous and service communication
- System must tolerate partial failures
- AI and Todo services must scale independently
- Advanced features must be implemented: recurring tasks, due dates & reminders, priorities & tags, search & filter, sort tasks

---

## 5. Authentication & Security Requirements

### 5.1 JWT-Based Authentication
- Better Auth must be configured to issue JWT tokens
- Frontend must attach JWT tokens to every API request header
- Backend must verify JWT signatures using shared secret (BETTER_AUTH_SECRET)
- All API endpoints must filter data by authenticated user's ID
- User isolation must be enforced - each user only sees their own tasks

### 5.2 API Security
- All API requests must include valid JWT tokens
- Requests without tokens must receive 401 Unauthorized
- Task ownership must be enforced on every operation
- Session state must be properly managed

---

## 6. AI Governance Rules

1. AI is **not authoritative**
2. AI must:
   - Interpret user intent
   - Call tools / APIs
   - Return confirmations
3. AI must never:
   - Modify state without explicit tool invocation
   - Hallucinate task data
   - Operate without traceable actions
4. All AI decisions must be explainable through logs or traces.
5. Natural language commands must be mapped to appropriate task operations

---

## 7. Database & Persistence Standards

### 7.1 Schema Requirements
- Tasks table must include: id (primary key), user_id (foreign key), title, description, completed, created_at, updated_at
- Users table managed by Better Auth with: id, email, name, created_at
- Proper indexing must be applied for efficient querying by user_id and completion status

### 7.2 Data Consistency
- All database operations must maintain referential integrity
- Transactions must be used for complex operations
- Validation must occur before persistence

---

## 8. Deployment & Infrastructure Discipline

- Each deployment target must be reproducible
- Local and cloud deployments must use the same manifests where possible
- Secrets must never be hardcoded
- Infrastructure must be declarative
- Monorepo structure must follow the specified folder organization with proper CLAUDE.md files

---

## 9. Educational & Bonus Features (Optional)

### 9.1 Bonus Feature Considerations
Projects may implement additional features for bonus points:
- Reusable Intelligence via Claude Code Subagents and Agent Skills
- Cloud-Native Blueprints via Agent Skills
- Multi-language Support (Urdu) in chatbot
- Voice Commands for todo operations

### 9.2 Learning Objectives
- Understanding of spec-driven development workflow
- Full-stack development with Next.js and FastAPI
- AI agent development and MCP integration
- Cloud-native deployment practices
- Event-driven architecture with Kafka and Dapr

---

## 10. Educational Integrity
This project is also a learning artifact.

Therefore:
- Code clarity is preferred over cleverness
- Every phase must be understandable in isolation
- Architecture decisions must be explainable to beginners
- Spec-driven methodology must be followed rigorously

---

## 11. Change Control
- Any change that violates this constitution is invalid
- Constitution updates require:
  - Explicit justification
  - Impact analysis on all phases

---

## Governance

This constitution supersedes all other practices. Amendments require explicit justification and impact analysis on all phases. All development must comply with these principles, and complexity must be justified with clear traceability to requirements.

**Version**: 1.0.0 | **Ratified**: TODO(RATIFICATION_DATE) | **Last Amended**: 2026-01-20
