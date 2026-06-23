from app.seed.expanded_devops_cards import EXPANDED_DEVOPS_CARDS


DEVOPS_DECKS = [
    {
        "title": "Docker - Foundations",
        "description": "Images, containers, layers, networks, volumes, and Compose.",
        "topic": "docker",
        "level": "beginner",
        "cards": [
            {
                "front": "What is the difference between a Docker image and a container?",
                "back": "An image is a read-only template. A container is a running instance of that image with a thin writable layer.",
                "card_type": "interview",
            },
            {
                "front": "Why use a multi-stage Docker build?",
                "back": "To build with heavy tools in one stage and copy only the runtime artifact into a smaller, safer final image.",
                "card_type": "concept",
            },
            {
                "front": "Command: list running containers.",
                "back": "docker ps",
                "card_type": "command",
            },
            {
                "front": "Scenario: A container exits immediately. What do you check first?",
                "back": "Check docker logs, the container command/entrypoint, required environment variables, file permissions, and the process exit code.",
                "card_type": "scenario",
            },
        ],
    },
    {
        "title": "Kubernetes - Core Objects",
        "description": "Pods, Deployments, Services, ConfigMaps, Secrets, probes, and scaling.",
        "topic": "kubernetes",
        "level": "intermediate",
        "cards": [
            {
                "front": "What is the difference between a Pod and a Deployment?",
                "back": "A Pod is the smallest runnable unit. A Deployment manages ReplicaSets and keeps the desired number of Pods running with rollout/rollback support.",
                "card_type": "interview",
            },
            {
                "front": "Command: list Pods in namespace products.",
                "back": "kubectl get pods -n products",
                "card_type": "command",
            },
            {
                "front": "Why do we need a Service if Pods already have IP addresses?",
                "back": "Pod IPs are ephemeral. A Service provides stable DNS/load balancing over changing Pods.",
                "card_type": "concept",
            },
            {
                "front": "Scenario: Pod is CrashLoopBackOff. What do you check first?",
                "back": "kubectl logs, kubectl describe pod, events, env vars, config, image, command, resource limits, and probes.",
                "card_type": "scenario",
            },
        ],
    },
    {
        "title": "Helm - Charts and Values",
        "description": "Reusable Kubernetes packaging with templates and environment values.",
        "topic": "helm",
        "level": "intermediate",
        "cards": [
            {
                "front": "Why use Helm instead of raw Kubernetes YAML?",
                "back": "Helm packages related manifests, supports templating, values per environment, versioned releases, upgrades, and rollbacks.",
                "card_type": "interview",
            },
            {
                "front": "Command: render a Helm chart locally without installing it.",
                "back": "helm template RELEASE_NAME ./chart -f values.yaml",
                "card_type": "command",
            },
        ],
    },
    {
        "title": "CI/CD - GitHub Actions",
        "description": "Build, test, package, image creation, quality gates, and deployment flow.",
        "topic": "cicd",
        "level": "beginner",
        "cards": [
            {
                "front": "What is the difference between CI and CD?",
                "back": "CI continuously validates code with build/test checks. CD automatically delivers validated changes to environments.",
                "card_type": "concept",
            },
            {
                "front": "Why should tests run before building and pushing a Docker image?",
                "back": "A failing build should never become a deployable artifact. Tests are a quality gate before packaging.",
                "card_type": "interview",
            },
        ],
    },
    {
        "title": "Terraform - Basics",
        "description": "Infrastructure as Code fundamentals: providers, resources, state, and plans.",
        "topic": "terraform",
        "level": "beginner",
        "cards": [
            {
                "front": "What is Terraform state?",
                "back": "State maps real infrastructure to Terraform configuration. It is required for planning changes and must be stored safely.",
                "card_type": "interview",
            },
            {
                "front": "Command: preview infrastructure changes.",
                "back": "terraform plan",
                "card_type": "command",
            },
        ],
    },
    {
        "title": "Monitoring - Prometheus and Grafana",
        "description": "Metrics, dashboards, alerts, and production visibility.",
        "topic": "monitoring",
        "level": "intermediate",
        "cards": [
            {
                "front": "What is the difference between logs, metrics, and traces?",
                "back": "Logs are events, metrics are numeric time series, and traces show a request path across services.",
                "card_type": "concept",
            },
            {
                "front": "Why does Prometheus scrape metrics instead of apps pushing them?",
                "back": "Pull-based scraping centralizes discovery, health, labels, and collection intervals. Apps expose metrics; Prometheus collects them.",
                "card_type": "interview",
            },
        ],
    },
    {
        "title": "Security - DevOps Hardening",
        "description": "Secrets, RBAC, non-root containers, scanning, TLS, and least privilege.",
        "topic": "security",
        "level": "intermediate",
        "cards": [
            {
                "front": "Why should containers run as non-root?",
                "back": "It reduces blast radius if the app is compromised and aligns with Kubernetes Pod Security best practices.",
                "card_type": "interview",
            },
            {
                "front": "What is the production problem with committing Kubernetes Secret YAML to Git?",
                "back": "Secret values are only base64-encoded, not safely encrypted. Use tools like External Secrets, Vault, or cloud secret managers.",
                "card_type": "scenario",
            },
        ],
    },
]

