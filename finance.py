import random
print("Welcome to Finance Quiz")
finance_questions = {
    1: {
        "question": "What is the study of how individuals and societies allocate scarce resources?",
        "options": {
            "a": "Finance",
            "b": "Economics",
            "c": "Accounting",
            "d": "Marketing",
        },
        "correct_answer": "b",
        "hint": "It's a social science dealing with production, distribution, and consumption of goods."
    },
    2: {
        "question": "What term refers to the total value of goods and services produced within a country?",
        "options": {
            "a": "Gross Domestic Product (GDP)",
            "b": "Gross National Product (GNP)",
            "c": "Consumer Price Index (CPI)",
            "d": "Consumer Confidence Index (CCI)",
        },
        "correct_answer": "a",
        "hint": "It's a key economic indicator reflecting a nation's economic performance."
    },
    3: {
        "question": "Which economic system relies on supply and demand to determine resource allocation?",
        "options": {
            "a": "Capitalism",
            "b": "Communism",
            "c": "Socialism",
            "d": "Mercantilism",
        },
        "correct_answer": "a",
        "hint": "It's associated with a free market approach."
    },
    4: {
        "question": "In finance, what term is used to describe the interest rate that banks charge each other for short-term loans?",
        "options": {
            "a": "Prime Rate",
            "b": "Federal Funds Rate",
            "c": "Discount Rate",
            "d": "LIBOR",
        },
        "correct_answer": "b",
        "hint": "It's a key tool for central banks to control monetary policy."
    },
    5: {
        "question": "Which type of unemployment occurs due to fluctuations in the business cycle?",
        "options": {
            "a": "Structural Unemployment",
            "b": "Frictional Unemployment",
            "c": "Cyclical Unemployment",
            "d": "Seasonal Unemployment",
        },
        "correct_answer": "c",
        "hint": "This type of unemployment is linked to economic health."
    },
    6: {
        "question": "What term describes a situation where a country imports more than it exports?",
        "options": {
            "a": "Trade Deficit",
            "b": "Trade Surplus",
            "c": "Balance of Trade",
            "d": "Current Account Deficit",
        },
        "correct_answer": "a",
        "hint": "It can lead to currency value decrease."
    },
    7: {
        "question": "What is the primary purpose of antitrust laws in economics?",
        "options": {
            "a": "To encourage monopolistic behavior",
            "b": "To promote fair competition and prevent monopolies",
            "c": "To protect intellectual property rights",
            "d": "To regulate international trade",
        },
        "correct_answer": "b",
        "hint": "They prevent market power abuse."
    },
    8: {
        "question": "In finance, what does 'P/E ratio' measure?",
        "options": {
            "a": "A company's debt-to-equity ratio",
            "b": "The return on investment for a stock",
            "c": "The market value of a stock relative to its earnings per share",
            "d": "The growth rate of a company's earnings",
        },
        "correct_answer": "c",
        "hint": "It assesses relative stock valuation."
    },
    9: {
        "question": "Which type of monetary policy tool is used to control the money supply?",
        "options": {
            "a": "Fiscal policy",
            "b": "Open market operations",
            "c": "Quantitative easing",
            "d": "Supply-side policy",
        },
        "correct_answer": "b",
        "hint": "It involves buying or selling government securities."
    },
    10: {
        "question": "Which economic indicator measures the percentage change in the price level of goods and services?",
        "options": {
            "a": "Gross Domestic Product (GDP)",
            "b": "Consumer Price Index (CPI)",
            "c": "Producer Price Index (PPI)",
            "d": "Retail Sales Index (RSI)",
        },
        "correct_answer": "b",
        "hint": "It tracks inflation trends."
    },
    11: {
        "question": "What term describes the cost of forgoing the next best alternative when making a decision?",
        "options": {
            "a": "Opportunity cost",
            "b": "Marginal cost",
            "c": "Sunk cost",
            "d": "Average cost",
        },
        "correct_answer": "a",
        "hint": "A fundamental concept in economics."
    },
    12: {
        "question": "Which market structure consists of a large number of small firms selling identical products?",
        "options": {
            "a": "Monopoly",
            "b": "Oligopoly",
            "c": "Perfect competition",
            "d": "Monopolistic competition",
        },
        "correct_answer": "c",
        "hint": "No product differentiation in this structure."
    },
    13: {
        "question": "In finance, what does 'ETF' stand for?",
        "options": {
            "a": "Estimated Trading Fund",
            "b": "Exchange Traded Fund",
            "c": "Equity Trust Fund",
            "d": "Extended Treasury Fund",
        },
        "correct_answer": "b",
        "hint": "It's a type of investment fund traded on stock exchanges."
    },
    14: {
        "question": "What term describes a situation where the price of goods and services increases over time?",
        "options": {
            "a": "Inflation",
            "b": "Recession",
            "c": "Deflation",
            "d": "Stagflation",
        },
        "correct_answer": "a",
        "hint": "It erodes purchasing power of money."
    },
    15: {
        "question": "Which monetary policy tool involves changing the reserve requirements for banks?",
        "options": {
            "a": "Open market operations",
            "b": "Discount rate",
            "c": "Reserve ratio",
            "d": "Quantitative easing",
        },
        "correct_answer": "c",
        "hint": "It determines how much banks must hold in reserves."
    },
    16: {
        "question": "What is the primary goal of contractionary fiscal policy?",
        "options": {
            "a": "To reduce unemployment",
            "b": "To stimulate economic growth",
            "c": "To decrease government spending",
            "d": "To control inflation",
        },
        "correct_answer": "d",
        "hint": "It involves reducing government spending and increasing taxes."
    },
    17: {
        "question": "In economics, what term is used for the ability to produce a good at a lower opportunity cost than others?",
        "options": {
            "a": "Comparative advantage",
            "b": "Absolute advantage",
            "c": "Marginal advantage",
            "d": "Production advantage",
        },
        "correct_answer": "a",
        "hint": "It's the basis for international trade."
    },
    18: {
        "question": "Which type of risk is associated with changes in interest rates?",
        "options": {
            "a": "Credit risk",
            "b": "Market risk",
            "c": "Operational risk",
            "d": "Liquidity risk",
        },
        "correct_answer": "b",
        "hint": "Also known as interest rate risk."
    },
    19: {
        "question": "What term describes a situation where the government spends more than it collects in revenue?",
        "options": {
            "a": "Budget surplus",
            "b": "Budget deficit",
            "c": "National debt",
            "d": "Fiscal deficit",
        },
        "correct_answer": "b",
        "hint": "It leads to increased national debt."
    },
    20: {
        "question": "What is the main function of a central bank in an economy?",
        "options": {
            "a": "To regulate the stock market",
            "b": "To control fiscal policy",
            "c": "To manage foreign exchange rates",
            "d": "To control the money supply and monetary policy",
        },
        "correct_answer": "d",
        "hint": "It influences interest rates and inflation."
    },
    21: {
        "question": "Which economic theory advocates for limited government intervention in the economy and emphasizes individual self-interest?",
        "options": {
            "a": "Keynesian economics",
            "b": "Classical economics",
            "c": "Behavioral economics",
            "d": "Marxist economics",
        },
        "correct_answer": "b",
        "hint": "Associated with Adam Smith's 'The Wealth of Nations.'"
    },
    22: {
        "question": "What term is used to describe a situation where the quantity demanded exceeds the quantity supplied at a given price?",
        "options": {
            "a": "Surplus",
            "b": "Shortage",
            "c": "Equilibrium",
            "d": "Scarcity",
        },
        "correct_answer": "b",
        "hint": "Indicates that the price is too low."
    },
    23: {
        "question": "In finance, what does the acronym IPO stand for?",
        "options": {
            "a": "Initial Public Offering",
            "b": "International Portfolio Organization",
            "c": "Investment and Portfolio Optimization",
            "d": "Integrated Public Offering",
        },
        "correct_answer": "a",
        "hint": "First sale of stock by a private company to the public."
    },
    24: {
        "question": "What is the term for a sustained period of economic downturn characterized by falling GDP and rising unemployment?",
        "options": {
            "a": "Boom",
            "b": "Recession",
            "c": "Depression",
            "d": "Recovery",
        },
        "correct_answer": "b",
        "hint": "A phase of the business cycle."
    },
    25: {
        "question": "In finance, what term describes a measure of an asset's price volatility?",
        "options": {
            "a": "Beta",
            "b": "Alpha",
            "c": "Sharpe ratio",
            "d": "Standard deviation",
        },
        "correct_answer": "d",
        "hint": "Quantifies historical price fluctuations."
    },
    26: {
        "question": "What is the term for a sustained period of economic downturn characterized by falling GDP and rising unemployment?",
        "options": {
            "a": "Boom",
            "b": "Recession",
            "c": "Depression",
            "d": "Recovery",
        },
        "correct_answer": "b",
        "hint": "A phase of the business cycle."
    },
    27: {
        "question": "In finance, what term is used to describe the risk of a loss arising from a change in foreign exchange rates?",
        "options": {
            "a": "Currency risk",
            "b": "Market risk",
            "c": "Interest rate risk",
            "d": "Credit risk",
        },
        "correct_answer": "a",
        "hint": "Affects international investments."
    },
    28: {
        "question": "What term is used to describe the highest point of economic activity in a business cycle?",
        "options": {
            "a": "Boom",
            "b": "Recession",
            "c": "Depression",
            "d": "Recovery",
        },
        "correct_answer": "a",
        "hint": "Characterized by high employment and production."
    },
    29: {
        "question": "Which financial ratio measures a company's ability to meet its short-term obligations?",
        "options": {
            "a": "Debt-to-Equity Ratio",
            "b": "Current Ratio",
            "c": "Return on Equity (ROE)",
            "d": "Price-Earnings (P/E) Ratio",
        },
        "correct_answer": "b",
        "hint": "Compares current assets to current liabilities."
    },
    30: {
        "question": "What term describes the phenomenon where an increase in the money supply leads to an increase in prices without a corresponding increase in real output?",
        "options": {
            "a": "Hyperinflation",
            "b": "Stagflation",
            "c": "Demand-pull inflation",
            "d": "Cost-push inflation",
        },
        "correct_answer": "a",
        "hint": "Erodes value of money rapidly."
    },
    31: {
        "question": "Which international organization provides financial assistance and policy advice to its member countries?",
        "options": {
            "a": "World Trade Organization (WTO)",
            "b": "International Monetary Fund (IMF)",
            "c": "World Bank",
            "d": "United Nations (UN)",
        },
        "correct_answer": "b",
        "hint": "Plays a crucial role during financial crises."
    },
    32: {
        "question": "In finance, what term is used to describe a market condition where asset prices are declining?",
        "options": {
            "a": "Bull market",
            "b": "Bear market",
            "c": "Bullish trend",
            "d": "Sideways market",
        },
        "correct_answer": "b",
        "hint": "Pessimistic sentiment in the market."
    },
    33: {
        "question": "What term describes the highest point of economic activity in a business cycle?",
        "options": {
            "a": "Boom",
            "b": "Recession",
            "c": "Depression",
            "d": "Recovery",
        },
        "correct_answer": "a",
        "hint": "Characterized by high employment and production."
    },
    34: {
        "question": "Which type of unemployment occurs when workers are transitioning between jobs?",
        "options": {
            "a": "Structural unemployment",
            "b": "Frictional unemployment",
            "c": "Cyclical unemployment",
            "d": "Seasonal unemployment",
        },
        "correct_answer": "b",
        "hint": "Natural part of the labor market."
    },
    35: {
        "question": "In finance, what term is used for the interest rate that banks charge each other for short-term loans?",
        "options": {
            "a": "Prime Rate",
            "b": "Federal Funds Rate",
            "c": "Discount Rate",
            "d": "LIBOR",
        },
        "correct_answer": "b",
        "hint": "Key tool for central banks' monetary policy."
    },
    36: {
        "question": "Which economic concept suggests that as income increases, the proportion spent on goods decreases?",
        "options": {
            "a": "Engel's law",
            "b": "Laffer curve",
            "c": "Pareto efficiency",
            "d": "Phillips curve",
        },
        "correct_answer": "a",
        "hint": "Relates to consumption patterns."
    },
    37: {
        "question": "What term describes the cost of forgoing the next best alternative when making a decision?",
        "options": {
            "a": "Opportunity cost",
            "b": "Marginal cost",
            "c": "Sunk cost",
            "d": "Average cost",
        },
        "correct_answer": "a",
        "hint": "Fundamental concept in economics."
    },
    38: {
        "question": "Which market structure consists of a single seller dominating the entire market?",
        "options": {
            "a": "Oligopoly",
            "b": "Monopolistic competition",
            "c": "Monopoly",
            "d": "Perfect competition",
        },
        "correct_answer": "c",
        "hint": "Characterized by absence of competition."
    },
    39: {
        "question": "In economics, what term is used for the ability to produce a good at a lower opportunity cost than others?",
        "options": {
            "a": "Comparative advantage",
            "b": "Absolute advantage",
            "c": "Marginal advantage",
            "d": "Production advantage",
        },
        "correct_answer": "a",
        "hint": "Basis for international trade."
    },
    40: {
        "question": "What term describes a situation where a country imports more than it exports?",
        "options": {
            "a": "Trade Deficit",
            "b": "Trade Surplus",
            "c": "Balance of Trade",
            "d": "Current Account Deficit",
        },
        "correct_answer": "a",
        "hint": "Can lead to currency value decrease."
    },
    41: {
        "question": "What is the primary purpose of antitrust laws in economics?",
        "options": {
            "a": "To encourage monopolistic behavior",
            "b": "To promote fair competition and prevent monopolies",
            "c": "To protect intellectual property rights",
            "d": "To regulate international trade",
        },
        "correct_answer": "b",
        "hint": "Prevent market power abuse."
    },
    42: {
        "question": "In finance, what does 'P/E ratio' measure?",
        "options": {
            "a": "A company's debt-to-equity ratio",
            "b": "The return on investment for a stock",
            "c": "The market value of a stock relative to its earnings per share",
            "d": "The growth rate of a company's earnings",
        },
        "correct_answer": "c",
        "hint": "Assesses relative stock valuation."
    },
    43: {
        "question": "Which type of monetary policy tool is used to control the money supply?",
        "options": {
            "a": "Fiscal policy",
            "b": "Open market operations",
            "c": "Quantitative easing",
            "d": "Supply-side policy",
        },
        "correct_answer": "b",
        "hint": "Involves buying or selling government securities."
    },
    44: {
        "question": "What term is used to describe a situation where the quantity demanded exceeds the quantity supplied at a given price?",
        "options": {
            "a": "Surplus",
            "b": "Shortage",
            "c": "Equilibrium",
            "d": "Scarcity",
        },
        "correct_answer": "b",
        "hint": "Indicates that the price is too low."
    },
    45: {
        "question": "In finance, what does the acronym IPO stand for?",
        "options": {
            "a": "Initial Public Offering",
            "b": "International Portfolio Organization",
            "c": "Investment and Portfolio Optimization",
            "d": "Integrated Public Offering",
        },
        "correct_answer": "a",
        "hint": "First sale of stock by a private company to the public."
    },
    46: {
        "question": "What is the term for a sustained period of economic downturn characterized by falling GDP and rising unemployment?",
        "options": {
            "a": "Boom",
            "b": "Recession",
            "c": "Depression",
            "d": "Recovery",
        },
        "correct_answer": "b",
        "hint": "A phase of the business cycle."
    },
    47: {
        "question": "In finance, what term is used to describe a measure of an asset's price volatility?",
        "options": {
            "a": "Beta",
            "b": "Alpha",
            "c": "Sharpe ratio",
            "d": "Standard deviation",
        },
        "correct_answer": "d",
        "hint": "Quantifies historical price fluctuations."
    },
    48: {
        "question": "What term describes the cost of forgoing the next best alternative when making a decision?",
        "options": {
            "a": "Opportunity cost",
            "b": "Marginal cost",
            "c": "Sunk cost",
            "d": "Average cost",
        },
        "correct_answer": "a",
        "hint": "Fundamental concept in economics."
    },
    49: {
        "question": "Which market structure consists of a large number of small firms selling identical products?",
        "options": {
            "a": "Monopoly",
            "b": "Oligopoly",
            "c": "Perfect competition",
            "d": "Monopolistic competition",
        },
        "correct_answer": "c",
        "hint": "No product differentiation in this structure."
    },
    50: {
        "question": "In economics, what term is used for the ability to produce a good at a lower opportunity cost than others?",
        "options": {
            "a": "Comparative advantage",
            "b": "Absolute advantage",
            "c": "Marginal advantage",
            "d": "Production advantage",
        },
        "correct_answer": "a",
        "hint": "Basis for international trade."
    }
}
def select_random_questions(finance_questions, num_questions=10):
    question_keys = list(finance_questions.keys())
    random.shuffle(question_keys)
    selected_questions = {key: finance_questions[key] for key in question_keys[:num_questions]}
    return selected_questions

def display_question(question_number, question_info):
    print(f"Question {question_number}: {question_info['question']}")
    print("Options:")
    for option, text in question_info['options'].items():
        print(f"{option}: {text}")
    return input("Your answer: ").lower()

def main():
    num_questions = 10
    selected_questions = select_random_questions(finance_questions, num_questions)

    correct_answers = 0
    for idx, (question_number, question_info) in enumerate(selected_questions.items(), start=1):
        user_answer = display_question(idx, question_info)
        if user_answer == question_info['correct_answer']:
            print("Correct!\n")
            correct_answers += 1
        else:
            print(f"Wrong! The correct answer is {question_info['correct_answer']}\n")

    print(f"You answered {correct_answers} out of {num_questions} questions correctly.")

if __name__ == "__main__":
    main()