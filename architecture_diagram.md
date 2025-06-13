# Garden AI Architecture Diagram

Below is a diagram of the Garden AI system architecture using Mermaid syntax. You can render this diagram using various Mermaid-compatible tools or websites like [Mermaid Live Editor](https://mermaid.live/).

For an alternative diagram using official AWS service icons, see [aws_architecture_diagram.md](aws_architecture_diagram.md).

```mermaid
graph TD
    %% Edge Device Components
    subgraph "Edge Device (Raspberry Pi)"
        A[Camera Module] -->|Captures Images| B[Local Storage]
        B -->|Python Script| C[Upload to AWS]
        D[Cron Jobs] -->|Trigger| A
    end

    %% AWS Cloud Components
    subgraph "AWS Cloud"
        %% Storage Layer
        E[S3 Bucket] -->|Stores Images| F[Image Repository]
        
        %% Database Layer
        G[DynamoDB] -->|Stores| G1[Plant Status]
        G -->|Stores| G2[AI Summaries]
        G -->|Stores| G3[Messages]
        
        %% Processing Layer
        H[EventBridge] -->|Scheduled Trigger| I[Lambda Function]
        I -->|Reads New Images| E
        I -->|Reads History| G
        I -->|Sends Image| J[Amazon Bedrock Nova Pro]
        J -->|Analysis Results| I
        I -->|Updates Status & Summaries| G
        I -->|Writes Messages| G
        
        %% Web Interface
        K[S3 Static Website] -->|Hosts| L[Web App]
        L -->|Reads/Writes via| M[API Gateway]
        M -->|Authenticates with| P[Cognito User Pool]
        M -->|Processes Requests| N[CRUD Lambda]
        N -->|CRUD Operations| G
    end
    
    %% Human Interaction
    O[Gardener] -->|Interacts with| L
    
    %% Connections between Edge and Cloud
    C -->|Uploads Images| E
    
    %% Styling
    classDef edge fill:#f9f,stroke:#333,stroke-width:2px;
    classDef aws fill:#FF9900,stroke:#232F3E,stroke-width:2px,color:#232F3E;
    classDef human fill:#bbf,stroke:#333,stroke-width:2px;
    
    class A,B,C,D edge;
    class E,F,G,G1,G2,G3,H,I,J,K,L,M,N,P aws;
    class O human;
```