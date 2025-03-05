# **AI-Driven Trading Agent for Hyperliquid (Mock Implementation)**

## **Project Overview**
This project demonstrates a **trading agent** designed to make intelligent trading decisions using **LLM-driven AI models**. The system follows a structured pipeline:

1. **Gathering market data** (Mocked instead of real-time API calls).
2. **Processing and preparing data** for decision-making.
3. **Utilizing AI models to decide** trade positions (Buy, Sell, Hold).
4. **Simulating trade execution** (Instead of real on-chain trading).
5. **Logging and evaluating decisions** for future improvements.

Given the testnet **API key requirement and funding constraints**, we opted for a **simulated trading environment**, ensuring all functionalities work without real blockchain dependencies.

---

## **Project Components**

### **A. Market Data Simulation (Mock API)**
- Instead of calling Hyperliquid’s live API, we **simulate** fetching market prices.
- Prices fluctuate dynamically within a realistic range for assets like **BTC and ETH**.
- This allows for **realistic AI-driven trading decisions** without requiring real market connectivity.

### **B. AI-Driven Trade Decision-Making**
- AI/LLM logic **analyzes the market data** and decides whether to:
  - **Buy** a position (if the AI detects an opportunity).
  - **Sell** a position (if the AI predicts a downtrend).
  - **Hold** (if no strong signal is detected).
- The **decision logic mimics an AI-based approach**, but is randomized in this prototype for simplicity.

### **C. Trade Execution (Simulated)**
- Instead of placing real trades on Hyperliquid’s testnet, we **log the AI’s trade decisions**.
- The system simulates:
  - **Order placements** for the chosen assets.
  - **Execution at the market price**.
  - **Position tracking** over multiple cycles.

### **D. Logging & Evaluation**
- Trades are logged to **analyze AI performance**.
- This data could be further used for **AI fine-tuning or reinforcement learning**.

---

## **Why This Approach?**

### **1. Avoided On-Chain API Key & Funding Issues**  
- Hyperliquid’s testnet **requires Arbitrum USDC**, which is only accessible via **mainnet funding**.
- Since this was a **prototype**, a **mock environment** was the best tradeoff.

### **2. Focused on AI Trading Logic**  
- The goal was to demonstrate **AI integration** into trading rather than blockchain interaction.
- **LLM-centric approach** showcases decision-making rather than Hyperliquid's APIs.

### **3. Scalability for Future Enhancements**  
- If required, this **can be extended to live testnet trading** by switching from **mock API calls to Hyperliquid API**.
- The core **AI strategy remains the same**, meaning it’s adaptable to real-world applications.

---

## **Demo Flow**
To showcase the project, run the script and explain the following:
1. **Market Data Fetching** (Mocked market prices)
2. **AI Making Decisions** (Showing buy/sell/hold logic)
3. **Executing Trades** (Simulated order execution)
4. **Logging Results** (How the AI’s actions are tracked)

---

## **Potential Future Enhancements**
- **Integrate real Hyperliquid API** once funding and API keys are available.
- **Use Reinforcement Learning** instead of random decisions for AI optimization.
- **Introduce risk management strategies** (Stop-loss, Take-profit).
- **Expand asset coverage** (More cryptocurrencies & trading pairs).

---

## **Final Thoughts**
This project **demonstrates AI-powered trading agents** in a structured manner while overcoming testnet constraints. The implementation effectively showcases:

✅ **AI-based decision-making**  
✅ **Simulated trading execution**  
✅ **Scalability for real-world use cases**  

---

### **How to Run the Project**

1.  Create virtual environment
    ```bash
    python3 -m venv virtual
    ```
2. Activate environment (UNIX)
    ```bash
    (UNIX) source virtual/bin/activate
    (WINDOWS) virtual/scripts/activate
    ```
3. Install required packages
    ```bash
    pip install -r requirements.txt
    ```
4. .env Usage
    ```bash
    Follow .env.example and create .env before run app
    ```
5. Run API
    ```bash
    python3 main.py --env dev --debug
    ```
This will execute a few cycles of the AI trading logic and log the results to the console.
