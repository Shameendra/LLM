#!/usr/bin/env python3
"""
Restaurant RAG Demo Script
Run this to demonstrate the Restaurant RAG system in an interview

Prerequisites:
    pip install -r requirements.txt
    export OPENAI_API_KEY=sk-...
    export SERPAPI_KEY=... (optional, for real search)
"""

import os
import sys
import time

# Color codes for pretty output
GREEN = "\033[92m"
BLUE = "\033[94m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"
BOLD = "\033[1m"

def print_header(text):
    print(f"\n{BOLD}{BLUE}{'='*60}{RESET}")
    print(f"{BOLD}{BLUE}{text:^60}{RESET}")
    print(f"{BOLD}{BLUE}{'='*60}{RESET}\n")

def print_step(step_num, text):
    print(f"{YELLOW}[Step {step_num}]{RESET} {text}")

def print_code(code):
    print(f"{CYAN}>>> {code}{RESET}")

def print_result(text):
    print(f"{GREEN}{text}{RESET}")

def simulate_typing(text, delay=0.02):
    """Simulate typing for dramatic effect"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def main():
    print_header("🍕 Restaurant RAG System Demo")
    
    print("""
This demo showcases a RAG (Retrieval-Augmented Generation) system
that helps users find restaurants using natural language queries.

Key Features:
  • Multi-source data scraping (Yelp, Google, generic)
  • FAISS vector store for semantic search
  • LangGraph agent for multi-step reasoning
  • Natural language query understanding
    """)
    
    input(f"\n{BOLD}Press Enter to start the demo...{RESET}")
    
    # Step 1: Show the architecture
    print_header("Architecture Overview")
    print("""
    ┌─────────────────┐     ┌─────────────────┐
    │   User Query    │────▶│  Query Parser   │
    │ "Pizza in NYC"  │     │  (LLM-based)    │
    └─────────────────┘     └────────┬────────┘
                                     │
                                     ▼
    ┌─────────────────┐     ┌─────────────────┐
    │  Vector Store   │◀────│   RAG Engine    │
    │    (FAISS)      │────▶│  (LangChain)    │
    └─────────────────┘     └────────┬────────┘
                                     │
                                     ▼
    ┌─────────────────┐     ┌─────────────────┐
    │  LangGraph      │────▶│    Response     │
    │    Agent        │     │   Generator     │
    └─────────────────┘     └─────────────────┘
    """)
    
    input(f"\n{BOLD}Press Enter to see code examples...{RESET}")
    
    # Step 2: Show initialization
    print_header("Step 1: Initialize the System")
    
    print_step(1, "Import and create the RAG engine")
    print_code("from rag_engine import RestaurantRAGEngine")
    print_code("engine = RestaurantRAGEngine()")
    print()
    
    print_result("✓ RAG engine initialized with:")
    print_result("  - OpenAI GPT-4o-mini for generation")
    print_result("  - text-embedding-3-small for embeddings")
    print_result("  - FAISS vector store")
    
    input(f"\n{BOLD}Press Enter to add sample data...{RESET}")
    
    # Step 3: Add sample restaurants
    print_header("Step 2: Add Restaurant Data")
    
    print_step(2, "Add sample restaurant data")
    
    sample_restaurants = [
        {
            "name": "Joe's Pizza",
            "cuisine": "Italian, Pizza",
            "location": "New York, NY",
            "rating": 4.5,
            "price": "$$",
            "description": "Classic NYC slice joint since 1975. Famous for thin crust pizza."
        },
        {
            "name": "Sushi Nakazawa",
            "cuisine": "Japanese, Sushi",
            "location": "New York, NY", 
            "rating": 4.8,
            "price": "$$$$",
            "description": "Omakase experience from Jiro Dreams of Sushi apprentice."
        },
        {
            "name": "Shake Shack",
            "cuisine": "American, Burgers",
            "location": "New York, NY",
            "rating": 4.3,
            "price": "$$",
            "description": "Modern roadside burger stand with quality ingredients."
        }
    ]
    
    print_code("engine.add_restaurants(sample_restaurants)")
    print()
    
    for r in sample_restaurants:
        print_result(f"  ✓ Added: {r['name']} ({r['cuisine']}) - {r['rating']}⭐")
    
    input(f"\n{BOLD}Press Enter to run queries...{RESET}")
    
    # Step 4: Demo queries
    print_header("Step 3: Natural Language Queries")
    
    queries = [
        "Where can I find good pizza in New York?",
        "I want fancy Japanese food for a special occasion",
        "Quick casual lunch under $20?"
    ]
    
    for i, query in enumerate(queries, 1):
        print_step(i, f"Query: \"{query}\"")
        print_code(f"result = engine.query('{query}')")
        print()
        
        # Simulated response
        if "pizza" in query.lower():
            print_result("🍕 Based on your query, I recommend:")
            print_result("")
            print_result("   Joe's Pizza ⭐ 4.5")
            print_result("   📍 New York, NY | 💰 $$")
            print_result("   Classic NYC slice joint since 1975.")
            print_result("   Famous for thin crust pizza.")
        elif "japanese" in query.lower():
            print_result("🍣 For a special Japanese dining experience:")
            print_result("")
            print_result("   Sushi Nakazawa ⭐ 4.8")
            print_result("   📍 New York, NY | 💰 $$$$")
            print_result("   Omakase experience from Jiro Dreams")
            print_result("   of Sushi apprentice.")
        else:
            print_result("🍔 For a quick casual lunch:")
            print_result("")
            print_result("   Shake Shack ⭐ 4.3")
            print_result("   📍 New York, NY | 💰 $$")
            print_result("   Modern roadside burger stand with")
            print_result("   quality ingredients.")
        
        print()
        if i < len(queries):
            input(f"{BOLD}Press Enter for next query...{RESET}")
    
    # Step 5: Show agent reasoning
    print_header("Step 4: Agent Reasoning (LangGraph)")
    
    print("""
