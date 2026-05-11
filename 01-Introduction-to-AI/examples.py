#!/usr/bin/env python3
"""
Introduction to AI - Code Examples
Demonstrates basic AI concepts and problem-solving
"""

import random
from typing import List, Tuple


class AIBasics:
    """Basic AI concepts and examples"""

    @staticmethod
    def simple_decision_tree(age: int, income: float) -> str:
        """
        Simple rule-based decision system (Expert System)
        Example: Loan approval system
        """
        if age < 18:
            return "Ineligible: Too young"
        elif income < 20000:
            return "Rejected: Income too low"
        elif age > 65:
            return "Requires additional review"
        else:
            return "Approved"

    @staticmethod
    def turing_test_simulator():
        """
        Simple Turing test - Q&A system
        Demonstrates conversational AI basics
        """
        responses = {
            "What is AI?": "AI is the simulation of human intelligence by machines.",
            "What can AI do?": "AI can perceive, reason, learn, and make decisions.",
            "Is AI conscious?": "Current AI systems are not conscious, though it's a philosophical question.",
            "What are AI winters?": "Periods of reduced AI funding and progress due to unmet expectations.",
            "What is machine learning?": "A subset of AI where systems learn patterns from data."
        }
        
        question = input("Ask a question: ")
        return responses.get(question, "I don't know the answer to that question.")

    @staticmethod
    def classify_iris(sepal_length: float, sepal_width: float, 
                     petal_length: float, petal_width: float) -> str:
        """
        Simple iris flower classification (like ML)
        Rule-based approximation of ML classifier
        """
        if petal_length < 2.5:
            return "Setosa"
        elif petal_length < 4.8:
            if petal_width < 1.7:
                return "Versicolor"
            else:
                return "Virginica"
        else:
            return "Virginica"

    @staticmethod
    def game_ai_minimax(board_state: List[int]) -> int:
        """
        Simple minimax for tic-tac-toe
        Demonstrates game-playing AI
        
        Board: [0-8] representing 3x3 grid
        0: empty, 1: AI, -1: human
        """
        
        def check_winner(state):
            """Check if there's a winner"""
            lines = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
                    [0, 3, 6], [1, 4, 7], [2, 5, 8],
                    [0, 4, 8], [2, 4, 6]]
            
            for line in lines:
                if state[line[0]] == state[line[1]] == state[line[2]] != 0:
                    return state[line[0]]
            return None
        
        def minimax(state, is_ai):
            """Minimax algorithm"""
            winner = check_winner(state)
            
            if winner == 1:
                return 10
            elif winner == -1:
                return -10
            elif 0 not in state:
                return 0
            
            if is_ai:
                max_score = -float('inf')
                for i in range(9):
                    if state[i] == 0:
                        state[i] = 1
                        score = minimax(state, False)
                        state[i] = 0
                        max_score = max(score, max_score)
                return max_score
            else:
                min_score = float('inf')
                for i in range(9):
                    if state[i] == 0:
                        state[i] = -1
                        score = minimax(state, True)
                        state[i] = 0
                        min_score = min(score, min_score)
                return min_score
        
        best_score = -float('inf')
        best_move = None
        
        for i in range(9):
            if board_state[i] == 0:
                board_state[i] = 1
                score = minimax(board_state, False)
                board_state[i] = 0
                
                if score > best_score:
                    best_score = score
                    best_move = i
        
        return best_move

    @staticmethod
    def neural_network_simulation():
        """
        Simple neural network simulation
        Demonstrates how neural networks work
        """
        class SimpleNeuralNet:
            def __init__(self, learning_rate=0.1):
                self.w1 = random.random()
                self.w2 = random.random()
                self.b = random.random()
                self.lr = learning_rate
            
            def sigmoid(self, x):
                return 1 / (1 + 2.71828 ** -x)
            
            def sigmoid_derivative(self, x):
                return x * (1 - x)
            
            def forward(self, x1, x2):
                return self.sigmoid(self.w1 * x1 + self.w2 * x2 + self.b)
            
            def train(self, x1, x2, y, epochs=100):
                for _ in range(epochs):
                    # Forward pass
                    output = self.forward(x1, x2)
                    
                    # Calculate error
                    error = y - output
                    
                    # Backpropagation
                    d_output = error * self.sigmoid_derivative(output)
                    
                    # Update weights
                    self.w1 += d_output * x1 * self.lr
                    self.w2 += d_output * x2 * self.lr
                    self.b += d_output * self.lr
        
        return SimpleNeuralNet()


def main():
    """Run all examples"""
    print("=" * 60)
    print("Artificial Intelligence - Practical Examples")
    print("=" * 60)
    
    # Example 1: Decision Tree
    print("\n1. Decision Tree (Expert System)")
    print("-" * 40)
    print(f"Age 25, Income $50,000: {AIBasics.simple_decision_tree(25, 50000)}")
    print(f"Age 16, Income $30,000: {AIBasics.simple_decision_tree(16, 30000)}")
    print(f"Age 70, Income $60,000: {AIBasics.simple_decision_tree(70, 60000)}")
    
    # Example 2: Classification
    print("\n2. Iris Flower Classification (ML)")
    print("-" * 40)
    print(f"Flower 1: {AIBasics.classify_iris(5.1, 3.5, 1.4, 0.2)}")
    print(f"Flower 2: {AIBasics.classify_iris(6.2, 2.9, 4.3, 1.3)}")
    print(f"Flower 3: {AIBasics.classify_iris(7.7, 3.0, 6.1, 2.3)}")
    
    # Example 3: Tic-Tac-Toe AI
    print("\n3. Game AI - Tic-Tac-Toe (Minimax)")
    print("-" * 40)
    board = [0] * 9
    move = AIBasics.game_ai_minimax(board)
    print(f"AI's best first move: Position {move}")
    
    # Example 4: Neural Network
    print("\n4. Simple Neural Network")
    print("-" * 40)
    nn = AIBasics.neural_network_simulation()
    print(f"Initial output for (0.5, 0.5): {nn.forward(0.5, 0.5):.4f}")
    nn.train(0.5, 0.5, 1.0, epochs=1000)
    print(f"After training for (0.5, 0.5): {nn.forward(0.5, 0.5):.4f}")
    
    # Example 5: AI Applications
    print("\n5. AI Applications Summary")
    print("-" * 40)
    applications = {
        "Healthcare": "Disease diagnosis, drug discovery",
        "Finance": "Fraud detection, trading algorithms",
        "Transportation": "Autonomous vehicles, traffic optimization",
        "Entertainment": "Recommendations, game AI",
        "Manufacturing": "Quality control, predictive maintenance"
    }
    for domain, use_case in applications.items():
        print(f"• {domain}: {use_case}")
    
    print("\n" + "=" * 60)
    print("Examples completed! Ready to learn more?")
    print("=" * 60)


if __name__ == "__main__":
    main()