ADDITIONAL_DEVOPS_CARDS = {
    "Docker - Foundations": [
        {
            "front": "What is a Docker layer?",
            "back": "A Docker layer is a filesystem change created by an image instruction. Layers are cached and reused to make builds and pulls faster.",
            "card_type": "concept",
        },
        {
            "front": "Why should you use `.dockerignore`?",
            "back": "It keeps the build context small, avoids copying local junk or secrets, and prevents stale artifacts from influencing image builds.",
            "card_type": "interview",
        },
        {
            "front": "Command: show logs for a container named api.",
            "back": "docker logs api",
            "card_type": "command",
        },
        {
            "front": "Command: enter a shell inside a running container.",
            "back": "docker exec -it CONTAINER_NAME sh",
            "card_type": "command",
        },
        {
            "front": "Scenario: App works on host but cannot connect to DB in Docker Compose. What is a common cause?",
            "back": "Using localhost from inside the app container. In Compose, the DB should be reached by service name, for example `db:5432`.",
            "card_type": "scenario",
        },
        {
            "front": "Why is running containers as root risky?",
            "back": "If the app is compromised, root inside the container increases the potential blast radius, especially with mounted volumes or runtime escapes.",
            "card_type": "interview",
        },
    ],
    "Kubernetes - Core Objects": [
        {
            "front": "What is a Kubernetes Namespace?",
            "back": "A Namespace is a logical isolation boundary for Kubernetes resources, commonly used to separate apps, teams, or environments.",
            "card_type": "concept",
        },
        {
            "front": "What is the difference between ConfigMap and Secret?",
            "back": "ConfigMap stores non-sensitive configuration. Secret stores sensitive values, but real production secrets should usually come from a secret manager.",
            "card_type": "interview",
        },
        {
            "front": "Command: describe a failing Pod.",
            "back": "kubectl describe pod POD_NAME -n NAMESPACE",
            "card_type": "command",
        },
        {
            "front": "Command: follow logs for a Deployment.",
            "back": "kubectl logs -f deployment/DEPLOYMENT_NAME -n NAMESPACE",
            "card_type": "command",
        },
        {
            "front": "What is the difference between readiness and liveness probes?",
            "back": "Readiness decides whether a Pod receives traffic. Liveness decides whether Kubernetes should restart the container.",
            "card_type": "interview",
        },
        {
            "front": "Scenario: Service has no endpoints. What do you check?",
            "back": "Check the Service selector, Pod labels, Pod readiness, namespace, and whether the Pods are actually running.",
            "card_type": "scenario",
        },
        {
            "front": "What does ImagePullBackOff usually mean?",
            "back": "Kubernetes cannot pull the image. Common causes are wrong image name/tag, missing registry credentials, or network/registry access issues.",
            "card_type": "scenario",
        },
        {
            "front": "Why set CPU and memory requests?",
            "back": "Requests help the scheduler place Pods correctly and provide reliable capacity planning. Limits prevent a container from consuming too many resources.",
            "card_type": "interview",
        },
    ],
    "Helm - Charts and Values": [
        {
            "front": "What is `values.yaml` in Helm?",
            "back": "`values.yaml` contains configurable inputs for templates, allowing the same chart to be reused across environments.",
            "card_type": "concept",
        },
        {
            "front": "Command: install or upgrade a Helm release.",
            "back": "helm upgrade --install RELEASE_NAME ./chart -f values.yaml",
            "card_type": "command",
        },
        {
            "front": "Command: rollback a Helm release.",
            "back": "helm rollback RELEASE_NAME REVISION",
            "card_type": "command",
        },
        {
            "front": "Why run `helm template` in CI?",
            "back": "It renders templates without touching the cluster, catching syntax and values errors early.",
            "card_type": "interview",
        },
        {
            "front": "Scenario: Helm upgrade fails. What do you inspect?",
            "back": "Check `helm status`, rendered manifests with `helm template`, Kubernetes events, rollout status, and values used for the release.",
            "card_type": "scenario",
        },
    ],
    "CI/CD - GitHub Actions": [
        {
            "front": "What is an artifact in CI/CD?",
            "back": "An artifact is a build output such as a jar, binary, test report, or packaged chart that can be stored and reused by later jobs.",
            "card_type": "concept",
        },
        {
            "front": "Why tag Docker images with a commit SHA?",
            "back": "A commit SHA creates an immutable link between source code and image, making deployments traceable and rollbacks safer.",
            "card_type": "interview",
        },
        {
            "front": "What is a quality gate?",
            "back": "A quality gate is a required check, such as tests, linting, scanning, or review approval, that must pass before promotion.",
            "card_type": "concept",
        },
        {
            "front": "Scenario: Pipeline passes locally but fails in CI. What do you compare?",
            "back": "Compare OS, environment variables, secrets, dependency versions, working directory, network access, caches, and file paths.",
            "card_type": "scenario",
        },
        {
            "front": "Why should deployment jobs depend on build/test jobs?",
            "back": "It prevents unverified code from being deployed and creates a clear promotion flow through the pipeline.",
            "card_type": "interview",
        },
    ],
    "Terraform - Basics": [
        {
            "front": "What is the difference between `terraform plan` and `terraform apply`?",
            "back": "`plan` previews changes. `apply` executes those changes against real infrastructure.",
            "card_type": "interview",
        },
        {
            "front": "Why should Terraform state be remote for teams?",
            "back": "Remote state enables collaboration, locking, backup, and a single source of truth for infrastructure mappings.",
            "card_type": "concept",
        },
        {
            "front": "What is a Terraform provider?",
            "back": "A provider is a plugin that lets Terraform manage a platform or service, such as AWS, Azure, Kubernetes, or GitHub.",
            "card_type": "concept",
        },
        {
            "front": "Scenario: Terraform wants to recreate a database. What should you do?",
            "back": "Stop and inspect the plan carefully. Check lifecycle rules, changed immutable fields, state drift, imports, and whether replacement is acceptable.",
            "card_type": "scenario",
        },
        {
            "front": "Command: format Terraform files.",
            "back": "terraform fmt -recursive",
            "card_type": "command",
        },
    ],
    "Monitoring - Prometheus and Grafana": [
        {
            "front": "What is an SLI?",
            "back": "A Service Level Indicator is a measured reliability signal, such as availability, latency, or error rate.",
            "card_type": "concept",
        },
        {
            "front": "What is an SLO?",
            "back": "A Service Level Objective is a target for an SLI, such as 99.9% availability over 30 days.",
            "card_type": "concept",
        },
        {
            "front": "What metrics matter for an HTTP API?",
            "back": "Request rate, error rate, latency percentiles, saturation, CPU, memory, restarts, and database connection pool usage.",
            "card_type": "interview",
        },
        {
            "front": "Scenario: Users report slowness. What dashboards do you check?",
            "back": "Check request latency, 5xx/4xx rates, CPU/memory, pod restarts, DB latency, DB connections, and recent deployments.",
            "card_type": "scenario",
        },
        {
            "front": "Why are alerts better when tied to user impact?",
            "back": "User-impact alerts reduce noise and focus on symptoms that matter, such as high error rate or latency, instead of every low-level fluctuation.",
            "card_type": "interview",
        },
    ],
    "Security - DevOps Hardening": [
        {
            "front": "What is least privilege?",
            "back": "Least privilege means giving an identity only the permissions it needs to perform its job, nothing more.",
            "card_type": "concept",
        },
        {
            "front": "Why scan container images?",
            "back": "Image scanning finds known CVEs in OS packages and application dependencies before deployment.",
            "card_type": "interview",
        },
        {
            "front": "What is Kubernetes RBAC?",
            "back": "RBAC controls who or what can perform actions against Kubernetes resources using Roles, ClusterRoles, RoleBindings, and ClusterRoleBindings.",
            "card_type": "concept",
        },
        {
            "front": "Scenario: A Pod should not talk to the database. What Kubernetes feature helps?",
            "back": "NetworkPolicy can restrict traffic so only approved Pods can connect to the database service.",
            "card_type": "scenario",
        },
        {
            "front": "Why use a read-only root filesystem?",
            "back": "It reduces persistence options for attackers and makes the container filesystem more predictable. Writable paths should be explicit, such as `/tmp`.",
            "card_type": "interview",
        },
    ],
}

for deck in DEVOPS_DECKS:
    deck["cards"].extend(ADDITIONAL_DEVOPS_CARDS.get(deck["title"], []))
    deck["cards"].extend(EXPANDED_DEVOPS_CARDS.get(deck["title"], []))