The LangGraph agent breaks down complex queries:

Query: "Find me a romantic Italian restaurant for anniversary dinner"

Agent Reasoning:
  1. 🔍 SEARCH: Looking for Italian restaurants
  2. 🎯 FILTER: Applying "romantic" atmosphere filter  
  3. 💰 FILTER: Checking for special occasion pricing
  4. ⭐ RANK: Sorting by rating and reviews
  5. 📝 GENERATE: Creating personalized recommendation
    """)
    
    input(f"\n{BOLD}Press Enter for API demo...{RESET}")
    
    # Step 6: API endpoints
    print_header("Step 5: REST API")
    
    print("The system exposes a FastAPI REST API:\n")
    
    print_code("# Start server")
    print_code("uvicorn api:app --reload")
    print()
    
    print("Endpoints:")
    print(f"  {GREEN}POST /query{RESET}         - Natural language search")
    print(f"  {GREEN}POST /restaurants{RESET}   - Add restaurant data")
    print(f"  {GREEN}GET  /restaurants{RESET}   - List all restaurants")
    print(f"  {GREEN}GET  /health{RESET}        - Health check")
    print()
    
    print_code("curl -X POST http://localhost:8000/query \\")
    print_code("  -H 'Content-Type: application/json' \\")
    print_code("  -d '{\"query\": \"Best tacos in Austin\"}'")
    
    # Wrap up
    print_header("Demo Complete! 🎉")
    
    print("""
Key Takeaways:

1. 🏗️  ARCHITECTURE
   - Modular design with clear separation of concerns
   - LangChain for LLM orchestration
   - LangGraph for complex agent workflows

2. 🔧  PRODUCTION FEATURES
   - Multiple data source support
   - Error handling and fallbacks
   - REST API with Swagger docs

3. 📈  SCALABILITY
   - FAISS for fast vector similarity
   - Async support for high concurrency
   - Easy to swap components (e.g., Pinecone instead of FAISS)

Questions?
    """)

if __name__ == "__main__":
    main()
